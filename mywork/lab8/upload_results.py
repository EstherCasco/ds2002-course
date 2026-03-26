import sys
import os
import glob
import logging
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    """Get input folder and destination from command line."""
    input_folder = sys.argv[1]
    destination = sys.argv[2]
    return input_folder, destination

def upload(input_folder, destination):
    """Upload results-*.csv files to S3."""
    try:
        s3 = boto3.client("s3", region_name="us-east-1")

        parts = destination.split("/", 1)
        bucket = parts[0]

        if len(parts) > 1:
            prefix = parts[1]
        else:
            prefix = ""

        if prefix != "" and not prefix.endswith("/"):
            prefix = prefix + "/"

        files = glob.glob(input_folder + "/results-*.csv")

        for file_name in files:
            short_name = os.path.basename(file_name)
            key = prefix + short_name
            s3.upload_file(file_name, bucket, key)
            logger.info("uploaded %s to s3://%s/%s", file_name, bucket, key)

        return True

    except Exception as e:
        logger.error("upload failed: %s", e)
        return False

def main():
    """Run the upload process."""
    input_folder, destination = parse_args()
    success = upload(input_folder, destination)

    if success:
        logger.info("upload completed successfully")
    else:
        logger.info("upload failed")

if __name__ == "__main__":
    main()
