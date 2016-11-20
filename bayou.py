#!/usr/bin/env python

import cherrypy

class Bayou(object):
    def index(self):
        pass
    index.exposed = True

cherrypy.quickstart(Bayou())
