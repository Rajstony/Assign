import os
from google.cloud import storage

## Creating bucket
bucket_name = "murugt-hu-script-bucket"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
bucket.storage_class = "STANDARD"
new_bucket = storage_client.create_bucket(bucket, location="asia-southeast1")

print(
    "Bucket was created {} in {} with storage class {}".format(
        new_bucket.name, new_bucket.location, new_bucket.storage_class
    )
)

