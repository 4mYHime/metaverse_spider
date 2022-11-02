"""
pip install beautifulsoup4 requests
"""

import json
import time

import requests
from bs4 import BeautifulSoup


def _18art_announcement_catch():
    session = requests.session()
    request_time = str(round(time.time_ns() / 10 ** 6))
    session.headers = {
        "authority": "info.18art.art",
        "method": "GET",
        "path": f"/html/infor/infor.html?sub=0&v={request_time}",
        "scheme": "https",
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    response = session.get(url=f"https://info.18art.art/html/infor/infor.html?sub=0&v={request_time}")
    if response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http request status != 200"}
    content_str = response.content.decode(response.encoding)
    try:
        soup = BeautifulSoup(content_str, "html.parser")
        scripts = soup.find_all("script")
        target = scripts[2].string
        target = target[target.find(';') + 1: target.rfind(';')]
        ibox_announcement_json = json.loads(target[target.find('{'):])
    except Exception as e:
        return {"state": False, "data": {}, "msg": "parse content error"}
    return {"state": True, "data": ibox_announcement_json, "msg": ""}


if __name__ == "__main__":
    _18art_announcement_catch()

""""{
    "noticeList": [
        {
            "classId": 6,
            "className": "活动公告",
            "list": [
                {
                    "classId": 6,
                    "className": "活动公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/89cf92715537445a9ddcc39ec1608b82.png",
                    "id": 2068,
                    "time": 1667143920000,
                    "title": "【十八数藏活动公告】注册赢好礼，欢乐齐相聚（三）特别提醒",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2068.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 10,
            "className": "藏品鉴赏",
            "list": [
                {
                    "classId": 10,
                    "className": "藏品鉴赏",
                    "coverImg": "/file/oss/nft/image/nft-goods/5a0d718ba03a4f879526244b92a2f2b8.jpg",
                    "id": 1835,
                    "time": 1666357560000,
                    "title": "【十八数藏藏品鉴赏】非遗典藏：韩熙载夜宴图",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_1835.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 5,
            "className": "上新公告",
            "list": [
                {
                    "classId": 5,
                    "className": "上新公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/856048e455624802a9b2b156b5426318.png",
                    "id": 2075,
                    "time": 1667193780000,
                    "title": "【十八数藏上新公告】心灵物语系列藏品《曙光》今日上线",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2075.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 7,
            "className": "合成公告",
            "list": [
                {
                    "classId": 7,
                    "className": "合成公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/8cf0bfa942374844a1ee516e80228e26.png",
                    "id": 2062,
                    "time": 1667128680000,
                    "title": "【十八数藏合成公告】树下 “鲁积分”与“何二丫”的故事",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2062.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 3,
            "className": "运营公告",
            "list": [
                {
                    "classId": 3,
                    "className": "运营公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/f8153e49341e4f87a94976b276438329.png",
                    "id": 1504,
                    "time": 1664674620000,
                    "title": "【十八数藏运营公告】十八数藏iOS App下载流程及入口",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_1504.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 4,
            "className": "寄售公告",
            "list": [
                {
                    "classId": 4,
                    "className": "寄售公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/55988745109f4a9fa1cc2e7f64b50363.png",
                    "id": 2078,
                    "time": 1667199000000,
                    "title": "【十八数藏寄售公告】《隐迹修道曹国舅》开放寄售",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2078.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 11,
            "className": "赋能公告",
            "list": [
                {
                    "classId": 11,
                    "className": "赋能公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/ab8f12c07ac3435abb3d86fc88d2ef1d.jpg",
                    "id": 1996,
                    "time": 1666945680000,
                    "title": "【十八数藏赋能公告】对《 柜山神》、《赤鱬》、《梦游山海》赋能调整公告",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_1996.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 9,
            "className": "空投公告",
            "list": [
                {
                    "classId": 9,
                    "className": "空投公告",
                    "coverImg": "/file/oss/nft/image/nft-goods/0632f35eec4b4461a3b483b6fdcc3669.png",
                    "id": 2074,
                    "time": 1667190840000,
                    "title": "【十八数藏空投公告】对藏品《千秋风骨》进行空投公告",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2074.html?v=1667201742155"
                }
            ]
        },
        {
            "classId": 8,
            "className": "白名单",
            "list": [
                {
                    "classId": 8,
                    "className": "白名单",
                    "coverImg": "/file/oss/nft/image/nft-goods/19b651cb660347cfabbb3432cbfaaa03.png",
                    "id": 2079,
                    "time": 1667201700000,
                    "title": "【十八数藏白名单公告】《新生》优先购白名单",
                    "url": "https://info.18art.art/html/infor/detail/infor_detail_2079.html?v=1667201742155"
                }
            ]
        }
    ]
}"""