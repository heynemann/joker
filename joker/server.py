#!/usr/bin/python
# -*- coding: utf-8 -*-

# this file is part of joker.
# https://github.com/heynemann/joker

# licensed under the mit license:
# http://www.opensource.org/licenses/mit-license
# copyright (c) 2014 bernardo heynemann heynemann@gmail.com

from cow.server import Server
from cow.plugins.redis_plugin import RedisPlugin
from tornado.httpclient import AsyncHTTPClient

from joker import __version__
from joker.handlers import BaseHandler
from joker.handlers.middleware import MiddlewareHandler
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

    def get_routes(self):
        return []

    def get_handlers(self):
        handlers = [
            ('/version/?', VersionHandler),
        ]
        for route in self.get_routes():
            handlers.append((route[0], MiddlewareHandler, {
                'middlewares': route[1]
            }))

        return tuple(handlers)

    def get_plugins(self):
        return [
            RedisPlugin
        ]

if __name__ == '__main__':
    main()
