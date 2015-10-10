#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


if len(sys.argv) == 2:
	fichero = sys.argv[1]
else:
	print('Usage: python3 karaoke.py file.smil')

def ordenar(lista):
	for valor in lista:
		if valor == str(valor):
			etiqueta = valor
			sys.stdout.write(etiqueta + '\\')
		else:
			for i in valor.keys():
				if valor[i] != '':
					sys.stdout.write(i + '=' + '"' + valor[i]+ '"' + '\\')
			sys.stdout.write('n')
			print()


if __name__ == '__main__':

	parser = make_parser()
	cHandler = smallsmilhandler.SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open('karaoke.smil'))
	ordenar(cHandler.get_tags())
