import boto3

AWS_REGION = "us-west-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
VOLUME_ID = 'vol-02ac567ea3b2772e5'

snapshot = EC2_RESOURCE.create_snapshot(
    VolumeId=VOLUME_ID,
       TagSpecifications=[
           {
               'ResourceType': 'snapshot',
               'Tags': [
                   {
                    'Key':'Name',
                    'Value':'murugt-snapshot'
}
            ]
                    }
                      ]
                      )    
tag = snapshot.create_tags(
                {
                  'Key': 'Name',
                  'Value':'murugt-vol'
                }            
)
print(f'Snapshot {snapshot.id} created volume {VOLUME_ID}')

