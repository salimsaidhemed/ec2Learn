AWS_ACCESS_KEY_ID = "AKIAWUJJPWO23RALYWX2"
AWS_SECRET_ACCESS_KEY = "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"
REGION = "us-east-2"
from boto.ec2 import connect_to_region

conn = connect_to_region(
    REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

ssh = conn.create_security_group('ssh','SSH Access Group')
ssh.authorize('tcp',22,22,'0.0.0.0/0')
reservation = conn.run_instances(
    'AMI ID',
    instance_type='t2.micro',
    key_name='Salim',
    security_group_ids=['ssh']
)
instance=reservation.instances[0]


