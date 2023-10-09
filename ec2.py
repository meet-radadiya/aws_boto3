from decouple import config
import boto3
import sys

ec2 = boto3.client('ec2',
                   aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
                   aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
                   region_name="ap-south-1")

# print(ec2.describe_instances())

# Create Instance
# conn = ec2.run_instances(InstanceType="t2.micro",
#                          MaxCount=1,
#                          MinCount=1,
#                          ImageId="ami-0f5ee92e2d63afc18")
#
# print(conn)

# Terminate Instance
# response = ec2.terminate_instances(InstanceIds=['i-06f38d0a543581d96'])
# print(response)
