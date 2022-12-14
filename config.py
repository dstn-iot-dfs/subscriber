# a file with all required config params.
import uuid

class config():
	
	mqtt_borker_ip = "localhost"
	mqtt_topic = "img"
	mqtt_port = 1883
	mqtt_client_name = str(uuid.uuid1())
	queue_size_limit = 5
	cutoff_strength = 60
	max_timeouts = 1000
	img_xmit_time = 0.5 #time after which xmit in s
	img_gen_time = 5
	kertish_ip = "10.60.38.105:4000"
