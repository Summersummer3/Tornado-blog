# -*- coding: utf-8 -*-
# __author__ = 'summer'


from tornado_json.requesthandlers import APIHandler, ViewHandler
from tornado_json import schema,exceptions


class LoginHandler(APIHandler):
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "username": {"type":"string"},
                "password": {"type":"string"},
            }
        },
        input_example={
            "username": "abc",
            "password": "12345"
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
            }
        },
        output_example={
            "message": "login success"
        },
    )
    def post(self):
        res = self.db_conn[self.settings["collection"]].find_one({"username": self.body["username"],
                                                                  "password": self.body["password"]})
        if res is None:
            exceptions.api_assert(False, 400, "not such user")
        else:
            message = "{} login success.".format(self.body["username"])
            return {
                "message": message
            }

class RegisterHandler(APIHandler):
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "username": {"type":"string"},
                "password": {"type":"string"},
            }
        },
        input_example={
            "username": "abc",
            "password": "12345"
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
            }
        },
        output_example={
            "message": "register success"
        },
    )
    def post(self):
        self.db_conn[self.settings["collection"]].insert(self.body)
        return {
            "message": "{} register success.".format(self.body["username"])
        }


