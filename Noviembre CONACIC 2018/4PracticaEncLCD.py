### Se desea cambiar el color del display usando boton, encoder
#Cambia de color rojo a color amarillo utilizando el encoder

#Biblioteca LCD RGB
import pyupm_i2clcd as lcd
#Biblioteca Encoder
import pyupm_rotaryencoder as myencoder
import time
#Se inicializa el encoder en el puerto 4 y 5
encoder = myencoder.RotaryEncoder(4,5)

#Inicializan los colores
c1 = 0
c2 = 0
c0 = 255

#Direccion del LCD RGB
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
#Operaciones del LCD RGB
mylcd.clear()
mylcd.setColor(c0, c1, c2)
mylcd.setCursor(0,0)
mylcd.write("Encoder y LCD")

valorencoder = 0
aux = 1
while 1:
	valorencoder = abs(encoder.position())
	#Si el valor del encoder rebasa 255 vuelve a 0
	if valorencoder > 255:
		valorencoder = valorencoder - 255
	c1 = valorencoder
	#Se imprime en pantalla el valor de los datos del LED RGB
	print str(c0)+ " "+ str(c1) + " " + str(c2)
	#Se asigna el color al LED RGB
	mylcd.setColor(c0,valorencoder,c2)
	#Espera 0.5 antes de continuar
	time.sleep(0.5)
