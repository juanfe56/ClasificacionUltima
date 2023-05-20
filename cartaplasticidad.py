# Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import math
from scipy.interpolate import interp1d

def function_plast(nombre):

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
  plt.title("Carta de plasticidad",fontsize=20)
  plt.xlabel("Limite liquido (LL)",fontsize=10)
  plt.ylabel("Indice de plasticidad (IP)",fontsize=10)
  plt.grid(color='grey', linestyle='dotted', linewidth=1)

  plt.scatter(ll, ip)

  plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
  plt.show()
  
  #condicionales para clasificar segun la grafica
  if ip >  0.9*(ll-0.8):
    respuesta = " No se puede clasificar"
  elif ip < 0.9*(ll-0.8) and ip > 0.73*(ll-20):
    if ll < 50:
      if ip > 7:
        if nombre == "Plasticidad":
          respuesta = "Este suelo es una arcilla de baja plasticidad"
        else:
          respuesta = " arcillosa"
      elif ip < 7 and ip > 4:
        if nombre == "Plasticidad":
          respuesta = " Este suelo es una arcilla limosa"
        else:
          respuesta = " arcillosa limosa"
      else:
        if nombre == "Plasticidad":
          respuesta = "Este suelo es un limo de baja plasticidad"
        else:
          respuesta = " limosa"
    elif ll >= 50:
      if nombre == "Plasticidad":
        respuesta = "Este suelo es un limo de baja plasticidad"
      else:
        respuesta = " arcillosa"
  else:
    if ll < 50:
      if nombre == "Plasticidad":
        respuesta = "Este suelo es un limo de baja plasticidad"
      else:
        respuesta = " limosa"
    elif ll >= 50:
      if nombre == "Plasticidad":
        respuesta = "Este suelo es un limo de alta plasticidad"
      else:
        respuesta = " limosa"
  if nombre == "Plasticidad":
    print(respuesta)
  else:
    print(nombre + respuesta)