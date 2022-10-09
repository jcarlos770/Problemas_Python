import csv
from pylab import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
"""from google.colab import auth"""
from oauth2client.client import GoogleCredentials
"""from google.colab import files""" 
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
# Importar librerías para los cálculos.
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

#descargar el archivo de Google Drive
downloaded = drive.CreateFile({'id':"1STuungS16RJKf7nsrMB02CeiTVp2Q4fZ"})   # reemplace la id con la id del archivo al que desea acceder
downloaded.GetContentFile('DATA.TXT')        # reemplace el nombre del archivo con su archivo
#Leer los datos del archivo csv
dataraw=pd.read_csv("DATA.TXT", header=None, delimiter=",",index_col=False) #Sin encabezado,delimitado por comas, no tiene columna indice 

data1= dataraw.fillna(method='bfill', limit=1)
data= data1.fillna(method='pad', limit=1)
Humidity=data.iloc[:,3]
Day=data.iloc[1,0]
Temperature=data.iloc[:,2]
Time=data.iloc[:,1]
MHZ19B_ppm_CO2=data.iloc[:,5:22]
T_6703_ppm_CO2=data.iloc[:,25:42]
print (Day)
print (data)
#print (ppm1)
ig = plt.figure(dpi=200, figsize=(300,20))
plt.plot(Time,Temperature, c='red')
plt.plot(Time,Humidity, c='blue')
plt.plot(Time,MHZ19B_ppm_CO2, c='orange')
plt.plot(Time,T_6703_ppm_CO2, c='green')
# Rotar la etiqueta de el eje x.
plt.xticks(Time,rotation='vertical')
plt.ylabel("Factor")
plt.xlabel("Time")
plt.legend(("Temperature","Humidity","MHZ19B_ppm_CO2", "T_6703_ppm_CO2"),prop = {'size': 10}, loc='center right',shadow=True, fancybox=True)

#Descargar archivo de la gráfica
plt.savefig("abc.png")
files.download('abc.png')

ag = plt.figure(dpi=200, figsize=(300,20))
plt.plot(Time,Temperature, c='red')
plt.plot(Time,Humidity, c='blue')
# Rotar la etiqueta de el eje x.
plt.xticks(Time,rotation='vertical')
plt.ylabel("Factor")
plt.xlabel("Time")
legend(('Temperature', 'Humidity'),prop = {'size': 10}, loc='center right', shadow=True, fancybox=True)

#Descargar archivo de la gráfica
plt.savefig("abc1.png")
files.download('abc1.png')


