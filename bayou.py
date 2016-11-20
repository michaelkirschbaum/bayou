#!/usr/bin/env python

import cherrypy
import os
from deck import Deck
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

class Bayou(object):
    def index(self):
        deck = Deck()

        template = env.get_template('index.html')
        return template.render(deck=deck)
    index.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
cherrypy.quickstart(Bayou())
