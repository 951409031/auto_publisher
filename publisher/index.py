import os
from publisher.libs.aweme import create


if __name__ == '__main__':
    meta = {
            "file": os.path.join(os.path.dirname(__file__), "example/1.mp4"),
            "delay": 0,
            "text": "菜鸡彬无敌"
        }
    response = create(meta)

