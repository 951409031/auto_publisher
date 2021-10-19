import requests
from spider import Spider
from publisher import Publisher

if __name__ == '__main__':
    publisher = Publisher()
    spider = Spider(platform="weibo", t=1)
    for item in spider.bingo(page=1):
        url = item["url"] if item["url"].startswith("http") else f"https:{item['url']}"
        publisher.update_meta(
            file=requests.get(url, stream=True).content,
            delay=0, text=item["title"]
        )
        publisher.create_meta()

