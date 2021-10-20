import requests
from config.index import Config


def _auth():
    config = Config()
    url = "https://media.douyin.com/web/api/media/upload/auth/"
    headers = {
      'Cookie': config.get("douyin_cookie")
    }
    response = requests.get(url, headers=headers).json()
    if not response.get("auth"):
        print("---douyin_cookie 已失效, 请更新---")
    return response


def auth_info():
    url = "https://vas-lf-x.snssdk.com/video/openapi/v1/?action=GetVideoUploadParams&use_edge_node=1"
    auth_header = _auth()
    headers = {
        'authorization': auth_header.get("auth"),
        'x-tt-access': auth_header.get("ak")
    }
    response = requests.get(url, headers=headers).json()
    response["data"].update(auth_header)
    return response["data"]


if __name__ == '__main__':
    print(auth_info())