"""
pip install requests
"""

import json

import requests


def _theone_announcement_catch():
    session = requests.session()
    session.headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7', 'Cache-Control': 'no-cache',
                       'Connection': 'keep-alive', 'Content-Length': '71',
                       'Content-Type': 'application/json;charset=UTF-8', 'Host': 'api.theone.art', 'Origin': 'https',
                       'Pragma': 'no-cache', 'Referer': 'https',
                       'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                       'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'empty',
                       'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    _theone_announcement_json = {}
    response = session.post(
        url="https://api.theone.art/market/api/dynamicNews/findNewsList",
        data=json.dumps({
            "categoryId": 35,
            "location": "list",
            "pageCount": 1,
            "pageSize": 9999,
            "top": 0
        }))

    if response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http request status != 200"}
    content_str = response.content.decode(response.encoding)
    try:
        content = json.loads(content_str)
    except Exception as e:
        return {"state": False, "data": {}, "msg": "http content parse error"}

    if content["code"] != 200:
        return {"state": False, "data": {}, "msg": "http content code != 200"}

    for i in content["data"]["records"]:
        try:
            if "平台通知" in _theone_announcement_json.keys():
                _theone_announcement_json["平台通知"].append(i)
            else:
                _theone_announcement_json["平台通知"] = [i]
        except Exception as e:
            pass

    return {"state": True, "data": _theone_announcement_json, "msg": ""}


if __name__ == "__main__":
    _theone_announcement_catch()

"""
{
    "平台通知": [
        {
            "name": "产品周报（10/27） | 关于唯艺元宇宙更新进度的公告",
            "summarize": null,
            "categoryName": null,
            "location": "list",
            "cover": "https://theoneart-common.oss-cn-qingdao.aliyuncs.com/author/8a28d69c2c690b62e0e0b5cd4b6f284f1666851132511.png",
            "updateBy": "王希腾",
            "releaseBy": "王希腾",
            "releaseTime": "2022/10/27 19:27:36",
            "activityStartTime": null,
            "activityEndTime": null,
            "uuid": "927d8ab39575485f71759e8006624dc8"
        },
        {
            "name": "产品周报（10/26） | 关于唯艺云、唯艺链更新进度的公告",
            "summarize": null,
            "categoryName": null,
            "location": "list",
            "cover": "https://theoneart-common.oss-cn-qingdao.aliyuncs.com/author/bb2b2a66f681353f7820efdd59a949c81666778905173.jpg",
            "updateBy": "王希腾",
            "releaseBy": "王希腾",
            "releaseTime": "2022/10/26 19:53:17",
            "activityStartTime": null,
            "activityEndTime": null,
            "uuid": "e07afb7ee59accaeddb08be135367097"
        }
    ]
}
"""
