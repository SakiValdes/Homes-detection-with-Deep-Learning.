# encoding: utf-8
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import tensorflow as tf


global graph,model
tf.keras.backend.clear_session()
graph = tf.get_default_graph()
with graph.as_default():

  longitud, altura = 35, 35
  modelo = './modelo/modelo1.h5'
  pesos_modelo = './modelo/pesos1.h5'
  cnn = load_model(modelo)
  cnn.load_weights(pesos_modelo)


  def predict(file):
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x) ##[1,0,0]
    resultado = array[0]
    respuesta = np.argmax(resultado)#indice del arreglo: valor con más peso: 
    if respuesta == 0:
      #print("lote")
      return 0
    elif respuesta == 1:
      #print("vss")
      return 1
   



    
