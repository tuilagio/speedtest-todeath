import os
from time import sleep

#os.system("speedtest-cli --csv")
os.system("git clone https://github.com/sivel/speedtest-cli.git")
# os.system("cd ")
os.system("python ./speedtest-cli/speedtest.py --csv-header >> result.csv")
os.system("python ./speedtest-cli/speedtest.py --list >> servers.txt")

with open('servers.txt') as fp:
    #with open("serverIDs.txt") as fp1
    for line in fp:
        if line[0] == "R":
            continue
        print "testing: " + line
        id = line.split(')')[0]
        os.system("speedtest-cli --csv --server " +id+ " >> result.csv")
        print "Sleep for 10 sec"
        sleep(10)
