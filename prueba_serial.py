import psycopg2
import serial
import time
from datetime import datetime

print("Hello world")
puerto = serial.Serial("COM4",115200)

#Variables
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "postgre379"
PSQL_DB = "postgres"

#Conexion
conexion_address = """
host=%s port=%s user=%s password=%s dbname=%s
"""% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
conexion = psycopg2.connect(conexion_address)
cursoro = conexion.cursor()

#Query "2021-06-17 19:09:50-05"
#SQL = "SELECT * FROM log_tem_hum WHERE temperatura = 21.25"
# SQL = """
# INSERT INTO public.log_tem_hum (fecha_hora, temperatura, humedad) VALUES (%s, %s, %s);
# """ % ("\'" + date_time + "-05\'::timestamptz", 20.25, 80.25)
# cursoro.execute(SQL)
#Get Values
#all_values = cursoro.fetchall()
#print("Get values: ", all_values)

# cursoro.close()
# conexion.commit()
# conexion.close()

while (1):
    puerto.flushInput()
    time.sleep(1)
    recibido = puerto.readline
    puerto.flushInput()
    crecibido = str(recibido)
    print(crecibido)
    temp = crecibido[len(crecibido)-8:len(crecibido)-3]
    print(temp)

    date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(date_time)
    SQL = """
    INSERT INTO public.log_tem_hum (fecha_hora, temperatura, humedad) VALUES (%s, %s, %s);
    """ % ("\'" + date_time + "-05\'::timestamptz", temp, 79.25)
    cursoro.execute(SQL)
    conexion.commit()
    time.sleep(4)

conexion.close()
