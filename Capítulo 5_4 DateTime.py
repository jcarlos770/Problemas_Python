import datetime
print(40*'-')
print('Información con datetime.date')
hoy=datetime.date.today()
print(hoy)
print(hoy.weekday())
print(hoy.day)
print(40*'-')
print('Información con datetime.datetime')
ahora=datetime.datetime.today()
print(ahora)
print(ahora.hour)
print(ahora.minute)