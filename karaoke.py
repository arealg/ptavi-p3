#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler




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


if __name__ == '__main__':

	parser = make_parser()
	cHandler = smallsmilhandler.SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open(sys.argv[1]))
	ordenar(cHandler.get_tags())
