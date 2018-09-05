#Biblioteca del encoder
import pyupm_rotaryencoder as encoder
import time
#Inicializacion del encoder
ejemploEncoder = encoder.RotaryEncoder(4, 5)
while 1:
	print str(ejemploEncoder.position())
	time.sleep(0.5)