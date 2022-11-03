"""
pip install requests
"""

import json
import random
import time

import requests


def _shuzimart_announcement_catch():
    session = requests.session()
    session.headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7', 'Cache-Control': 'no-cache',
                       'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded',
                       'Host': 'h5.shuzimart.com', 'Pragma': 'no-cache', 'Referer': 'https',
                       'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                       'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'empty',
                       'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    _shuzimart_announcement_json = {}
    page = 1
    while True:
        response = session.get(
            url=f"https://h5.shuzimart.com/index.php?s=/api/article/lists&page={page}&category_id=0&wxapp_id=10001&is_h5=1&token=")

        if response.status_code != 200:
            continue
        content_str = response.content.decode(response.encoding)
        try:
            content = json.loads(content_str)
        except Exception as e:
            continue

        if content["code"] != 1:
            continue

        for i in content["data"]["list"]["data"]:
            try:
                name = i['category']['name']
                if name in _shuzimart_announcement_json.keys():
                    _shuzimart_announcement_json[name].append(i)
                else:
                    _shuzimart_announcement_json[name] = [i]
            except Exception as e:
                pass
        if content["data"]["list"]["current_page"] == content["data"]["list"]["last_page"]:
            break
        else:
            page += 1
            time.sleep(random.random())
    return {"state": True, "data": _shuzimart_announcement_json, "msg": ""}


if __name__ == "__main__":
    _shuzimart_announcement_catch()

"""
{
    "官方公告": [
        {
            "article_id": 22,
            "article_title": "2022年10月10日更新事项",
            "show_type": 10,
            "category_id": 1,
            "image_id": 332,
            "article_sort": 1,
            "article_status": 1,
            "virtual_views": 7000,
            "actual_views": 483,
            "article_abstract": "今日更新",
            "image": {
                "file_id": 332,
                "storage": "local",
                "group_id": 0,
                "file_url": "",
                "file_name": "20221014114803278238460.png",
                "file_size": 80437,
                "file_type": "image",
                "extension": "png",
                "is_user": 0,
                "is_recycle": 0,
                "is_delete": 0,
                "store_user_id": 10001,
                "file_path": " "
            },
            "category": {
                "category_id": 1,
                "name": "官方公告",
                "sort": 1,
                "wxapp_id": 10001,
                "create_time": "2022-07-25 19:13:52",
                "update_time": "2022-08-08 13:52:43"
            },
            "show_views": 7483,
            "view_time": "2022-10-10"
        }
    ],
    "活动速看": [
        {
            "article_id": 16,
            "article_title": "月满中秋，天涯共赏",
            "show_type": 20,
            "category_id": 2,
            "image_id": 225,
            "article_sort": 1,
            "article_status": 1,
            "virtual_views": 1000,
            "actual_views": 749,
            "article_abstract": "祝数字玛特家人们中秋快乐",
            "image": {
                "file_id": 225,
                "storage": "local",
                "group_id": 0,
                "file_url": "",
                "file_name": "2022090410145360e697484.jpg",
                "file_size": 410691,
                "file_type": "image",
                "extension": "jpg",
                "is_user": 0,
                "is_recycle": 0,
                "is_delete": 0,
                "store_user_id": 10001,
                "file_path": "https://h5.shuzimart.com/uploads/2022090410145360e697484.jpg"
            },
            "category": {
                "category_id": 2,
                "name": "活动速看",
                "sort": 2,
                "wxapp_id": 10001,
                "create_time": "2022-07-27 11:25:35",
                "update_time": "2022-08-08 13:52:08"
            },
            "show_views": 1749,
            "view_time": "2022-09-04"
        }
    ]
}
"""
