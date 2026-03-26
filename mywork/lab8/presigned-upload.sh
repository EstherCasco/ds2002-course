#!/bin/bash

file=$1
bucket=$2
expire=$3

aws s3 cp "$file" "s3://$bucket/"
aws s3 presign --expires-in "$expire" "s3://$bucket/$(basename "$file")"
