import json

from flask import Flask, render_template

from text import sugerir_palabras, revisar_ortografia

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/dic/<palabra>')
def validar(palabra):
	ortografia = revisar_ortografia(palabra)

	data = {'orto': ortografia}

	if not ortografia:
		data['sugerencias'] = sugerir_palabras(palabra)

	json_data = json.dumps(data)
	return json_data


if __name__ == '__main__':
	app.run(host='0.0.0.0')

