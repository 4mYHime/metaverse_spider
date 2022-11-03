"""
pip install beautifulsoup4 requests
"""

import json
import time

import requests
from bs4 import BeautifulSoup


def _ibox_announcement_catch():
    session = requests.session()
    request_time = str(round(time.time_ns() / 10 ** 6))
    session.headers = {
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
    response = session.get(url=f"https://notice.ibox.art/html/notice/notice.html?{request_time}")
    if response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http request status != 200"}
    content_str = response.content.decode()
    try:
        soup = BeautifulSoup(content_str, "html.parser")
        scripts = soup.find_all("script")
        target = scripts[2].string
        ibox_announcement_json = json.loads(target[target.find('{'): target[:target.rfind(';')].rfind(';')])
    except Exception as e:
        return {"state": False, "data": {}, "msg": "parse content error"}
    return {"state": True, "data": ibox_announcement_json, "msg": ""}


if __name__ == "__main__":
    _ibox_announcement_catch()

"""
{
    "allList": [
        {
            "className": "活动公告",
            "id": 2119,
            "noticeClassId": 15,
            "noticeName": "【iBox活动公告】「持仓进阶，《盛夏的斑》升星来袭！」空投白名单",
            "noticeTime": 1667451240000,
            "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2119.html?1667451277657"
        },
        {
            "className": "合成公告",
            "id": 2118,
            "noticeClassId": 8,
            "noticeName": "【iBox合成公告】全新藏品《神秘殿堂》/《神秘楼宇》合成白名单",
            "noticeTime": 1667447100000,
            "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2118.html?1667451277657"
        },
        {
            "className": "活动公告",
            "id": 2117,
            "noticeClassId": 15,
            "noticeName": "【iBox活动公告】「霜降不寒 秋风温热」活动 《汉寿亭侯关云长1:1兑换资格卡》权益兑现",
            "noticeTime": 1667446200000,
            "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2117.html?1667451277657"
        }
    ],
    "byClassList": [
        {
            "className": "上新公告",
            "noticeClassId": 7,
            "noticeList": [
                {
                    "id": 2097,
                    "noticeClassId": 7,
                    "noticeName": "【iBox上新公告】「启明星」「经典名人堂」系列【优质】藏品《聚财童子》白名单",
                    "noticeTime": 1667376120000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2097.html?1667451277657"
                }
            ]
        },
        {
            "className": "合成公告",
            "noticeClassId": 8,
            "noticeList": [
                {
                    "id": 2118,
                    "noticeClassId": 8,
                    "noticeName": "【iBox合成公告】全新藏品《神秘殿堂》/《神秘楼宇》合成白名单",
                    "noticeTime": 1667447100000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2118.html?1667451277657"
                }
            ]
        },
        {
            "className": "澄清公告",
            "noticeClassId": 11,
            "noticeList": [
                {
                    "id": 1895,
                    "noticeClassId": 11,
                    "noticeName": "【iBox澄清公告】关于《精卫》空投事宜的相关处理方案",
                    "noticeTime": 1666158300000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_1895.html?1667451277657"
                }
            ]
        },
        {
            "className": "空投公告",
            "noticeClassId": 9,
            "noticeList": [
                {
                    "id": 2063,
                    "noticeClassId": 9,
                    "noticeName": "【iBox空投公告】「生旦净末丑」系列藏品进行空投白名单",
                    "noticeTime": 1667216880000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2063.html?1667451277657"
                }
            ]
        },
        {
            "className": "寄售公告",
            "noticeClassId": 10,
            "noticeList": [
                {
                    "id": 2098,
                    "noticeClassId": 10,
                    "noticeName": "【iBox寄售公告】iBox平台批量藏品开放寄售",
                    "noticeTime": 1667382060000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2098.html?1667451277657"
                }
            ]
        },
        {
            "className": "iBox宇宙编年史",
            "noticeClassId": 17,
            "noticeList": [
                {
                    "id": 2100,
                    "noticeClassId": 17,
                    "noticeName": "【元宇宙编年史】【机密】关于已探索行星领主资料介绍",
                    "noticeTime": 1667383800000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2100.html?1667451277657"
                }
            ]
        },
        {
            "className": "活动公告",
            "noticeClassId": 15,
            "noticeList": [
                {
                    "id": 2119,
                    "noticeClassId": 15,
                    "noticeName": "【iBox活动公告】「持仓进阶，《盛夏的斑》升星来袭！」空投白名单",
                    "noticeTime": 1667451240000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2119.html?1667451277657"
                }
            ]
        },
        {
            "className": "系统公告",
            "noticeClassId": 14,
            "noticeList": [
                {
                    "id": 2079,
                    "noticeClassId": 14,
                    "noticeName": "【iBox系统公告】iBox平台公告栏优化升级",
                    "noticeTime": 1667310900000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2079.html?1667451277657"
                }
            ]
        },
        {
            "className": "赋能公告",
            "noticeClassId": 13,
            "noticeList": [
                {
                    "id": 621,
                    "noticeClassId": 13,
                    "noticeName": "【iBox赋能公告】iBox藏品赋能清单（1）",
                    "noticeTime": 1656947582000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_621.html?1667451277657"
                }
            ]
        }
    ],
    "tabList": [
        {
            "className": "上新公告",
            "id": 7
        },
        {
            "className": "合成公告",
            "id": 8
        },
        {
            "className": "澄清公告",
            "id": 11
        },
        {
            "className": "空投公告",
            "id": 9
        },
        {
            "className": "寄售公告",
            "id": 10
        },
        {
            "className": "iBox宇宙编年史",
            "id": 17
        },
        {
            "className": "活动公告",
            "id": 15
        },
        {
            "className": "系统公告",
            "id": 14
        },
        {
            "className": "赋能公告",
            "id": 13
        }
    ]
}
"""
