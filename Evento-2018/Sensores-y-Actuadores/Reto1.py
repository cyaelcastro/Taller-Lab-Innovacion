#Reto 1
#Trabajar con LCD I2C y TH02


#importa bibliotecas
#Biblioteca Sensor temperatura y humedad
import pyupm_th02 as tyhupm
#Biblioteca del LCD RGB
import pyupm_i2clcd as lcd 
import time

#Se inicializa el sensor pirolico en el puerto 2
tyh = tyhupm.TH02(bus=0, addr=64)
#Direcciones del LCD segun el fabricante
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62) 
#Limpia display
mylcd.clear() 
#Asigna color de led al LCD
mylcd.setColor(0, 113, 197)

while True:
    humedad = tyh.getHumidity()
    temperatura = tyh.getTemperature()
    #Se pone el curso en (0,0)
    mylcd.setCursor(0,0)
    mylcd.write("T: "+str(temperatura))
    mylcd.setCursor(1,0)
    mylcd.write("H: "+str(humedad))
    time.sleep(2)

