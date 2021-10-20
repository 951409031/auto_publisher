import json
import requests
from config.index import Config
from spider.weibo.utils.cookie import cookie


# 搞笑类视频
def bingo(page=1):
    config = Config()
    for num in range(page):
        data = json.dumps({
            "Component_Channel_Editor": {
                "next_cursor": config.get("weibo_cursor"), "cid": 4379552642725861, "count": 9}
        })
        collection = wheel(data=data)
        editor = collection.get("data", {}).get("Component_Channel_Editor", {})
        config.save(weibo_cursor=editor.get("next_cursor"))
        for item in editor.get("list", []):
            single = wheel(data=json.dumps({"Component_Play_Playinfo": {"oid": item["oid"]}}))
            yield {
                "media_id": item["media_id"],
                "oid": item["oid"],
                "mid": item["mid"],
                "title": item["title"],
                "cover_image": item["cover_image"],
                "url": list(single.get("data", {}).get("Component_Play_Playinfo", {}).get("urls", {}).values())[-1]
            }
        print(f"---第 {num} 页完成---")
    print(f"---数据获取结束, 共 {page} 页, {page * 9} 条---")


def wheel(data):
    url = "https://weibo.com/tv/api/component"
    params = {
        "page": "/tv/channel/4379552642725861/editor"
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
