import boto3
elb=boto3.client('elb')
import logging
logging.basicConfig(filename="app_plan.log",level=logging.INFO)
lb1=elb.create_load_balancer(
    LoadBalancerName="murugt-load",
    Listeners= [
        {

          'Protocol':'HTTP',
          'LoadBalancerPort':80,
          'InstancePort':'HTTP',
          'InstancePort':80
        },
    ],
    AvailabilityZones=['ap-south-1a']
)

health_check=elb.configure_health_check(
    LoadBalancerName="murugt-load",
    HealthCheck = {
       'Target':'TCP:22',
       'Interval':10,
       'Timeout':5,
       'UnhealthyThreshold':5,
       'HealthyThreshold':5
    }
)


attach_instance=elb.register_instances_with_load_balancer(
       LoadBalancerName="murugt-load",
       Instances=[
       {
          "InstanceId": "i-04eda5021d72baf47"
        },
        {
           "InstanceId": "i-053b3969ba99dfaee"
        }
    ]
)

logging.info("ADDED")
print("instances mapped")