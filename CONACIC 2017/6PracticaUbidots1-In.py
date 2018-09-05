#Bibliotecas
import time, mraa
#Se importa la instancia ApiClient de Ubidots
from ubidots import ApiClient

import pyupm_i2clcd as lcd
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)


#Conexion a ubidots

#Datos de la conexion
TOKEN = "" #ApiKey
VAR_ID_SENSOR1 = ""  # Booluz

#Se intenta acceder
for i in range(0,5):
    try:
        print "Conectando a Ubidots"
        api = ApiClient(token=TOKEN)
        break
        
    except:
        print "Intento fallido, volviendo a conectar"
        time.sleep(5)
print "Conexion exitosa"
a0 = mraa.Aio(0)

while(1):

    try:

        myLcd.clear()
        #Se inicializa variable con ubidots
        lecturaBool = api.get_variable(VAR_ID_SENSOR1)

        #Se tratan de obtener 1 valor de ubidots
        ultimoValor = lecturaBool.get_values(1)
       
        
        textoLectura = int(ultimoValor[0]['value'])
    
        #Se imprime en pantalla y se escribe en LCD
        print (textoLectura)
        imprimir = str(textoLectura)
        myLcd.write(imprimir)
        if textoLectura == 1:
            myLcd.setColor(255,0,0)
        else:
            myLcd.setColor(0,0,255)
    
        print "Valores recibidos correctamente"
        
    except:
        print "No se pudo recibir"
    time.sleep(1)
    