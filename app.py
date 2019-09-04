#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
import os


response={}
minimo, maximo =0, 0

app = Flask(__name__)
Bootstrap(app)

@app.route('/predict', methods=['POST'])
def predict():
	import io
	import base64
	from PIL import Image
	from flask import request
	message = request.get_json(force=True)
	encoded = message['image']
	decoded = base64.b64decode(encoded)
	image = Image.open(io.BytesIO(decoded))

	#image.save('./static/uploads/mapa', format="PNG")
	import contar as c	
	minimo, maximo = c.iniciar_conteo(image)	
	response = { 
		'prediccion': { 
			'minimo': minimo,
			'maximo' : maximo,			
	  	}
	}
	return jsonify(response)


if __name__ == '__main__':
    app.run(port=6747, debug=True) 	


