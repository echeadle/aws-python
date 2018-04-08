import boto3

conn=boto3.client('ec2')
response=conn.create_security_group(GroupName='mywebgroup',Description="SG for web", VpcId="vpc-60a0b007")

print(response)
