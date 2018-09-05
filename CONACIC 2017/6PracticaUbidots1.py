#!/usr/bin/python
#Bibliotecas
import time, mraa
from ubidots import ApiClient

#Se inicializa el puerto 0 analogico
a0 = mraa.Aio(0)

#Datos para la conexion a ubidots
TOKEN = ""  #API Key
VAR_ID_SENSOR1 = ""  # ID de variable

#Se intenta la conexion 6 veces
for i in range(0,5):
    try:
        print "Requesting Ubidots token"
        api = ApiClient(token=TOKEN)  #Se realiza la peticion de conexion
        break
    
    except:
        print "No internet connection, retrying..."
        time.sleep(5)
print "Conexion exitosa"

#Se inicializa variable con su ID
sensor1 = api.get_variable(VAR_ID_SENSOR1)
   
while(1):
	try:
		#Se lee el valor del sensor
	    sensor1_valor = a0.read()
	    #Se sube  el valor en la plataforma
	    sensor1_value = sensor1.save_value({'value': sensor1_valor}) 
	    #Se imprime en pantalla
	    print sensor1_valor
	    
	except:
		print "No se pudo enviar"
	time.sleep(1)