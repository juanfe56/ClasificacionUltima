import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import math
from .valoresentrada import *

# 3 CALCULO DE CU Y CC

#creacion de nueva tabla para la iteracion 
tabla_calculo = Tabladataframe.loc[0:10,["Diametro (mm)",'% Pasa']]    
calculo_d = []                                                     

#ciclo for para buscar los diamtros donde pasa el 10%, 30% y 60% del material 
for i in [10 , 30, 60]:
  #Buscar el pasa mayor y menor mas cercano al porcentaje pasa requerido (10, 30 y 60) 
  mayor = tabla_calculo[tabla_calculo['% Pasa']>=i].tail(1)   
  menor = tabla_calculo[tabla_calculo['% Pasa']<=i].head(1)  

  #Guarda los valores de pasa y de tamaño de tamiz del porcentaje inferior 
  menor_pasa = float(menor["% Pasa"])         
  menor_tamiz = float(menor["Diametro (mm)"])    
  #Guarda los valores de pasa y de tamaño de tamiz del porcentaje mayor
  mayor_pasa = float(mayor["% Pasa"])        
  mayor_tamiz = float(mayor["Diametro (mm)"])   

  #interpolacion 
  if menor_pasa == i or mayor_pasa == i:
    di = menor_tamiz
    calculo_d.append(di)
  else: 
    di = 10**(np.log10(menor_tamiz)+(i-menor_pasa)/(mayor_pasa-menor_pasa)*np.log10(mayor_tamiz/menor_tamiz))
    calculo_d.append(di)

#Resultados  
d10 = calculo_d[0]
d30 = calculo_d[1]
d60 = calculo_d[2]
cc = d30*d30/(d10*d60)    
cu = d60/d10              
print('  El coeficiente de curvatura es {} y el coeficiente de uniformidad {}'.format(round(cc,3),round(cu,3)))


# 4 VALORES DE ENTRADA

pasa_4 = Tabladataframe.loc[3,'% Pasa']
pasa_200 = Tabladataframe.loc[9,'% Pasa']

#Funcion granulometria 
def function_gran(nombre):

  #separar cuando es grava y cuando es arena el cu y el cc
  if nombre == "Grava":
    #Se clasifica en funcion de los coeficientes(uniformidad y curvatura)
    if cu > 4 and 1 <= cc <= 3:
      print("El suelo esta clasificado como GW, es decir una Grava bien gradada")  
    else:
      print("El suelo esta clasificado como GP, es decir una Grava pobremente gradada")
  else:
    if cu > 6 and 1 <= cc <= 3:
      print("El suelo esta clasificado como SW, es decir una Arena bien gradada")  
    else: 
      print("El suelo esta clasificado como SP, es decir una Arena pobremente gradada")

#Funcion granulometria y plasticidad 
def function_granulometria_y_plasticidad(nombre):
  #Valores de los ejes
  x =  np.array([0,100])
  y = np.array([0,70])
  #Solicitud de valores de LL y IP al usuario 
  ll = float(input("Escriba el Limite Liquido (LL): "))
  ip = float(input("Escriba el Indice de Plasticidad (IP): "))
  #Lineas y estilos de grafico 
  plt.xlim(0,100)
  plt.ylim(0,70)
  plt.plot(x, 0.73*(x-20), label = "linea A", color = "red")
  plt.plot(x, 0.9*(x-0.8), label = "linea U", color = "green", linestyle = "dashed")
  plt.axvline(x=50, label = "linea U", color = "b")
  plt.axhline(y=4, label = "linea CL-ML", color = "red", linestyle = "dashed", xmin=0.05, xmax=0.25)
  plt.axhline(y=7, label = "linea CL-ML", color = "red", linestyle = "dashed", xmin=0.08, xmax=0.30)
  plt.title("Carta de plasticidad",fontsize=10)
  plt.xlabel("Limite liquido (LL)",fontsize=10)
  plt.ylabel("Indice de plasticidad (IP)",fontsize=10)
    
  plt.scatter(ll, ip)
    
  plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
  plt.show()
    
  #separar cuando es grava y cuando es arena el cu y el cc
  if nombre == "Grava":
    if cu > 4 and 1 <= cc <= 3:
      if ip >  0.9*(ll-0.8):
        respuesta = " No se puede clasificar"
      elif ip < 0.9*(ll-0.8) and ip > 0.73*(ll-20):
        if ll < 50:
          if ip > 7:
            respuesta = " arcillosa"
          elif ip < 7 and ip > 4:
            respuesta = " arcillosa limosa"
          else:
            respuesta = " limosa"
        elif ll >= 50:
          respuesta = " arcillosa"
      else:
        if ll < 50:
          respuesta = " limosa"
        elif ll >= 50:
          respuesta = " limosa"
        print("El suelo esta clasificado como "+nombre + respuesta +" bien gradada")
    else:
      if ip >  0.9*(ll-0.8):
        respuesta = " No se puede clasificar"
      elif ip < 0.9*(ll-0.8) and ip > 0.73*(ll-20):
        if ll < 50:
          if ip > 7:
            respuesta = " arcillosa"
          elif ip < 7 and ip > 4:
            respuesta = " arcillosa limosa"
          else:
            respuesta = " limosa"
        elif ll >= 50:
          respuesta = " arcillosa"
      else:
        if ll < 50:
          respuesta = " limosa"
        elif ll >= 50:
          respuesta = " limosa"
      print("El suelo esta clasificado como "+nombre + respuesta +" pobremente gradada")
  else:
    if cu > 6 and 1 <= cc <= 3:
      if ip >  0.9*(ll-0.8):
        respuesta = " No se puede clasificar"
      elif ip < 0.9*(ll-0.8) and ip > 0.73*(ll-20):
        if ll < 50:
          if ip > 7:
            respuesta = " arcillosa"
          elif ip < 7 and ip > 4:
            respuesta = " arcillosa limosa"
          else:
            respuesta = " limosa"
        elif ll >= 50:
          respuesta = " arcillosa"
      else:
        if ll < 50:
          respuesta = " limosa"
        elif ll >= 50:
          respuesta = " limosa"
        print("El suelo esta clasificado como "+nombre + respuesta +" bien gradada")
    else:
      if ip >  0.9*(ll-0.8):
        respuesta = " No se puede clasificar"
      elif ip < 0.9*(ll-0.8) and ip > 0.73*(ll-20):
        if ll < 50:
          if ip > 7:
            respuesta = " arcillosa"
          elif ip < 7 and ip > 4:
            respuesta = " arcillosa limosa"
          else:
            respuesta = " limosa"
        elif ll >= 50:
          respuesta = " arcillosa"
      else:
        if ll < 50:
          respuesta = " limosa"
        elif ll >= 50:
          respuesta = " limosa"
      print("El suelo esta clasificado como "+nombre + respuesta +" pobremente gradada")

