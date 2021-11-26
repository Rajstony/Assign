import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 8,
                    'VolumeType': 'gp2'
            },
        },
    ],
     ImageId = 'ami-00782a7608c7fc226',
     MinCount=2,
     MaxCount=3,
     InstanceType='t2.micro',
     KeyName='assign',
     TagSpecifications=[
        {
        'ResourceType': 'instance',
        'Tags': [
            {
             'Key': 'Name',
             'Value':'murugt-hu-script'
            }

        ]
    }]
        
)