# encoding: utf-8
from PIL import Image             # funciones para cargar y manipular imágenes
from predecir import predict
from flask import Flask, render_template
import os
import random




def Contar(izquierda,arriba,derecha,abajo, mapa):
  #mapa = Image.open("./static/uploads/mapa.jpg")
  mapa = mapa
  #mapa.show()  
  total_vss = 0  
  vss= [] ##array donde estan las vss etiquetadas
  x = 1


   
  while abajo < 2155:
      while derecha <= 2500:
        region = (izquierda,arriba,derecha,abajo)
        seccion = mapa.crop(region)
        
        dir='./data/vss_etiquetadas/' + str(x)
        seccion.save('./data/seccion', format="PNG")
        if predict('./data/seccion') == 1:         
          vss.append(seccion)
          total_vss = total_vss + 1 
          seccion.save(dir, format="PNG")
          x = x + 1
          #vss[total_vss-1].show()                   
        derecha = derecha + 50
        izquierda = izquierda + 50          
      arriba = arriba + 50
      abajo = abajo + 50
      derecha = 50
      izquierda = 0
  return total_vss

  
def iniciar_conteo(imagen):   
  #puntos de inicio
  izquierda=0
  arriba=0
  derecha=50
  abajo=50
  total= []
  mapa = imagen
  while arriba < 30:        
    while izquierda < 30:
      total.append(Contar(izquierda,arriba,derecha,abajo, mapa))      
      izquierda=izquierda+25
      derecha=derecha+25                
    arriba=arriba+25
    abajo=abajo+25
    izquierda=0
    derecha=50

  minimo=min(total)
  maximo=max(total)  
  print (minimo, maximo)
  

  return minimo, maximo
      
#iniciar_conteo()