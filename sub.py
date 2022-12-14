import paho.mqtt.client
import json, requests,time,threading,os
from config import config
from queue import Queue

# Global vars
q = Queue(maxsize=config.queue_size_limit)
lock = threading.Lock()

def on_message(client,userdata,message):
	global q
	obj = json.loads(message.payload)
	print(message.payload[:120])
	fname = str(obj['ts']) + '_' + str(obj['id'])
	contents = obj['data']
	try:
		fh = open(fname,'w')
		print(fh.write(contents), 'bytes written')
		fh.flush()
		fh.close()
	except :
		print("I/O error")
	lock.acquire()
	if q.full():
		q.get()
	q.put(fname)
	lock.release()
	
	# call write
	time.sleep(50)
	# yeet file once write is dones
	if os.path.exists(fname):
		os.remove(fname)

client = paho.mqtt.client.Client(client_id=config.mqtt_client_name,clean_session=False)
client.connect(host=config.mqtt_borker_ip, port=1883)
client.on_message = on_message
client.subscribe(config.mqtt_topic,2)
time.sleep(1)
client.loop_forever()
# while 1:
# 	msg = subscribe.simple("img", hostname=config.mqtt_borker_ip)
# 	obj = json.loads(msg.payload)
# 	req = requests.get(kertish_head)
# 	print(req.status_code)
# 	print(msg.payload[:100], len(msg.payload))


# POST Req with file
# import requests

# url = "http://127.0.0.1:8000/api/annotate/"

# payload={'user': '3'}
# files=[
#   ('annotations',('annotate_1564683718873.csv',open('/home/tanmay/BITS/sop/sample-data/annotate_1564683718873.csv','rb'),'text/csv'))
# ]
# headers = {
#   'Authorization': 'Bearer 97fe3c35b9a2fca01f8e9f4e16f48f9d0879b0c0178f2099cc7d1d5461a23342'
# }

# response = requests.request("POST", url, headers=headers, data=payload, files=files)

# print(response.text)
