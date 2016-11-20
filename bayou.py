#!/usr/bin/env python

import cherrypy

class Bayou(object):
    def index(self):
        pass
    index.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.quickstart(Bayou())
