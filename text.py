import os

import hunspell

from settings import APP_STATIC

es_dic = os.path.join(APP_STATIC, 'es_ANY.dic')
es_aff = os.path.join(APP_STATIC, 'es_ANY.aff')

dic = hunspell.HunSpell(es_dic, es_aff)


def revisar_ortografia(palabra: str) -> bool:
	"""
	Funcion para revisar una palabra ortograficamente
	:param: palabra Palabra a revisar
	:return: True si esta bien la palabra
	"""
	return dic.spell(palabra)


def sugerir_palabras(palabra: str):
	"""
	Funcion para sugerir palabras
	"""
	return dic.suggest(palabra)
