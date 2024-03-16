import boto3
import requests

# Download a file from the internet
file_url = "https://files.worldwildlife.org/wwfcmsprod/images/Tiger_resting_Bandhavgarh_National_Park_India/hero_small/6aofsvaglm_Medium_WW226365.jpg"
local_filename = file_url.split('/')[-1]
response = requests.get(file_url)
open(local_filename, 'wb').write(response.content)

# Define AWS S3 details
bucket_name = 'ds2002-tvy6kv'
object_name = local_filename

# Upload the file to S3
s3_client = boto3.client('s3')
with open(local_filename, "rb") as f:
    s3_client.upload_fileobj(f, bucket_name, object_name)

# Generate a presigned URL
url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=604800)
print(url)
