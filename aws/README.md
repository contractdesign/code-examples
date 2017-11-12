# Amazon Web Services CLI

Amazon Web Services offers a commandline interface (CLI) to control
its cloud services.  They typically start with ```aws``` followed by
the service name (e.g., ec2 or s3).  The notes below cover the CLI
commands for their elastic cloud 2 (EC2) service, which provisions
virtual machines on demand.


## Credentials

Before running these commands, you will need to enter your AWS
credential into the CLI tool using ```aws configure```.  This command
requests your access key ID, secret key and default region.


## Start an EC2 Instance

To start an EC2 instance, use the command below.  Before doing so for
the first time, you will probably need to go through the web interface
and note the instance ID, security group id and subnet.

```bash
$ aws ec2 run-instances \
--image-id ami-ID \
--instance-type t2.micro \
--key-name exp \
--security-group-ids sg-<ID> \
--subnet-id subnet-<ID>
 ```

## List Instances

To list running instances, use ```describe-instances```.  This command
outputs a large JSON file, so ```jq``` can print out fields of
interest, such as the instance's public IP address or status.

```bash
$ aws ec2 describe-instances | \
  jq -r '.Reservations[].Instances[] | .InstanceId + "\t" + .State.Name + "\t" + .PublicIpAddress'
```

## Terminate Instances

To terminate running instances, use the command below.  The instance
ids of the running VMs can be retrieved using ```aws ec2
describe-instances``` as described previously.

```bash
$ aws ec2 terminate-instances --instance-ids <IDs>
```
