import os
import requests
from publisher.config.index import config
from publisher.libs.video import confirm


def create(meta):
    info = confirm(meta["file"])
    url = "https://media.douyin.com/web/api/media/aweme/create/"
    headers = {
        "Cookie": config["Cookie"]
    }
    data = {
        "video_id": info["vid"],
        "poster": info["oid"],
        "poster_delay": meta["delay"],
        "text": meta["text"],
        "text_extra": [{"start": 0, "end": 3, "user_id": "", "type": 1, "hashtag_name": "音乐"}],
        "mentions": [],
        "visibility_type": 0,
        "third_text": "",
        "download": 0,
        "upload_source": 1,
        "is_preview": 0
    }
    response = requests.post(url, headers=headers, data=data).json()
    if response["status_code"] == 0:
        print("---上传成功---")
    return response


if __name__ == '__main__':
    meta = {
        "file": os.path.join(os.path.abspath("../../"), "example/1.mp4"),
        "delay": 0,
        "text": "菜鸡彬无敌"
    }
    response = create(meta)
