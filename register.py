#-*- coding: utf-8 -*-
class Application(object):
    PLUGINS = dict()

    @classmethod
    def register(cls, use="None"):
        def wrapper(app):
            cls.PLUGINS.update({app.__name__: use})
            return app

        return wrapper