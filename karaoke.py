#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smallsmilhandler
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import urllib.request as load
import json


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.etiquetas = cHandler.get_tags()

    def __str__(self):
        lista_str = ''
        for tag_attrs in self.etiquetas:
            if tag_attrs == str(tag_attrs):
                etiqueta = tag_attrs
                lista_str += etiqueta + '\t'
            else:
                for valor in tag_attrs.keys():
                    if tag_attrs[valor] != '':
                        lista_str += (valor + '=' + '"'
                                      + tag_attrs[valor] + '"' + '\t')
                lista_str = (lista_str + '\n')
        lista_str = lista_str[:-1]
        return lista_str

    def do_json(self, fich_smil, fich_json=''):
        if fich_json == '':
            fich_json = fich_smil.split('.')[0] + '.json'
        with open(fich_json, 'w') as file:
            json.dump(self.etiquetas, file, sort_keys=True, indent=4)

    def do_local(self):
        lista_dicc = [dato for dato in self.etiquetas if dato != str(dato)]
        for dicc in lista_dicc:
            if 'src' in dicc and 'http:' in dicc['src'].split('/')[0]:
                load.urlretrieve(dicc['src'], dicc['src'].split('/')[-1])
                dicc['src'] = dicc['src'].split('/')[-1]


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: python3 karaoke.py file.smil')

    karaoke = KaraokeLocal(sys.argv[1])
    print(karaoke)
    karaoke.do_json(sys.argv[1])
    karaoke.do_local()
    karaoke.do_json(sys.argv[1], 'local.json')
    print(karaoke)
