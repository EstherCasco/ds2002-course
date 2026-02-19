#!/usr/bin/env python3

import sys 
import logging
import os
import requests
import pandas as pd

API_URL = "http://api.open-notify.org/iss-now.json"

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
    logger.info("transforming")
    ts_unix = data["timestamp"]
    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]
    ts_readable = pd.to_datetime(ts_unix, unit="s", utc=True)
    ts_str = ts_readable.strftime("%Y-%m-%d %H:%M:%S UTC")

    row = {
        "timestamp_unix": ts_unix,
        "timestamp_utc": ts_str,
        "latitude": lat,
        "longitude": lon
    }

    df=pd.DataFrame([row])
    logger.info("Transform is done")
    return df



def load(df, csv_file, logger):
    logger.info(f"writing to {csv_file}")
    file_exists = os.path.exists(csv_file)
    df.to_csv(csv_file, mode="a", header=(not file_exists), index = False)
    logger.info("The Load is done!")



def main():
    logger = setup_logger()
    if len(sys.argv) != 2:
        logger.error("Usage: python3 iss.py <output_csv_file>")
        sys.ext(1)

    csv_file = sys.argv[1]
    logger.info(f"Starting ETL. Output file = {csv_file}")
    data = extract(logger)

    if data is None:
        logger.error("Stopping because extract failed.")
        sys.exit(1)

    df = transform(data, logger)
    load(df, csv_file, logger)
    logger.info("ETL Finished!!!")
    
    



if __name__ == "__main__":
    main()