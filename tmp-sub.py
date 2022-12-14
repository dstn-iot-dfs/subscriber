import paho.mqtt.subscribe as subscribe
import json, requests
from config import config

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
