#!/usr/bin/env python

import cherrypy
import os
from jinja2 import Environment, FileSystemLoader
from deck import Deck

env = Environment(loader=FileSystemLoader('templates'))

class Bayou(object):
    deck = Deck()

    def index(self):
        template = env.get_template('index.html')
        return template.render()
    index.exposed = True

    # return name of card
    def draw(self):
        try:
            card = self.deck.draw()
        except IndexError:
            return ""
        else:
            if isinstance(card.number, int) and card.suit is not None:
                return str(card.number) + " of " + card.suit
            elif card.suit is not None:
                return card.number + " of " + card.suit
            else:
                return card.number
    draw.exposed = True

    def shuffle(self):
        self.deck.shuffle()
    shuffle.exposed = True

    def new(self):
        self.deck = Deck()
    new.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
cherrypy.quickstart(Bayou())
