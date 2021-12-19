import os
import random
import urllib3
import time

if os.name != "posix":
	exit()

https_PoolManager = urllib3.PoolManager()

def log(logging_ips):
	logs = open('ips.txt', 'a')
	logs.write(logging_ips)
	logs.close()

def timeout():
	print('a')
	time.sleep(64)

def appendtopool():
	print("appending to pool")
	os.system('git pull https://github.com/Zsobix/IP-Guesser.pool.git main')
	print("done! Zsobix gonna automerge problably 2days later")
	time.sleep(4)

while True:
	openips = open('ips.txt', 'r')
	openips2 = openips.read()
	ipnum1 = random.randint(0, 255)
	ipnum2 = random.randint(0, 255)
	ipnum3 = random.randint(0, 255)
	ipnum4 = random.randint(0, 255)
	ipnum1 = str(ipnum1)
	ipnum2 = str(ipnum2)
	ipnum3 = str(ipnum3)
	ipnum4 = str(ipnum4)
	ip = ipnum1 + "." + ipnum2 + "." + ipnum3 + "." + ipnum4
	if ip in openips2:
		os.system("python3 main.py")
		openips.close()
		exit()
	r = https_PoolManager.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	responsecode = r.status
	if responsecode == 429 or "429":
		timeout()
	location = r.data
	location = location.decode(encoding='UTF-8')
	if location == "":
		os.system("python3 main.py")
		openips.close()
		exit()
	print(ip)
	print(location)
	responsecode = str(responsecode)
	print('response code:' + responsecode + '\n')
	responsecode = int(responsecode)
	ip = ip + '\n'
	log(ip)
	openips.close()