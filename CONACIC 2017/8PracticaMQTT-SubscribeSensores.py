# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import pyupm_i2clcd as lcd
import pyupm_buzzer

mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
mylcd.clear()
mylcd.setColor(0, 150, 255)
mylcd.setCursor(0,0)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
	client.subscribe("CursoFCC")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	mylcd.clear()
	mensaje = str(msg.payload)
	print "Topic: "+ msg.topic+"\nMessage: "+ mensaje
	
	if int(mensaje) > 400:
		mylcd.setColor(255,0,0)
	else:
		mylcd.setColor(0,0,255)
	
	
	mylcd.write(mensaje)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()