import os
import json


class Config(object):
    __instance = None

    def __new__(cls):
        if cls.__instance:
            return cls.__instance
        return super().__new__(cls)

    def __init__(self):
        self.__path = os.path.join(os.path.dirname(__file__), "config.json")
        self.config = json.load(open(self.__path))
        Config.__instance = self

    def get(self, key):
        return self.config.get(key, "")

    def set(self, **kwargs):
        self.config.update(kwargs)

    def save(self, **kwargs):
        self.config.update(kwargs)
        json.dump(self.config, open(self.__path, "w"), indent=4)
