import json
import requests


def _42verse_announcement_catch():
    session = requests.session()
    session.headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
        'Host': 'api.42verse.shop', 'Pragma': 'no-cache', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    _42verse_announcement_json = {}
    response = session.get(url="https://api.42verse.shop/api/front/notice/list?cid=&lastId=&limit=99999&page=1")

    if response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http request status != 200"}
    content_str = response.content.decode(response.encoding)
    try:
        content = json.loads(content_str)
    except Exception as e:
        return {"state": False, "data": {}, "msg": "content parse error"}

    if content["code"] != 200:
        return {"state": False, "data": {}, "msg": "content code != 200"}

    for i in content["data"]["list"]:
        try:
            title = i['title'].split("｜")[0]
            if title in _42verse_announcement_json.keys():
                _42verse_announcement_json[title].append(i)
            else:
                _42verse_announcement_json[title] = [i]
        except Exception as e:
            pass
    return {"state": True, "data": _42verse_announcement_json, "msg": ""}


if __name__ == "__main__":
    _42verse_announcement_catch()

"""
{
    "通知": [
        {
            "id": 923,
            "title": "通知｜首次惊喜合成活动开启预告",
            "author": "42ART",
            "synopsis": "点击查看详情",
            "visit": "9523",
            "content": "<p><img class=\"wscnph\" src=\"https://img.42verse.shop/crmebimage/public/content/2022/10/30/fef54115095e4679aecbe3b415be524aqprsmmsts5.jpg\" /></p>",
            "sort": 923,
            "status": 0,
            "createTime": "2022-10-30"
        }
    ],
    "空投": [
        {
            "id": 919,
            "title": "空投｜《夏侯惇》持仓福利空投发放预告",
            "author": "42ART",
            "synopsis": "点击查看详情",
            "visit": "15958",
            "content": "<p><img class=\"wscnph\" src=\"https://img.42verse.shop/crmebimage/public/content/2022/10/30/ef509bf6fd82436bb8e5e714f31f56f2134obnzend.jpg\" /></p>",
            "sort": 918,
            "status": 0,
            "createTime": "2022-10-30"
        }
    ],
    "公示": [
        {
            "id": 915,
            "title": "公示｜“三国”系列《诸葛亮》空投名单",
            "author": "42ART",
            "synopsis": "点击查看详情",
            "visit": "10118",
            "content": "<p>亲爱的42ART社群伙伴：</p>\n<p>以下为10月29日&ldquo;三国&rdquo;系列《诸葛亮》空投名单<br /><a href=\"https://docs.qq.com/sheet/DRlF6dkhuSWl2QnZB?tab=BB08J2\" target=\"_blank\" rel=\"noopener\">https://docs.qq.com/sheet/DRlF6dkhuSWl2QnZB?tab=BB08J2</a></p>\n<p><br />温馨提示：<br />持有1张《飞向天际》空投8个《诸葛亮》，持有1张《古今交辉》空投15个《诸葛亮》。空投将于名单公示后两日内发放。空投权益可叠加。</p>\n<p>活动详情网址：<br /><a href=\"https://www.42verse.shop/NoticeDetails/909\" target=\"_blank\" rel=\"noopener\">https://www.42verse.shop/NoticeDetails/909</a></p>\n<p>&nbsp;</p>\n<p style=\"text-align: right;\">42ART</p>\n<p style=\"text-align: right;\">2022年10月29日</p>",
            "sort": 915,
            "status": 0,
            "createTime": "2022-10-29"
        }
    ],
    "兑换": [
        {
            "id": 907,
            "title": "兑换｜“三国”系列《三国魔方》兑换活动开启预告",
            "author": "42ART",
            "synopsis": "点击查看详情",
            "visit": "18713",
            "content": "<p><img class=\"wscnph\" src=\"https://img.42verse.shop/crmebimage/public/content/2022/10/29/b23b854f577e434cbac3534dcaa62780g7v7oxe1jm.jpg\" /></p>",
            "sort": 908,
            "status": 0,
            "createTime": "2022-10-29"
        }
    ],
    "合成": [
        {
            "id": 905,
            "title": "合成｜“三国”系列《吕布》合成活动开启预告",
            "author": "42ART",
            "synopsis": "点击查看详情",
            "visit": "28772",
            "content": "<p><img class=\"wscnph\" src=\"https://img.42verse.shop/crmebimage/public/content/2022/10/28/1335d9e9808e4e92a88aa6c4848392804atnf626ob.jpg\" /></p>",
            "sort": 905,
            "status": 0,
            "createTime": "2022-10-28"
        }
    ]
}
"""
