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
from joker.importer import get_class


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
        return self.config.ROUTES

    def get_handlers(self):
        handlers = [
            ('/version/?', VersionHandler),
        ]
        for route in self.get_routes():
            middleware_classes = route[1]
            result = []
            for middleware_class in middleware_classes:
                if isinstance(middleware_class, basestring):
                    result.append(get_class(middleware_class))
                else:
                    result.append(middleware_class)

            handlers.append((route[0], MiddlewareHandler, {
                'middlewares': result
            }))

        return tuple(handlers)

    def get_plugins(self):
        return [
            RedisPlugin
        ]

if __name__ == '__main__':
    main()
