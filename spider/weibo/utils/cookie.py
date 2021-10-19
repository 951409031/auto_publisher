import requests
import random
import json
import re


class Cookie(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        }
        self.sub, self.tid = "", ""
        self.tid_pattern = re.compile(r"^(\w|=)*$")
        self.update()

    def get_tid(self):
        tid_url = "https://passport.weibo.com/visitor/genvisitor"
        data = {
            "cb": "gen_callback",
            "fp": {
                "os": "3",
                "browser": "Chrome69,0,3497,100",
                "fonts": "undefined",
                "screenInfo": "1920*1080*24",
                "plugins": "Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native Client"
            }
        }
        resp = requests.post(url=tid_url, data=data, headers=self.headers)

        if resp.status_code == 200:
            ret = eval(
                resp.text.replace("window.gen_callback && gen_callback(", "").replace(");", "").replace("true", "1"))
            self.tid = ret.get('data').get('tid')
            while True:
                if self.tid_pattern.match(self.tid):
                    break
                print("当前 tid 无效, 重新获取", self.tid)
                self.tid = self.get_tid()
            return self.tid
        print("---获取 tid 失败---")

    def update(self):
        cookies = {
            "tid": self.tid if self.tid else self.get_tid()
        }
        url = f"https://passport.weibo.com/visitor/visitor?a=incarnate&t={self.tid}&w=2&c=095&gc=&cb=cross_domain&from=weibo&_rand={random.random()}"
        resp = requests.get(url, cookies=cookies, headers=self.headers)
        ret = json.loads(
            resp.text.replace("window.cross_domain && cross_domain(", "").replace(");", "").replace("null", "1"))
        sub = ret.get("data", {}).get("sub")
        if sub:
            self.sub = sub
            return self.sub
        print("---获取 cookie 失败---", ret)


cookie = Cookie()
