import json

from flask import Flask, render_template, request

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
	palabras = request.args.get('ignorar', default=[], type=list[str])

	sugerencias = {}
	for palabra in oracion.split():
		if palabra not in palabras:
			problema_ortografia = revisar_ortografia(palabra)
			if not problema_ortografia:
				sugerencias[palabra] = sugerir_palabras(palabra)

	json_data= json.dumps(sugerencias)

	return json_data


if __name__ == '__main__':
	app.run(host='0.0.0.0')

