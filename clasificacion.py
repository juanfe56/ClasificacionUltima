# Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import math
from scipy.interpolate import interp1d
from .granulometria import *
from .cartaplasticidad import *


# 6 CLASIFICACION
if pasa_200 < 50:
  print("Vamos a clasificar un suelo grueso")
  #grafica
  plt.figure(figsize=(14,4))
  plt.title("",fontsize=10)
  plt.xlabel('Diametro(mm)')               #nombre eje x
  plt.ylabel('Porcentaje pasa(%)')         #nombre eje y 
  plt.title('Curva granulometrica')        #titulo grafica 
  plt.legend()
  plt.xscale("log")                        #escala logaritmica 
  plt.xlim(0.075,25)                       #limites grafica 
  plt.ylim(0,100)
  plt.grid(color='k',lw='0.1',ls='-')
  plt.plot(Tabladataframe['Diametro (mm)'],Tabladataframe['% Pasa'],linestyle='-',marker='o',color='k',fillstyle='none',label='Data') #datos a graficar 
  f=interp1d(Tabladataframe['% Pasa'],Tabladataframe['Diametro (mm)'])

  ax1=plt.gca()
  ax1.invert_xaxis()

  ax2=ax1.twiny()#
  ax2.invert_xaxis()
  ax2.set_xscale('log')
  ax2.set_xticks(Tabladataframe['Diametro (mm)'])
  ax2.set_xticklabels(Tabladataframe['Tamiz'],rotation=90,fontsize=8)#nombre los tamices

  #graficar puntos D10, D30, D60 
  x1_formatted = '{:.2f}'.format(d60)
  x2_formatted = '{:.2f}'.format(d30)
  x3_formatted = '{:.2f}'.format(d10)
  plt.scatter(d10, 10, marker='s', s=50, color='k', label='D60='+x3_formatted)
  plt.scatter(d30, 30, marker='D', s=50, color='k', label='D30='+x2_formatted)
  plt.scatter(d60, 60, marker='x', s=50, color='k', label='D10='+x1_formatted)

  #lineas de tamiz
  L_No34 = ([19,19]) #tamaño de tamiz segun corresponda
  L_No38 = ([9.5,9.5])
  L_No4 = ([4.75,4.75])
  L_No10 = ([2,2]) 
  L_No20 = ([0.85,0.85]) 
  L_No40 = ([0.425,0.425]) 
  L_No60 = ([0.250,0.250])
  L_No140 = ([0.150,0.150])  
  L_rango = ([0,100])

  #para mostrar las lineas
  plt.plot(L_No34, L_rango, color='black', lw='0.8', ls='--') #color negro y tipo de linea 
  plt.plot(L_No38, L_rango, color='black', lw='0.8', ls='--')
  plt.plot(L_No4, L_rango, color='black', lw='0.8', ls='--')
  plt.plot(L_No10, L_rango, color='black', lw='0.8', ls='--')
  plt.plot(L_No20, L_rango, color='black', lw='0.8', ls='--') 
  plt.plot(L_No40, L_rango, color='black', lw='0.8', ls='--')
  plt.plot(L_No60, L_rango, color='black', lw='0.8', ls='--')
  plt.plot(L_No140, L_rango, color='black', lw='0.8', ls='--')

  #para agregar textos 
  plt.text(19, 2, 'Grava(Gruesa)', fontsize=8, rotation=90) #Rotar 90 grados y tamaño de texto 
  plt.text(4.75, 2, 'Grava(Fina)', fontsize=8, rotation=90)
  plt.text(1.95, 2, 'Arena(Gruesa)', fontsize=8, rotation=90)
  plt.text(0.415, 2, 'Arena(Mediana)', fontsize=8, rotation=90)
  plt.text(0.075, 2, 'Arena(Fina)', fontsize=8, rotation=90) 

  #Lineas de la grilla
  x_values = [24, 15, 5, 4, 3, 2, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08] #valores en x donde poner lineas 
  for x in x_values:
    plt.axvline(x=x, color='grey', ls='-', lw='0.3')  #parametros lineas 

  plt.show()

  if pasa_4 < 50:
    print("Es una grava")
  
    if pasa_200 >= 12:
      function_plast("Grava")
    elif 5 <= pasa_200 < 12:
      function_granulometria_y_plasticidad("Grava")
    else:
      function_gran("Grava")

  else:
    print("Es una arena")
  
    if pasa_200 >= 12:
      function_plast("Arena")
    elif 5 <= pasa_200 < 12:
      function_granulometria_y_plasticidad("Arena")
    else:
      function_gran("Arena")

else:
  function_plast("Plasticidad")

