#importa bibliotecas
#Biblioteca Sensor temperatura y humedad
from upm import pyupm_th02 as tyhupm
import time

#Se inicializa el sensor de temperatura y humedad i2c
tyh = tyhupm.TH02(bus=0, addr=64)


while True:
    humedad = tyh.getHumidity()
    temperatura = tyh.getTemperature()
    print("Humedad: "+str(humedad))
    print("Temperatura: "+str(temperatura))
    time.sleep(1)