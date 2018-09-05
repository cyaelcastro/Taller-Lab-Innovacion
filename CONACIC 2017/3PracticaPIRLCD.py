#importa bibliotecas
#Biblioteca LCD RGB
import pyupm_i2clcd as lcd
#Biblioteca del sensor pirolico
import pyupm_biss0001 as upm_motion
import time
#Se inicializa el sensor pirolico en el puerto 2
motion = upm_motion.BISS0001(2)
#Direccion del LCD RGB
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.clear()
myLcd.setColor(255,255,0)
myLcd.write("Activando")
time.sleep(1)
myLcd.setCursor(0,0)

while 1:

	myLcd.clear()
	if (motion.value()):
		#Cada que detecte algo el sensor pirolico 
		myLcd.setColor(180,0,0)
		myLcd.write("Movimiento")
	else:
		#Cada que no detecte algo el sensor pirolico 
		myLcd.setColor(0,180,0)
		myLcd.write("No movimiento")

	time.sleep(.5)






