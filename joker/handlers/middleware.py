#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from joker.middleware import Response
from joker.handlers import BaseHandler


class MiddlewareHandler(BaseHandler):
    def initialize(self, middlewares):
        self.middlewares = middlewares

    def get(self):
        response = Response()

        for middleware_cls in self.middlewares:
            middleware = middleware_cls()
            middleware.process(self.application, self, self.request, response)

        for header_name, value in response.headers.items():
            self.set_header(header_name, value)

        self.write(''.join(response.body))
