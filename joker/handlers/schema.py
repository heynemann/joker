#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

import logging

from tornado.web import asynchronous
from tornado.gen import coroutine
from jsonschema import Draft4Validator
from jsonschema.exceptions import SchemaError
from ujson import loads

from joker.handlers import BaseHandler


class SchemaHandler(BaseHandler):

    @asynchronous
    @coroutine
    def put(self):
        body = self.request.body
        try:
            obj = loads(body)
        except Exception as err:
            self.send_error(400, err)
            self.finish()
            return

        try:
            Draft4Validator.check_schema(obj)
        except SchemaError as err:
            self.write('could not create specified schema')
            self.set_status(400)
            logging.error(err)
            self.finish()
            return

        self.write('OK')
        self.finish()
