import csv
import argparse


parser = argparse.ArgumentParser(description='file names to compare')
parser.add_argument('--oldfile', dest='oldfile', type=str, help='oldfilename')
parser.add_argument('--newfile', dest='newfile', type=str, help='newfilename')

args = parser.parse_args()

print("oldfile entered name =", args.oldfile)
print("newfile entered name =", args.newfile)

try:
            open('result_compare_files.csv', 'w').close()
except IOError:
            print('Failure')

with open(args.oldfile, 'r') as t1, open(args.newfile, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
with open('result_compare_files.csv', 'w') as outFile:
    counter =0
    for line in filetwo:
        if line not in fileone:
            print("This line is not in oldfile: ", line)
            outFile.write(line)
            counter +=1
    if counter == 0:
        print("BOTH FILES ARE EQUAL")
    else:
        print("BOTH FILES ARE NOT EQUAL")
