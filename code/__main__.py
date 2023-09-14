"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2
# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

#Security Group (2 inbound rule and 1 outbound)
sg = ec2.SecurityGroup('web-server-sg', description='security group for web servers')

allow_ssh  = ec2.SecurityGroupRule("AllowSSH", type='ingress',from_port=22, to_port=22 ,protocol="tcp", cidr_blocks=["0.0.0.0/0"], security_group_id=sg.id)
allow_http = ec2.SecurityGroupRule("AllowHTTP", type='ingress',from_port=80, to_port=80 ,protocol="tcp", cidr_blocks=["0.0.0.0/0"], security_group_id=sg.id)
allow_all  = ec2.SecurityGroupRule("AllowHTTP", type='egress',from_port=0, to_port=0 , protocol="-1", cidr_blocks=["0.0.0.0/0"], security_group_id=sg.id)

#Different instances
instance_names = ['web1','web2','web3']
output_public_ip = []
for instance in instance_names:
    # Create an AWS resource (EC2 Instance)
    ec2_instance = ec2.Instance(instance,ami="ami-053b0d53c279acc90", instance_type="t3.nano", key_name='test',vpc_security_group_ids=[sg.id], tags ={
    "Name": instance
})    
    output_public_ip.append(ec2_instance.public_ip)


pulumi.export('public_ip', output_public_ip)
pulumi.export('instance_url',pulumi.Output.concat("http://",ec2.instance.public_dns)) 