from typing import ByteString
import serial
import time

print("Hello world")
puerto = serial.Serial("COM7",115200)
xpress = serial.Serial("COM4",115200)

def leer_resp():
    respuesta = puerto.read_all()
    print(respuesta)
    return respuesta

def send_AT():
    puerto.write(b'AT\r\n')
    time.sleep(1)
    if (leer_resp() == b'AT\r\n\r\nOK\r\n'):
        print("AT OK")
    else:
        print("AT salió mal")

def conf_GPS():
    puerto.write(b'AT+GPSRD=1\r\n')
    time.sleep(0.1)
    if (leer_resp() == b'AT+GPSRD=1\r\n\r\nOK\r\n'):
        print("GPSRD OK")
    else:
        print("GPSRD salió mal")

def leer_GPS():
    puerto.write(b'AT+GPS=1\r\n')
    time.sleep(0.1)
    if (leer_resp() == b'AT+GPS=1\r\n\r\nOK\r\n'):
        print("GPS ACTIVO OK")
    else:
        print("GPS ACTIVO salió mal")

    time.sleep(1)
    nmea = leer_resp()

    puerto.write(b'AT+GPS=0\r\n')
    time.sleep(0.5)
    if (leer_resp() == b'AT+GPS=0\r\n\r\nOK\r\n'):
        print("GPS INACTIVO OK")
    else:
        print("GPS INACTIVO salió mal")
    
def send_SMS(numero, mensaje):
    puerto.write(b'AT+CMGF=1\r\n')
    time.sleep(0.1)
    if (leer_resp() == b'AT+CMGF=1\r\n\r\nOK\r\n'):
        print("CMGF OK")
    else:
        print("CMGF salió mal")
    
    puerto.write(b'AT+CMGS=' + numero.encode() + b'\r\n')
    time.sleep(0.5)
    if (leer_resp() == b'AT+CMGS=' + numero.encode() + b'\r\n\r\n>'):
        print("INICIO MENSAJE OK")
    else:
        print("INICIO MENSAJE salió mal")
    
    puerto.write(mensaje.encode() + chr(26).encode())
    time.sleep(2)
    if (str(leer_resp()).startswith("+CMGS: ")):     # b'+CMGS: 0\r\n\r\nOK\r\n' 
        print("MENSAJE ENVIADO OK")
    else:
        print("MENSAJE ENVIADO salió mal")

# Secuencia
send_AT()
#conf_GPS()
#leer_GPS()

while (1):
    #puerto.close()
    #xpress.open()
    xpress.flushInput()
    time.sleep(1)
    recibido = xpress.readline()
    xpress.flushInput()
    crecibido = str(recibido)
    print(crecibido)
    temp = crecibido[len(crecibido)-8:len(crecibido)-3]
    print(temp)

    #xpress.close()
    #puerto.open()
    send_SMS("987351250", "la temperatura actual es: " + temp)
    time.sleep(4)





######################################################################

# +CIEV: "MESSAGE",1

# +CMT: "+51976197302",,"2021/06/18,23:09:33+05"
# BBVA | Estimado Cliente, tu cuenta ha sido bloqueada. Para desbloquear tu cuenta afilia tu TOKEN DIGITAL de forma segura aqui: 
# http://gg.gg/_-BBVA

######################################################################

# ^CINIT: 1, 0, 0

# ^CINIT: 2, 32, 41891

# ^STN: 37

# ^CINIT: 4, 8192, 37

# ^CINIT: 8, 2048, 3

# ^CINIT: 16, 0, 1638435

# ^CINIT: 32, 0, 0

# +CREG: 0

# +CIEV: service,  1
# +CIEV: roam, 0

# +CREG: 1

######################################################################

# ^CINIT: 1, 0, 0

# ^CINIT: 1, 0, 0

# +CREG: 0

######################################################################

# ^CINIT: 1, 0, 0

# ^CINIT: 2, 32, 41891

# ^STN: 37

# ^CINIT: 4, 8192, 37

# ^CINIT: 8, 6144, 3

# ^CINIT: 16, 0, 1638435

# ^CINIT: 32, 0, 0

# +CREG: 0

# +CIEV: service,  1
# +CIEV: roam, 0

# +CREG: 1

######################################################################

# ^CINIT: 1, 0, 0

# ^CINIT: 2, 32, 4198

# ^STN: 38

# ^CINIT: 4, 8192, 38

# ^CINIT: 8, 2048, 3

# ^CINIT: 16, 0, 1638589

# ^CINIT: 32, 0, 0

# +CREG: 0

# ^CINIT: 130, 0, 0

# SIM not inserted

# +CIEV: service,  0
# +CIEV: roam, 0

# +CREG: 3

######################################################################

# ^CINIT: 1, 0, 0

# ^CINIT: 2, 32, 4198

# ^STN: 38

# ^CINIT: 4, 8192, 38

# ^CINIT: 8, 2048, 3

# ^CINIT: 16, 0, 1638589

# ^CINIT: 32, 0, 0

# +CREG: 0

# ^CINIT: 130, 0, 0

# SIM not inserted

# +CIEV: service,  0
# +CIEV: roam, 0

# +CREG: 3

