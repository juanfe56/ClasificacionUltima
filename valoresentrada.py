# Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import math
from scipy.interpolate import interp1d

# 1 DATAFRAME

#valores de entrada
tamiz = pd.Series(['1"', '3/4"', '3/8"', 'No.4', 'No.10', 'No.20', 'No.40', 'No.60', 'No.100', 'No.200', 'Fondo' ])                           
diametro=pd.Series([25,     #tamiz 1"
                    19,     #tamiz 3/4"
                    9.5,    #tamiz 3/8"
                    4.75,   #tamiz No.4
                    2,      #tamiz No.10
                    0.850,  #tamiz No.20
                    0.425,  #tamiz No.40
                    0.250,  #tamiz No.60
                    0.150,  #tamiz No.100
                    0.075,  #tamiz No.200
                    None])      
#Ingresar los datos del peso retenido en cada tamiz
retenido =pd.Series([0,     #tamiz 1"
                     10,    #tamiz 3/4"
                     30,    #tamiz 3/8"
                     10,    #tamiz No.4
                     40,    #tamiz No.10
                     10,    #tamiz No.20
                     206,   #tamiz No.40
                     10,    #tamiz No.60
                     10,    #tamiz No.100
                     300,   #tamiz No.200
                     1]) #fondo
retenido.sum()

#creacion dataframe

Tabladataframe = pd.DataFrame({      
    'Tamiz':tamiz,
    'Diametro (mm)': diametro,
    'Peso Retenido(gr)' : retenido}) 
   
#Columnas del dataframe

Tabladataframe['% Retenido']=retenido*100/retenido.sum()                      
Tabladataframe['% Retenido Acumulado']=(retenido*100/retenido.sum()).cumsum()   #se guarda el dato de la suma acumulado de cada tamiz 
Tabladataframe['% Pasa']=100-(retenido*100/retenido.sum()).cumsum()            
Tabladataframe['Peso Pasa(gr)']=retenido.sum()-retenido.cumsum() 

# 2 GRAFICAR DATAFRAME

print(Tabladataframe)