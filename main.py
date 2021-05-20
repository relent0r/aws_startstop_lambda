print('Starting Start/Stop Task')
import EC2_Start
import EC2_Stop
import os

region = os.environ['var_Region']
## below is old stuff, but handy to keep for future reference
## instances_temp = os.environ['var_Instances']
## instances = list(instances_temp.split(","))


def lambda_handler(event, context):
    instOwner = event["Owner"]
    print('Current Owner is :' + instOwner)
    if event["Action"] == "Start":
        EC2_Start.Start_Instance(region, instOwner)
    elif event["Action"] =="Stop":
        EC2_Stop.Stop_Instance(region,  instOwner)
    else:
        print('Invalid Input')

    