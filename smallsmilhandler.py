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

		self.etiqueta = {'root-layout': self.rl,'region':self.reg,
				    'img': self.img,
					'audio': self.aud,
					'textstream': self.text}
		self.l = []


	def get_tags(self):
		for i in self.etiqueta:
			self.l.append(i)
			self.l.append(self.etiqueta[i])
		print(self.l)


	def startElement(self, name, attrs):


		# print(self.l)
		# if name == 'root-layout':
		# 	for i in self.rl:
		# 		valor = attrs.get(i,'')
				# self.rl[i] = valor
			# self.l.append(self.rl)
			# print(self.rl)
			# self.l.append(dic)
		# if name == 'region':
		# 	for i in self.reg:
		# 		valor = attrs.get(i,'')
		# 		self.reg[i] = valor
		# 	put_list(self.reg)
		# if name == 'audio':
		# 	for i in self.aud:
		# 		valor = attrs.get(i,'')
		# 		self.aud[i] = valor
		# 	self.l.append(self.aud)
		# 	print(self.l)




			# self.l.append(dic)

		if name in self.etiqueta:
			lista = self.etiqueta[name]
			for i in lista:
				valor = attrs.get(i,'')
				lista[i] = valor



if __name__ == '__main__':

	parser = make_parser()
	cHandler = SmallSMILHandler()
	parser.setContentHandler(cHandler)
	parser.parse(open('karaoke.smil'))
	cHandler.get_tags()
