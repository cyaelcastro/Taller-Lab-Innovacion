# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

TOPIC = "Innovacion2018/BUAP/Loquequieras"
HOST = "test.mosquitto.org"


def on_connect(client, userdata, flags, rc):
	print("Conectado con codigo: "+str(rc))
	client.subscribe(TOPIC)

def on_message(client, userdata, msg):
	print "Topic: "+ msg.topic+"\nMensaje: "+str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect( HOST , 1883)

client.loop_forever()