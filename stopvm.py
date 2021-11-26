import boto3
region = 'ap-south-1'
instances = ['i-0e345045bfb33e61b', 'i-04eda5021d72baf47']
ec2 = boto3.client('ec2', region_name=region)
ec2.terminate_instances(InstanceIds=instances)
print('Have been terminated: ' + str(instances))