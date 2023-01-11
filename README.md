## Search EC2 ASG  and Specific ASG Instances and Export Tags to CSV

This Project is used to pull Tag details to CSV pre and post deployment of RDA / DRIVE deployments You might be looking at a list of hundreds of instance ids or ip addresses and you'll be wondering what these instances are or who they belong to.  This project can help you answer that question.  This is a python script that takes in a list of instance-ids, private or public ipv4 addresses and searches for them in your AWS account.  For the ones it finds, it creates a CSV file that contains the combined tags of all the instances.  By looking at this CSV file, you should be able to better categorize these instances.

### Input Instance Tags Example

python3 fetch_asg_instances_tags.py --environment preprod

### Output Instance Tags Example

![Example Input](images/output_asg_instances_tags.PNG?raw=true "Title")

### Input ASG Tags Example

python3 fetch_asg_tags.py --environment preprod

### Output ASG Tags Example

![Example Input](images/output_asg_tags.PNG?raw=true "Title")


### Pre-requisites Installation
1. Login to AWS AWS CloudShell

2. Check Python3 availability

  ```
  python3 
  ```
3. Clone the git repo to Cloud shell
  ```
  git clone https://github.com/Sage/lsm-cloud-operations.git
  ```

4. Install packages:
  ```
  python3 -m pip3 install -r requirements.txt
  ```

### Script Usage
```
python3 fetch_asg_tags.py --environment preprod

python3 fetch_asg_instances_tags.py --environment preprod

python3 comparecsv.py --oldfile result_asg_instances_tags_old.csv --newfile result_asg_instances_tags.csv

Example syntax: python3 fetch_asg_tags.py --environment  XXXXX

Parameters:
1. --environment (required) - the options available are 'preprod' and 'production'.


Example syntax: python3 comparecsv.py --oldfile result_asg_instances_tags_old.csv --newfile result_asg_instances_tags.csv

Parameters:
1. --oldfile (required) - option to be mentioned is files that got created while we fetched the Tags before deployment.
2. --newfile (required) - option to be mentioned is files that got created while we fetched the Tags after deployment.

```

Examples:
```
1) python3 fetch_asg_tags.py --environment preprod
2) python3 fetch_asg_tags.py --environment production
3) python3 fetch_asg_instances_tags.py --environment preprod
4) python3 fetch_asg_instances_tags.py --environment production
```


### Download the csv file for comparing the Tags fetched

Examples:
(ASG Tags / ASG Instances Tags: Once the script run is successfull we get a link to the file below console output, Download the files from Actions tab given in AWS Cloudshell )
```
1) SCRIPT RUN SUCCESSFULL - Fetched ASG INSTANCE Tags for -production
File location to download:  /home/cloudshell-user/gitrepo/lsm-cloud-operations/SageDrive/TagsValidation/result_asg_instances_tags.csv
```
2) We can also compare the files by compare script using below commands:
```
python3 comparecsv.py --oldfile result_asg_instances_tags_old.csv --newfile result_asg_instances_tags.csv
```


