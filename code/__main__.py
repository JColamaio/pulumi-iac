"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2
# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Create an AWS resource (EC2 Instance)
ec2_instance = ec2.Instance('web-server',ami="ami-053b0d53c279acc90", instance_type="t3.nano", key_name='test', tags ={
    "Name": "web"
})

pulumi.export('public_ip', ec2_instance.public_ip)