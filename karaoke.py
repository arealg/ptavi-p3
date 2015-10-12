#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import urllib.request


class KaraokeLocal():

	def __init__(self, fichero):
		parser = make_parser()
		cHandler = smallsmilhandler.SmallSMILHandler()
		parser.setContentHandler(cHandler)
		parser.parse(open(fichero))
		self.etiquetas = cHandler.get_tags()


	def __str__(self):
		a = ''
		for valor in self.etiquetas:
			if valor == str(valor):
				etiqueta = valor
				a += etiqueta + '\t'
			else:
				for i in valor.keys():
					if valor[i] != '':
						a += i + '=' + '"' + valor[i]+ '"' + '\t'
				a = a + '\n'
		a = a[:-1]
		return a


	def do_local(self):
		for dicc in self.etiquetas:
			if dicc != str(dicc):
				for i in dicc:
					u = dicc[i].split('/')
					if i == 'src' and u[0] == 'http:':
						urllib.request.urlretrieve(dicc[i],u[-1])
						dicc[i] = u[-1]


if __name__ == '__main__':

	if len(sys.argv) != 2:
		sys.exit('Usage: python3 karaoke.py file.smil')

	karaoke = KaraokeLocal(sys.argv[1])
	elementos = karaoke.etiquetas
	print(karaoke.__str__())
	karaoke.do_local()
	print(karaoke.__str__())
