# -*- coding: utf-8 -*-
# __author__ = 'summer'

import tornado.web
import bcrypt
import markdown
import re
from tornado import gen
from tornado_json.requesthandlers import APIHandler, ViewHandler
from tornado_json import schema


class LoginHandler(APIHandler):
    @schema.validate(
        input_schema={
            "type":"object",
            "properties":{
                "username":{"type":"string"},
                "password":{"type":"string"}
            }
        },
        input_example={
            "title": "abc",
            "body": "12345"
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            }
        },
        output_example={
            "message": "login success"
        },
    )
    def post(self):
        return {
            "message": "{} login success.".format(self.body["username"])
        }





