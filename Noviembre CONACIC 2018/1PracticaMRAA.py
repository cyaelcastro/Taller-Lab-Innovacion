#Se importan bibliotecas
import mraa 
import time

#Se define la interfaz analogica con el puerto
x = mraa.Aio(0)

while 1:
	#Lee el sensor en Analogico 0 cada 2 segundos
	print x.read()
	time.sleep(2)