# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from upm import pyupm_jhd1313m1 as lcd
from upm import pyupm_buzzer as upmBuzzer

mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
mylcd.clear()
mylcd.setColor(0, 150, 255)
mylcd.setCursor(0,0)

HOST = "test.mosquitto.org"
TOPIC = "Innovacion2018/BUAP/Loquequieras"


def on_connect(client, userdata, flags, rc):
	print("Conectado con resultado: "+str(rc))
	client.subscribe(TOPIC)


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

client.connect(HOST, 1883, 60)
client.loop_forever()