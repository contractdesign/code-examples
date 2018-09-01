
# Using the AWS CLI

This document contains notes on various commands using the AWS CLI.
Since many of the command options are long, tab completion is a must.
Add this line to your .bash See the
[AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-command-completion.html)
for other shells.

    complete -C '/usr/local/bin/aws_complete' aws



## S3 Bucket

Create a bucket with public permissions.  The bucket appears at
https://s3.amazonaws.com/exp-bucket  See
[restrictions](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html)

    $ aws s3api create-bucket --bucket exp-bucket --acl public-read --region us-east-1

Copy a file to a bucket

    $ aws s3 cp test.txt s3://exp-bucket/test.txt


## Public Keys

List key pairs

    aws ec2 describe-key-pairs

Create a key pair and save to a file

    aws ec2 create-key-pair --key-name <NAME> --query 'KeyMaterial' --output text > <NAME.pem>
    chmod 400 <NAME.pem>

Delete a key pair

    aws ec2 delete-key-pair --key-name exp


## EC2 Instances

List instances

    aws ec2 describe-instances

Create an EC2 instances from a stack.  See this
[blog post](https://medium.com/boltops/a-simple-introduction-to-aws-cloudformation-part-1-1694a41ae59d)
for more details.

    aws cloudformation create-stack --template-body file://single-instance.yml --stack-name single-instance --parameters ParameterKey=KeyName,ParameterValue=tutorial

To delete an instance
    aws ec2 terminate-instances --instance-ids <INSTANCE ID>
