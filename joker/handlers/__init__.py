#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from ujson import dumps
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    @property
    def config(self):
        return self.application.config

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json")
        self.write(dumps(obj))

    @property
    def redis(self):
        return self.application.redis
