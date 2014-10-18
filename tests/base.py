#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from cow.testing import CowTestCase
from tornado.httpclient import AsyncHTTPClient

from joker.config import Config
from joker.server import JokerServer


class ApiTestCase(CowTestCase):
    def get_config(self):
        return dict(
            REDISHOST='localhost',
            REDISPORT=4448
        )

    def get_server(self):
        cfg = Config(**self.get_config())
        self.server = JokerServer(config=cfg)
        return self.server

    def get_app(self):
        app = super(ApiTestCase, self).get_app()
        app.http_client = AsyncHTTPClient(self.io_loop)
        return app
