#!/usr/bin/env python

import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
from deck import Deck

env = Environment(loader=FileSystemLoader('templates'))

deck = Deck()

class Bayou(object):
    def index(self):
        template = env.get_template('index.html')
        return template.render()
    index.exposed = True

    def draw(self):
        return deck.draw()
    draw.exposed = True

    def shuffle(self):
        pass
    shuffle.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
cherrypy.quickstart(Bayou())
