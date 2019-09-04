Para ejecutar la aplicación es necesario en un entorno virtual de python tener instaladas la librería de Flask, Tensorflow, Keras y demás librerías de Python importadas en las diferentes clases de la aplicación (revisar el codigo).

En linea de comandos active el entorno virtual en donde instaló las librerias correspondientes y después ubiquese en el directorio donde guardó la aplicación y escriba los siguientes comandos:

export FLASK_APP=flask_app.py

flask run --host=0.0.0.0

python -m SimpleHTTPServer 5000

si el hots está en uso cambielo por otro puerto. Ejemplo:

python -m SimpleHTTPServer 8080

para finalizar escriba el siguiente comando para ejecutar la aplicación:

python app.py

Una vez activo el puerto, no cierre la terminal ( o consola) y dirijase a la direccion: 
http://127.0.0.1:5000/static/predecir.html

Ahora podrá usar la aplicación.
