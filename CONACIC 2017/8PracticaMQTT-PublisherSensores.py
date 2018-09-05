# -*- coding: utf-8 -*-
#Hace un solo envio
import paho.mqtt.client as mqtt
import mraa, time


#Realiza la conexion
mqttc = mqtt.Client()
#Servidor y puerto
mqttc.connect("test.mosquitto.org", 1883)
while 1:
	sensor = str(mraa.Aio(0).read())
	#Se publica el tema con el mensaje
	mqttc.publish("CursoFCC", sensor)
	print sensor
	time.sleep(3)
mqttc.loop(3) #timeout = 2