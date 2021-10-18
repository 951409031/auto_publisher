import requests
from publisher.config.index import config


def _auth():
    url = "https://media.douyin.com/web/api/media/upload/auth/"
    headers = {
      'Cookie': config.get("Cookie")
    }
    response = requests.get(url, headers=headers).json()
    return response


def auth_info():
    url = "https://vas-lf-x.snssdk.com/video/openapi/v1/?action=GetVideoUploadParams&use_edge_node=1"
    auth_header = _auth()
    headers = {
        'authorization': auth_header["auth"],
        'x-tt-access': auth_header["ak"]
    }
    response = requests.get(url, headers=headers).json()
    response["data"].update(auth_header)
    return response["data"]


if __name__ == '__main__':
    print(auth_info())