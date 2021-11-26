from google.cloud import storage

def list_bucket_object(bucketname):
    bucketname = "murugt-hu-script-bucket" 
    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucketname) 
    
    # List of all objects in bucket
    for blob in blobs:
        print(blob.name)