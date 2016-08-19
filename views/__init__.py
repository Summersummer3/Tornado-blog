# -*- coding: utf-8 -*-
# __author__ = 'summer'

from tornado_json.requesthandlers import ViewHandler
from tornado_routes import route

@route('',name='login')
class ViewLoginHandler(ViewHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", error = None)

@route('/register',name='register')
class ViewRegisterHandler(ViewHandler):
    def get(self, *args, **kwargs):
        self.render("login.html")