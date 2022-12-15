import subprocess
import json, requests,time,threading,os,shutil
from config import config
from queue import Queue
import datetime

def write_to_kertish(local_name,fs_name):
	local_name_modified = "local:" + local_name
	command =["./krtfs","-t",config.kertish_ip,"cp",local_name_modified,fs_name]
	p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out = p.stdout.read().decode()
	print(out)
	if(out.rfind('ok') > 0):
		return 'ok'
	else: 
		return 'fail'

def get_from_kertish(fs_name,local_name):
	local_name_modified = "local:" + local_name
	command =["./krtfs","-t",config.kertish_ip,"cp",fs_name,local_name_modified]
	p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out = p.stdout.read().decode()
	print(out)

def benchmark_write(fname):
	start = datetime.datetime.now()
	status = write_to_kertish(fname,fname)
	delta = datetime.datetime.now() - start
	with open('log','a') as log:
		log.write(fname+' '+str(delta) + ' ' + status + '\n')
	print(delta)

if __name__ == '__main__':
	fname = input('Enter a filename to test: ')
	benchmark_write(fname=fname)