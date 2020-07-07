import paho.mqtt.client as mqtt #import the client1
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	broker_address="192.168.1.184" 
	#broker_address="iot.eclipse.org" #use external broker
	client = mqtt.Client("P1") #create new instance
	client.connect("mqtt.eclipse.org", 1883, 60)
	client.publish("house/main-light","OFF")#publish
	return 'Success'
if __name__ == '__main__':
    app.run(host= '192.168.55.106', port=9000, debug=False)