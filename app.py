import json

from flask import Flask, render_template, request,jsonify
from text import sugerir_palabras, revisar_ortografia

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/diccionario/<palabra>')
def validar(palabra):
	ortografia = revisar_ortografia(palabra)

	data = {'orto': ortografia}

	if not ortografia:
		data['sugerencias'] = sugerir_palabras(palabra)

	json_data = json.dumps(data)
	return json_data

@app.route('/diccionario/')
def validar_palabras():
	"""
	:param: oraciones: str
	"""

	oracion = request.args.get('oracion', default="", type=str)
	ignorar_palabras = request.args.getlist('ignorar')

	sugerencias = {}
	for palabra in oracion.split():
		if palabra not in ignorar_palabras:
			problema_ortografia = revisar_ortografia(palabra)
			if not problema_ortografia:
				sugerencias[palabra] = sugerir_palabras(palabra)

	json_data= json.dumps(sugerencias)

	return jsonify(sugerencias)


if __name__ == '__main__':
	app.run(host='0.0.0.0')

