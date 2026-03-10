#!/usr/bin/env python3

import logging
import os
import requests
import pandas as pd
import mysql.connector
API_URL = "http://api.open-notify.org/iss-now.json"
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = "iss"

REPORTER_ID = "thc8mr"
REPORTER_NAME = "Esther Casco"

def get_connection():
    db = mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME
    )
    return db

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger()

def extract(logger):
    logger.info("Extracting")
    try:
        r= requests.get(API_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        logger.info("Extracting is a success")
        return data
    except Exception as e:
        logger.error(f"the Extraction error: {e}")
        return None

def transform(data, logger):
    logger.info("Transforming")

    ts_unix = data["timestamp"]
    lat = float(data["iss_position"]["latitude"])
    lon = float(data["iss_position"]["longitude"])
    message = data["message"]

    ts_readable = pd.to_datetime(ts_unix, unit="s", utc=True)
    ts_str = ts_readable.strftime("%Y-%m-%d %H:%M:%S UTC")

    row = {
        "message": message,
        "timestamp": ts_str,
        "latitude": lat,
        "longitude": lon
    }

    df = pd.DataFrame([row])
    logger.info("Transform is done")
    return df

def register_reporter(logger):
    logger.info("Checking reporter")

    db = None
    cursor = None

    try:
        db = get_connection()
        cursor = db.cursor()

        check_query = "SELECT reporter_id FROM reporters WHERE reporter_id = %s"
        cursor.execute(check_query, (REPORTER_ID,))
        result = cursor.fetchone()

        if result is None:
            insert_query = "INSERT INTO reporters (reporter_id, reporter_name) VALUES (%s, %s)"
            cursor.execute(insert_query, (REPORTER_ID, REPORTER_NAME))
            db.commit()
            logger.info("Reporter added")
        else:
            logger.info("Reporter already exists")

    except Exception as e:
        logger.error(f"Reporter error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

def load(df, logger):
    logger.info("Loading into MySQL")

    db = None
    cursor = None

    try:
        db = get_connection()
        cursor = db.cursor()

        row = df.iloc[0]

        insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            row["message"],
            row["latitude"],
            row["longitude"],
            row["timestamp"],
            REPORTER_ID
        )

        cursor.execute(insert_query, values)
        db.commit()
        logger.info("Load is done")

    except Exception as e:
        logger.error(f"Load error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


def main():
    logger = setup_logger()
    logger.info("Starting ETL")

    register_reporter(logger)

    data = extract(logger)

    if data is None:
        logger.error("Stopping because extract failed")
        return

    df = transform(data, logger)
    load(df, logger)

    logger.info("ETL Finished")
    print(df)



if __name__ == "__main__":
    main()
