#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import urllib.request



if len(sys.argv) != 2:
	print('Usage: python3 karaoke.py file.smil')

def ordenar(lista):
	for valor in lista:
		if valor == str(valor):
			etiqueta = valor
			print(etiqueta + '\\',end='')
		else:
			for i in valor.keys():
				if valor[i] != '':
					print(i + '=' + '"' + valor[i]+ '"' + '\\',end='')
			print('n',end='')
			print()

def descargar(lista):
	for dicc in lista:
		if dicc != str(dicc) :
			for i in dicc:
				if i == 'src':
					u = dicc[i].split('http://www.content-networking.com/smil/')
					if u[0] == '':
						urllib.request.urlretrieve(dicc[i],u[1])




if __name__ == '__main__':

	parser = make_parser()
	cHandler = smallsmilhandler.SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open(sys.argv[1]))
	# ordenar(cHandler.get_tags())
	descargar(cHandler.get_tags())
