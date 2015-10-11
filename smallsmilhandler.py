#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys




class SmallSMILHandler(ContentHandler):

	def __init__(self):

		self.rl = {'width': '','height':'','background-color': ''}
		self.reg = {'id': '', 'top': '', 'bottom': '', 'left': '',
					'right': '' }
		self.img = {'src': '','region':'', 'begin': '','dur':''}
		self.aud = {'src': '', 'begin':'', 'dur': ''}
		self.text = {'src':'','region':''}
		self.etiqueta = {'root-layout': self.rl,'region':self.reg,
				    'img': self.img,
					'audio': self.aud,
					'textstream': self.text}
		self.l = []


	def get_tags(self):
		return self.l


	def startElement(self, name, attrs):

		if name in self.etiqueta:
			lista = {}
			for i in self.etiqueta[name]:
				valor = attrs.get(i,'')
				lista[i] = valor
			self.l.append(name)
			self.l.append(lista)

if __name__ == '__main__':

	parser = make_parser()
	cHandler = SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open('karaoke.smil'))
	cHandler.get_tags()
