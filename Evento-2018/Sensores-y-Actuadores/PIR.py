import time
from upm import pyupm_biss0001 as upmMotion

movimiento = upmMotion.BISS0001(2)

while(1):
    if (movimiento.value()):
        print("Movimiento detectado")
    else:
        print("No se ha detectado movimiento")
    time.sleep(1)

