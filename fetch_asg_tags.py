
import boto3
import csv
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='Environment info')
parser.add_argument('--environment', dest='environment', type=str, help='environment name')

args = parser.parse_args()

print(args.environment)

client = boto3.client('autoscaling')
paginator = client.get_paginator('describe_auto_scaling_groups')
page_iterator = paginator.paginate(
            PaginationConfig={'PageSize': 100}
            )
#filtered_asgs = page_iterator.search('AutoScalingGroups[]')
filtered_asgs = page_iterator.search(
                    'AutoScalingGroups[] | [?contains(Tags[?Key==`{}`].Value, `{}`) && contains(Tags[?Key==`{}`].Value, `{}`)]'.format(
                                                'product', 'dynamo','environment',args.environment)
                    )
mylist = []
#print(filtered_asgs)
#print(type(filtered_asgs))
#print(list(filtered_asgs))
mylist = list(filtered_asgs)
print(mylist)

try:
            open('result_asg_tags.csv', 'w').close()
except IOError:
            print('Failure')

for asg in filtered_asgs:
    #print(asg['Tags'])
    my_list = asg['Tags']
    df = pd.DataFrame(my_list)
    df.to_csv('result_asg_tags.csv', mode='a')


if mylist:
    print("SCRIPT RUN SUCCESSFULL - fetched ASG Tags for - " + args.environment)
    print("File location to download: ", os.getcwd() + "/result_asg_tags.csv")
else:
    print("SCRIPT RUN FAILED - NO ASG Tags were available")
