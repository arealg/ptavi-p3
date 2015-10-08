#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

	def __init__(self):

		self.rl = {'width': '','height':'','background-color': ''}

		self.reg = {'id': '', 'top': '', 'bottom': '', 'left': '',
					'right': '' }
		self.img = {'src': '','region':'', 'begin': '','dur':''}

		self.aud = {'src': '', 'begin':'', 'dur': ''}

		self.text = {'src':'','region':''}

	# def get_tags(name,lista):
	# 	etiquetas = []
	# 	if len(etiqueta) == len(0):
	# 		etiquetas.append(name)
	# 	elif name not in etiquetas:
	# 		etiqueta.append(name)
	# 	return etiquetas + lista


	def startElement(self, name, attrs):
		etiqueta = {'root-layout': self.rl,'region':self.reg,
		            'img': self.img,
					'audio': self.aud,
					'textstream': self.text}

		if name in etiqueta:
			lista = etiqueta[name]
			for i in lista:
				valor = attrs.get(i,'')
				lista[i] = valor

			print(lista)


if __name__ == '__main__':

	parser = make_parser()
	cHandler = SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open('karaoke.smil'))
