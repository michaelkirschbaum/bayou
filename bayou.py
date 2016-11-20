#!/usr/bin/env python

import cherrypy
import os

class Bayou(object):
    def index(self):
        pass
    index.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
cherrypy.quickstart(Bayou())
