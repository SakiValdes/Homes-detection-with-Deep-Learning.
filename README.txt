Para ejecutar la aplicaci�n es necesario en un entorno virtual de python tener instaladas la librer�a de Flask, Tensorflow, Keras y dem�s librer�as de Python importadas en las diferentes clases de la aplicaci�n (revisar el codigo).

En linea de comandos active el entorno virtual en donde instal� las librerias correspondientes y despu�s ubiquese en el directorio donde guard� la aplicaci�n y escriba los siguientes comandos:

export FLASK_APP=flask_app.py

flask run --host=0.0.0.0

python -m SimpleHTTPServer 5000

si el hots est� en uso cambielo por otro puerto. Ejemplo:

python -m SimpleHTTPServer 8080

para finalizar escriba el siguiente comando para ejecutar la aplicaci�n:

python app.py

Una vez activo el puerto, no cierre la terminal ( o consola) y dirijase a la direccion: 
http://127.0.0.1:5000/static/predecir.html

Ahora podr� usar la aplicaci�n.
