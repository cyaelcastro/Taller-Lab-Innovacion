#importa bibliotecas 
import mraa, time

#Inicializa gpio con el puerto 0
x = mraa.Gpio(0)
n = 0
while 1:
	#Lee el valor del gpio
	if x.read():
		n = n + 1
		print "Numero de veces que ha apretado el boton: " + str(n)
	#Espera 0.1 segudos para volver a realizar la lectura
	time.sleep(.2)