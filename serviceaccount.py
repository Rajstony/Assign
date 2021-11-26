import os
from google.oauth2 import service_account
from google.cloud import googleapiclient


project_id="us-gcp-ame-con-116-npd-1"
service = googleapiclient.discovery.build('iam', 'v1')

service_accounts = service.projects().serviceAccounts().list(
    name='projects/'  +project_id).execute()

for account in service_accounts['accounts']:
    with open("randomfile.txt", "a") as o:
        print('Name:' +account['name']+"\n")
        print('Email:' +account['email']+"\n")
        print("\n")

print("Done")
