    #!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        rl = {'width': '', 'height': '', 'background-color': ''}
        reg = {'id': '', 'top': '', 'bottom': '', 'left': '',
               'right': ''}
        img = {'src': '', 'region': '', 'begin': '', 'dur': ''}
        aud = {'src': '', 'begin': '', 'dur': ''}
        text = {'src': '', 'region': ''}
        self.etiqueta = {'root-layout': rl, 'region': reg,
                         'img': img, 'audio': aud,
                         'textstream': text}
        self.l = []

    def get_tags(self):
        return self.l

    def startElement(self, name, attrs):
        if name in self.etiqueta:
            lista = {i: attrs.get(i, '') for i in self.etiqueta[name]}
            self.l.append(name)
            self.l.append(lista)
