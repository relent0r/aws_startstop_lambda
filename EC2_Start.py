import boto3

def Start_Instance(region, owner):
    ec2client = boto3.client('ec2', region_name=region)
    ec2instObject = boto3.resource('ec2', region_name=region)
    ec2list = []
    result = {}
    response = {}
    
    tempDict = {'Name': 'tag:Owner', 'Values': [owner]}
    instFilters = [
        tempDict
        ]
    response = ec2client.describe_instances(Filters=instFilters)
    
    for r in response['Reservations']:
        for i in r['Instances']:
            print('Filter Based Instance ID is :' + i['InstanceId'])
            inst = (i['InstanceId'])
            ec2inst = ec2instObject.Instance(inst)
            print('Current State is :' + str(ec2inst.state["Code"]))
            if ec2inst.state["Code"] == 80 :
                print('EC2 Instance :' + str(inst) + ' is currently stopped, adding to start list')
                ec2list.append(inst)
            elif ec2inst.state["Code"] == 16 :
                print('EC2 Instance :' + str(inst) + ' is already running ignoring')
            else:
                print('EC2 Instance :' + str(inst) + ' is in an invalid state ignoring')
    
    if len(ec2list) == 0 :
        print('Instance list is empty, assume all EC2 are started or invalid state')
    else:
        result = ec2client.start_instances(InstanceIds=ec2list)
    
    if result:
        print('starting your instances : ' + str(ec2list))
    else:
        print('No changes made to instances :' + str(ec2list))

