#importa las bibliotecas 

#Biblioteca del LCD RGB
from upm import pyupm_jhd1313m1 as lcd
import time

#Direcciones del LCD segun el fabricante
mylcd = lcd.Jhd1313m1(0, 0x3E, 0x62) 
#Limpia display
mylcd.clear() 
#Asigna color de led al LCD
mylcd.setColor(0, 113, 197)

mylcd.setCursor(0,0)
#Se escribe cadena en el display segun la posicion del cursor
mylcd.write("Intel Edison")
#Se pone el curso en (0,0)
mylcd.setCursor(1,0)
#Se escribe cadena en el display segun la posicion del cursor
mylcd.write("LAB Innovacion")
#Espera 5 segundos y luego termina la ejecucion
time.sleep(5)