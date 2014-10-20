#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com


class Response(object):
    def __init__(self):
        self.headers = {}
        self.body = []
        self.status = 200

    def set_header(self, name, value):
        self.headers[name] = str(value)


class Middleware(object):
    def process(self, app, handler, request, response):
        pass
