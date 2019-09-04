import keras
import tensorflow as tf
import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator #para preprocesar las imagenes
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential #para hacer CNN secuenciales
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from tensorflow.python.keras import applications #modelos de entrenamiento
from sklearn.externals import joblib
from keras.callbacks import TensorBoard 
import time


K.clear_session()

data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

epocas=10
longitud, altura = 224, 224
batch_size = 32 #numero de imagenes a procesar en cada paso
pasos_entrenamiento = 10 #numero de veces que se procesa la informacion en cada una de las epocas
pasos_validacion = 10
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 2
lr = 0.002
NAME = "Adamax{}".format(time.time())

"""
callbacks fit_generator()
"""
detener = tf.keras.callbacks.EarlyStopping(monitor='val_acc', patience=epocas, mode='max')
tensorboard = tf.keras.callbacks.TensorBoard(log_dir='./graphs9/{}'.format(NAME) )



#preprocesamiento
entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,    
    horizontal_flip=True)

validacion_datagen = ImageDataGenerator(rescale=1. / 255)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

validacion_generador = validacion_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

#ajuste modelo vgg16
def modelo():	
    vgg=applications.vgg16.VGG16()
    cnn=Sequential()    
    for capa in vgg.layers:
    	cnn.add(capa)
    cnn.layers.pop()
    for layer in cnn.layers:    	
    	layer.trainable=False
    cnn.add(Dense(clases,activation='softmax'))
    
    return cnn


cnn=modelo()


cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.Adamax(lr=lr),
            metrics=['accuracy'])

#entrenamiento
cnn.fit_generator(
    entrenamiento_generador,
    steps_per_epoch=pasos_entrenamiento,
    epochs=epocas,
    validation_data=validacion_generador,
    validation_steps=pasos_validacion,
    callbacks=[tensorboard, detener])


target_dir = './modelo_cnn/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
cnn.save('./modelo_cnn/modelo2.h5')
cnn.save_weights('./modelo_cnn/pesos2.h5')


