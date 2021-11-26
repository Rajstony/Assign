import boto3

import logging

ec2 = boto3.resource('ec2')

logging.basicConfig(filename="app_plan.log",level=logging.INFO)

# create a new EC2 instance

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

ImageId='ami-00782a7608c7fc226',

MinCount=1,

MaxCount=2,

InstanceType='t2.micro',

KeyName='sharadhi-key',

TagSpecifications=[

{

'ResourceType': 'instance',

'Tags': [

{

'Key': 'Name',

'Value': "sharadhihu19load"

}

]

}]

)

logging.info(instances)

print("Instances created")