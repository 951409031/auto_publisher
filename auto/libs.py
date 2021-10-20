import requests
from spider import Spider
from publisher import Publisher


def spider_and_publish(**kwargs):
    publisher = Publisher()
    spider = Spider(platform=kwargs["platform"], t=kwargs["type"])
    for item in spider.bingo(page=kwargs["page"]):
        url = item["url"] if item["url"].startswith("http") else f"https:{item['url']}"
        publisher.update_meta(
            file=requests.get(url, stream=True).content,
            delay=0, text=item["title"]
        )
        publisher.create_meta()
