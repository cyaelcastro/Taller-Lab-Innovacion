#RETO 2
#Junta el sensor PIROLICO, el LCD RGB I2C y BUZZER

#Bibliotecas
#Biblioteca del LCD RGB
from upm import pyupm_jhd1313m1 as lcd
#Biblioteca del sensor pirolico
from upm import pyupm_biss0001 as upmMotion
#Biblioteca del buzzer
from upm import pyupm_buzzer as upmBuzzer

import time

#Se inicializa el buzzer en el puerto 6
buzzer = upmBuzzer.Buzzer(6)
#Volumen del buzzer
buzzer.stopSound()
buzzer.setVolume(0.05)

#Se inicializa el sensor pirolico en el puerto 2
motion = upmMotion.BISS0001(2)
#Se inicializa el LCD en su direccion
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

#Operaciones de lcd
myLcd.clear()
myLcd.setColor(255,255,0)
myLcd.write("Activando")
myLcd.setCursor(0,0)
time.sleep(2)

while True:
	buzzer.stopSound()
	myLcd.clear()
	#Si detecta movimiento el sensor pirolico, suena el buzzer
	if (motion.value()):
		myLcd.setColor(255,0,0)
		myLcd.write("movimiento")
		buzzer.playSound(upmBuzzer.BUZZER_SI,200000)
	else:
		myLcd.setColor(0,255,0)
		myLcd.write("no movimiento")

	time.sleep(2)






