# -*- coding: utf-8 -*-
#Hace un solo envio
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883)

mqttc.publish("CURSOEdison", "Hola mundo")
mqttc.loop(3) #timeout = 2s