import os
from google.cloud import storage
#upload files
storage_client = storage.Client()

bucket_name="murugt-hu-script-bucket"
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob('s1-1.png')
blob.upload_from_filename('/users/murugt/desktop/s1-1.png')