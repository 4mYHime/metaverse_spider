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
        ":authority": "notice.ibox.art",
        ":method": "GET",
        ":path": f"/html/notice/notice.html?{request_time}",
        ":scheme": "https",
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': ' https',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    response = session.get(url=f"https://notice.ibox.art/html/notice/notice.html?{request_time}")
    if response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http request status != 200"}
    content_str = response.content.decode(response.encoding)
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
    "byClassList": [
        {
            "className": "上新公告",
            "noticeClassId": 7,
            "noticeList": [
                {
                    "id": 2045,
                    "noticeName": "【iBox上新公告】「创意之境」「原艺同盟」系列藏品《火牙城》白名单",
                    "noticeTime": 1667112300000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2045.html?1667152283779"
                }
            ]
        },
        {
            "className": "合成公告",
            "noticeClassId": 8,
            "noticeList": [
                {
                    "id": 2051,
                    "noticeName": "【iBox合成公告】全新藏品《蓝色钻石谷》/《红色钻石谷》随机合成公告",
                    "noticeTime": 1667131200000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2051.html?1667152283779"
                }
            ]
        },
        {
            "className": "澄清公告",
            "noticeClassId": 11,
            "noticeList": [
                {
                    "id": 1895,
                    "noticeName": "【iBox澄清公告】关于《精卫》空投事宜的相关处理方案",
                    "noticeTime": 1666158300000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_1895.html?1667152283779"
                }
            ]
        },
        {
            "className": "空投公告",
            "noticeClassId": 9,
            "noticeList": [
                {
                    "id": 2018,
                    "noticeName": "【iBox空投公告】「赛博八仙」系列藏品空投白名单",
                    "noticeTime": 1666955460000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2018.html?1667152283779"
                }
            ]
        },
        {
            "className": "寄售公告",
            "noticeClassId": 10,
            "noticeList": [
                {
                    "id": 2046,
                    "noticeName": "【iBox寄售公告】「阿尔法星」「观星者之塔」系列藏品《足球小将》开放寄售",
                    "noticeTime": 1667116140000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2046.html?1667152283779"
                }
            ]
        },
        {
            "className": "iBox宇宙编年史",
            "noticeClassId": 17,
            "noticeList": [
                {
                    "id": 1786,
                    "noticeName": "【iBox宇宙编年史】寻物梦幻世界",
                    "noticeTime": 1665316920000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_1786.html?1667152283779"
                }
            ]
        },
        {
            "className": "活动公告",
            "noticeClassId": 15,
            "noticeList": [
                {
                    "id": 2052,
                    "noticeName": "【iBox活动公告】「霜降不寒 秋风温热」感恩回馈系列活动（八）-《山海经-峳峳优先购资格卡》白名单",
                    "noticeTime": 1667131440000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2052.html?1667152283779"
                }
            ]
        },
        {
            "className": "系统公告",
            "noticeClassId": 14,
            "noticeList": [
                {
                    "id": 2024,
                    "noticeName": "【iBox系统公告】关于对藏品《汉寿亭侯关云长》销毁合同公告",
                    "noticeTime": 1666973580000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2024.html?1667152283779"
                }
            ]
        },
        {
            "className": "赋能公告",
            "noticeClassId": 13,
            "noticeList": [
                {
                    "id": 621,
                    "noticeName": "【iBox赋能公告】iBox藏品赋能清单（1）",
                    "noticeTime": 1656947582000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_621.html?1667152283779"
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
    ],
    "zhList": [
        {
            "className": "上新公告",
            "noticeClassId": 7,
            "noticeList": [
                {
                    "id": 2045,
                    "noticeName": "【iBox上新公告】「创意之境」「原艺同盟」系列藏品《火牙城》白名单",
                    "noticeTime": 1667112300000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2045.html?1667152283779"
                }
            ]
        },
        {
            "className": "合成公告",
            "noticeClassId": 8,
            "noticeList": [
                {
                    "id": 2051,
                    "noticeName": "【iBox合成公告】全新藏品《蓝色钻石谷》/《红色钻石谷》随机合成公告",
                    "noticeTime": 1667131200000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2051.html?1667152283779"
                }
            ]
        },
        {
            "className": "澄清公告",
            "noticeClassId": 11,
            "noticeList": [
                {
                    "id": 1895,
                    "noticeName": "【iBox澄清公告】关于《精卫》空投事宜的相关处理方案",
                    "noticeTime": 1666158300000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_1895.html?1667152283779"
                }
            ]
        },
        {
            "className": "空投公告",
            "noticeClassId": 9,
            "noticeList": [
                {
                    "id": 2018,
                    "noticeName": "【iBox空投公告】「赛博八仙」系列藏品空投白名单",
                    "noticeTime": 1666955460000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2018.html?1667152283779"
                }
            ]
        },
        {
            "className": "寄售公告",
            "noticeClassId": 10,
            "noticeList": [
                {
                    "id": 2046,
                    "noticeName": "【iBox寄售公告】「阿尔法星」「观星者之塔」系列藏品《足球小将》开放寄售",
                    "noticeTime": 1667116140000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2046.html?1667152283779"
                }
            ]
        },
        {
            "className": "iBox宇宙编年史",
            "noticeClassId": 17,
            "noticeList": [
                {
                    "id": 1786,
                    "noticeName": "【iBox宇宙编年史】寻物梦幻世界",
                    "noticeTime": 1665316920000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_1786.html?1667152283779"
                }
            ]
        },
        {
            "className": "活动公告",
            "noticeClassId": 15,
            "noticeList": [
                {
                    "id": 2052,
                    "noticeName": "【iBox活动公告】「霜降不寒 秋风温热」感恩回馈系列活动（八）-《山海经-峳峳优先购资格卡》白名单",
                    "noticeTime": 1667131440000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2052.html?1667152283779"
                }
            ]
        },
        {
            "className": "系统公告",
            "noticeClassId": 14,
            "noticeList": [
                {
                    "id": 2024,
                    "noticeName": "【iBox系统公告】关于对藏品《汉寿亭侯关云长》销毁合同公告",
                    "noticeTime": 1666973580000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_2024.html?1667152283779"
                }
            ]
        },
        {
            "className": "赋能公告",
            "noticeClassId": 13,
            "noticeList": [
                {
                    "id": 621,
                    "noticeName": "【iBox赋能公告】iBox藏品赋能清单（1）",
                    "noticeTime": 1656947582000,
                    "noticeUrl": "https://notice.ibox.art/html/notice/detail/notice_detail_621.html?1667152283779"
                }
            ]
        },
        {
            "noticeClassId": 0,
            "noticeList": []
        }
    ]
}
"""
