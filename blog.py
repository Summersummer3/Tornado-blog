#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import concurrent.futures
import MySQLdb
import os.path
import subprocess
import pymongo
import torndb
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from tornado_json.routes import get_routes, get_module_routes, gen_submodule_names
from tornado_json.application import Application
import sys
import tornado_routes
sys.path.append("../../")


define("port", default=8887, help="run on the given port", type=int)
define("mongo_host", default="localhost", help="blog mongodb host")
define("mongo_port", default=27017, help="blog mongodb port")
define("mongo_database", default="summer", help="blog database")


# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)
URL_PREFIX = ''



def main():
    import handlers
    routes = get_routes(handlers)
    for url in tornado_routes.make_handlers("", (r'/', tornado_routes.include('views'))):
        if isinstance(url, tornado.web.URLSpec):
            if url.name == "login":
                routes.append((r"/", url.handler_class))

    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes],
        indent=2)
    )

    settings = dict(
        blog_title=u"Summer Tornado Blog",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        ui_modules={"Entry": EntryModule},
        xsrf_cookies=False,
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url="/auth/login",
        debug=True,
        collection="blog",
    )

    # Have one global connection to the blog DB across all handlers
    client = pymongo.MongoClient(options.mongo_host, options.mongo_port)
    db = client[options.mongo_database]

    application = Application(routes, db_conn=db, generate_docs=True, settings=settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

class EntryModule(tornado.web.UIModule):
    def render(self, entry):
        return self.render_string("modules/entry.html", entry=entry)

if __name__ == "__main__":
    main()
