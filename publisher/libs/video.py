import os
import requests
from publisher.libs.utils import crc32
from publisher.libs.auth_info import auth_info


def upload(file):
    info = auth_info()
    url = f"https://{info['tos_host']}/{info['oid']}"
    headers = {
        "Authorization": info["tos_sign"],
        "Content-CRC32": crc32(file).lower()
    }
    response = requests.put(url, headers=headers, data=file).json()
    if response["success"] == 0:
        return info
    print("上传视频失败", response)


def confirm(file):
    info = upload(file)
    url = "https://vas-lf-x.snssdk.com/video/openapi/v1/"
    params = {
        "action": "UpdateVideoUploadInfos",
        "extra_param": info["extra_param"]
    }
    headers = {
        "Authorization": info["auth"],
        "x-tt-access": info["ak"]
    }
    data = {
        "vid": info["vid"],
        "oid": info["oid"],
        "token": info["token"],
        "poster_ss": 0,
        "is_exact_poster": True,
        "user_reference": ""
    }
    response = requests.post(url, params=params, headers=headers, json=data).json()
    if response["code"] == 2000:
        return info
    print("视频确认失败", response)


if __name__ == '__main__':
    p = os.path.join(os.path.abspath("../../"), "example/1.mp4")
    print(confirm(p))

