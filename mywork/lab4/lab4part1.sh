#!/bin/bash

# Define your bucket name and file path
BUCKET_NAME="ds2002-tvy6kv"
FILE_PATH="C:\Users\quent\Documents\DS2002\ds2002-course\mywork\lab4"
curl https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png > google.png
FILE = google.png
# Upload the file to S3
aws s3 cp $FILE  s3://$BUCKET_NAME/

# Generate a presigned URL
aws s3 presign s3://$BUCKET_NAME/$FILE --expires-in 604800
