import subprocess
import json, requests,time,threading,os,shutil
from config import config
from queue import Queue


def write_to_kertish(local_name,fs_name):
    local_name_modified = "local:" + local_name
    command =["./krtfs","-t",config.kertish_ip,"cp",local_name_modified,fs_name]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode()
    print(out)

if __name__ == '__main__':
	write_to_kertish("test2.txt","/test2.txt")

def get_from_kertish(fs_name,local_name):
    local_name_modified = "local:" + local_name
    command =["./krtfs","-t",config.kertish_ip,"cp",fs_name,local_name_modified]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode()
    print(out)