import json
import requests
from spider.weibo.utils.cookie import cookie


# 搞笑类视频
def bingo(page):
    data = json.dumps({
        "Component_Channel_Hot": {
            "next_cursor": page, "cid": 4379552642725861}
        })
    collection = wheel(data=data)
    for item in collection.get("data", {}).get("Component_Channel_Hot", {}).get("list", []):
        single = wheel(data=json.dumps({"Component_Play_Playinfo": {"oid": item["oid"]}}))
        yield {
            "media_id": item["media_id"],
            "oid": item["oid"],
            "mid": item["mid"],
            "title": item["title"],
            "cover_image": item["cover_image"],
            "url": list(single.get("data", {}).get("Component_Play_Playinfo", {}).get("urls", {}).values())[-1]
        }


def wheel(data):
    url = "https://weibo.com/tv/api/component"
    params = {
        "page": "/tv/channel/4379552642725861"
    }
    headers = {
        "Referer": "https://weibo.com/tv/channel/4379552642725861",
        "Cookie": f"SUB={cookie.sub}"
    }
    headers.update(cookie.headers)
    data = {
        "data": data
    }
    response = requests.post(url, headers=headers, params=params, data=data).json()
    if response["code"] != "100000":
        cookie.update()
    return response
