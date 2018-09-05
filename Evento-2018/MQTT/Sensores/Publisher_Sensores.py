# -*- coding: utf-8 -*-
#Hace un solo envio
import paho.mqtt.client as mqtt
import mraa, time
 
HOST = "test.mosquitto.org"
TOPIC = "Innovacion2018/BUAP/Loquequieras"

#Realiza la conexion
mqttc = mqtt.Client()
#Servidor y puerto
mqttc.connect( HOST , 1883)
while True:
	sensor = str(mraa.Aio(0).read())
	#Se publica el tema con el mensaje
	mqttc.publish( TOPIC , sensor)
	print sensor
	time.sleep(2)