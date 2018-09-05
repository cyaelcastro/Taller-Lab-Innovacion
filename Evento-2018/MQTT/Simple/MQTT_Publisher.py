# -*- coding: utf-8 -*-
#Hace un solo envio
import paho.mqtt.client as mqtt

HOST = "test.mosquitto.org"
TOPIC = "Innovacion2018/BUAP/Loquequieras"

mqttc = mqtt.Client()
mqttc.connect( HOST , 1883)

mqttc.publish( TOPIC , raw_input("Que deseas enviar?: "))