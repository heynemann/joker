#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of joker.
# https://github.com/heynemann/joker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Bernardo Heynemann heynemann@gmail.com

from cow.server import Server
from cow.plugins.redis_plugin import RedisPlugin
from tornado.httpclient import AsyncHTTPClient

from joker import __version__
from joker.handlers import BaseHandler
from joker.handlers.schema import SchemaHandler
from joker.config import Config


def main():
    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
    JokerServer.run()


class VersionHandler(BaseHandler):
    def get(self):
        self.write(__version__)


class JokerServer(Server):
    def get_config(self):
        return Config

    def get_handlers(self):
        handlers = [
            ('/version/?', VersionHandler),
            ('/schema/?', SchemaHandler),
        ]

        return tuple(handlers)

    def get_plugins(self):
        return [
            RedisPlugin
        ]

if __name__ == '__main__':
    main()
