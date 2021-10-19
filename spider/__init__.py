from importlib import import_module
from spider.const import PLATFORM_TYPE


class Spider(object):
    def __init__(self, platform, t):
        path = f"spider.{platform}.libs.{PLATFORM_TYPE[platform][t]}"
        self.spider = import_module(path)

    def bingo(self, **kwargs):
        return self.spider.bingo(**kwargs)

