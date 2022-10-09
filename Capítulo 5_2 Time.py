import time
print('Obtener la fecha y hora actual en diferentes formatos')
print('Tiempo en segundos:',time.time())
print('Fecha y hora como un texto:',time.ctime())
print('Estructura tiempo (UTC):',time.gmtime())
print('Estructura tiempo (local):',time.localtime())