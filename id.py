import paho.mqtt.client as mqtt #import the client1
from flask import Flask,request
from flask_ngrok import run_with_ngrok
import time
app = Flask(__name__)
#run_with_ngrok(app)
broker_url = "127.0.0.1"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code ")



client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_url, broker_port)



@app.route('/',methods=["POST"])
def hello_world():
	print("working")
	request_data= request.json
	print(request_data["topic"])
	def on_message(client, userdata, message):
   		print("Message Recieved: "+message.payload.decode())
	   	return "sucesss"
	client.on_message = on_message
	client.subscribe(request_data["topic"], qos=1)
	#broker_address="192.168.1.184" 
	#broker_address="iot.eclipse.org" #use external broker
	client.loop_start()
	client.publish(topic=request_data["topic"], payload=request_data["paylaod"], qos=1, retain=False)
	#time.sleep(4)
	#client.loop_forever()
	return "post" 


if __name__ == '__main__':
    app.run()
