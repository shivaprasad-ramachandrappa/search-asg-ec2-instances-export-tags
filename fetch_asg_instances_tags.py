import boto3
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='Environment info')
parser.add_argument('--environment', dest='environment', type=str, help='environment name')

args = parser.parse_args()

print(args.environment)

client = boto3.client('autoscaling')
ec2 = boto3.resource('ec2')

def get_instance_tags(instanceid):
    ec2instance = ec2.Instance(instanceid)
    #for tags in ec2instance.tags:
    return ec2instance.tags


paginator = client.get_paginator('describe_auto_scaling_groups')
page_iterator = paginator.paginate(
            PaginationConfig={'PageSize': 100}
            )
filtered_asgs = page_iterator.search(
            'AutoScalingGroups[] | [?contains(Tags[?Key==`{}`].Value, `{}`) && contains(Tags[?Key==`{}`].Value, `{}`)]'.format(
                        'product', 'dynamo','environment', args.environment)
            )

mylist = []
#print(filtered_asgs)
#print(type(filtered_asgs))
#print(list(filtered_asgs))
mylist = list(filtered_asgs)
print(mylist)

try:
        open('instances_list.txt', 'w').close()
except IOError:
        print('Failure')
for asg in filtered_asgs:
        print (asg['AutoScalingGroupName'])
        print( asg['Tags'])
        response = client.describe_auto_scaling_groups( AutoScalingGroupNames=[asg['AutoScalingGroupName'], ], MaxRecords=50)
        instances = response['AutoScalingGroups'][0]['Instances']
        for i in range(len(instances)):
            print(instances[i]['InstanceId'])
            with open('instances_list.txt', 'a') as the_file:
                the_file.write(instances[i]['InstanceId'] + '\n')
            tags_response = get_instance_tags(instances[i]['InstanceId'])
            print(tags_response)

try:
            open('result_asg_instances_tags.csv', 'w').close()
except IOError:
            print('Failure')
print('Calling Search_instance.py file to fetch and write the instances tags to csv')
try:
    if mylist:
        subprocess.call("python3 search_instances.py -i instances_list.txt -o result_asg_instances_tags.csv -r eu-west-1", shell=True)
        print('SCRIPT RUN SUCCESSFULL - Fetched ASG INSTANCE Tags for -' + args.environment)
        print("File location to download: ", os.getcwd() + "/result_asg_instances_tags.csv")
    else:
        print("SCRIPT RUN FAILED - NO ASG INSTANCE Tags were available")
except IOError:
                print('Failure in execution of search_instance.py')
