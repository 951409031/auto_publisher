from publisher.libs.aweme import create


class Publisher(object):
    def __init__(self):
        self.meta = {}

    def update_meta(self, **kwargs):
        self.meta.update(kwargs)

    def create_meta(self):
        return create(self.meta)

