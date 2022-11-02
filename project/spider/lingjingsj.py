"""
pip install requests
"""

import json

import requests


def _lingjingsj_announcement_catch():
    session = requests.session()
    session.headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br',
                       'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7', 'cache-control': 'no-cache',
                       'content-length': '165', 'content-type': 'application/json',
                       'origin': 'https://vip.lingjingsj.com',
                       'pragma': 'no-cache', 'referer': 'https://vip.lingjingsj.com/h5/', 'sec-fetch-dest': 'empty',
                       'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin',
                       'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    _lingjingsj_announcement_json = {}
    auth_response = session.post(
        url="https://vip.lingjingsj.com/api/passwordLogin",
        data=json.dumps({"mobile": "13456993881", "password": "13.13.13."}))
    if auth_response.status_code != 200:
        return {"state": False, "data": {}, "msg": "http_auth.status_code != 200"}

    try:
        auth_content = json.loads(auth_response.content.decode())
    except Exception as e:
        return {"state": False, "data": {}, "msg": "http_auth.content parse error"}
    if auth_content['code'] != 1:
        return {"state": False, "data": {}, "msg": "http_auth.content.code != 1"}
    token = auth_response.headers.get("token", None)
    if not token:
        return {"state": False, "data": {}, "msg": "http_auth.headers.token invalid"}

    page = 1
    while True:
        response = session.post(
            url="https://vip.lingjingsj.com/api/index/noticeList",
            data=json.dumps({"page": page,
                             "per_page": 10,
                             "token": token}))

        if response.status_code != 200:
            continue
        content_str = response.content.decode(response.encoding)
        try:
            content = json.loads(content_str)
        except Exception as e:
            continue

        if content["code"] != 1:
            continue

        for i in content["data"]["data"]:
            try:
                name = i["tag"]
                if name in _lingjingsj_announcement_json.keys():
                    _lingjingsj_announcement_json[name].append(i)
                else:
                    _lingjingsj_announcement_json[name] = [i]
            except Exception as e:
                continue

        if content["data"]["current_page"] == content["data"]["last_page"]:
            break
        else:
            page += 1

    return {"state": True, "data": _lingjingsj_announcement_json, "msg": ""}


if __name__ == "__main__":
    _lingjingsj_announcement_catch()

"""
{
    "熔炼预告": [
        {
            "id": 73,
            "title": "【熔炼最新公告】",
            "url": "",
            "create_time": "2022-10-31 17:32:26",
            "tag": "熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20221031/260497e0c2f0462495a72991ca2f4fad.jpg\"><br></p>",
            "update_time": "2022-10-31 17:32:29",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "上新": [
        {
            "id": 72,
            "title": "【灵镜上新公告】",
            "url": "",
            "create_time": "2022-10-31 17:31:37",
            "tag": "上新",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20221031/056ceb9b3c2bf014b3cd3017a1918f2f.jpg\"><br></p>",
            "update_time": "2022-10-31 17:31:39",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "寄售": [
        {
            "id": 58,
            "title": "【灵镜寄售公告】",
            "url": "",
            "create_time": "2022-10-14 23:26:09",
            "tag": "寄售",
            "content": "<p>亲爱的灵镜用户：</p><p>&nbsp; &nbsp; 您好！</p><p>&nbsp; &nbsp; 【 囚牛】 【伏羲 】&nbsp;&nbsp;&nbsp;数字藏品将于2022年10月15日开放寄售&nbsp; &nbsp;</p><p><img src=\"https://vip.lingjingsj.com/uploads/20221001/2a16f7a1317021fd20c87b515900888b.jpg\"><br></p><p><br></p><p><img src=\"https://vip.lingjingsj.com/uploads/20221010/d75905cd556e4cb9d7a73418018dc2a8.jpg\"><br></p><p>&nbsp; &nbsp;&nbsp;</p><p>&nbsp; &nbsp; &nbsp;敬请广大用户知悉，谢谢！<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 灵镜数字藏品<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2022年10月1日<br><br>灵镜风险提示： 灵镜&nbsp; 数字藏品平台发售的数字藏品仅具备收藏欣赏价值，官方对藏品价格不构成任何指导意义，请谨慎购买，严防炒作。<br>灵镜&nbsp; 平台郑重提醒广大用户：不使用第三方工具锁单、抢单！不影响其他藏家之间的正常转让寄售；以免引起自身 灵镜&nbsp; 账号被封禁、绑定支付账号被冻结等不必要的损失，也希望广大用户在接收到任何非官方渠道的信息时，不轻信，不传谣，共同创造一个清新的网络环境。</p>",
            "update_time": "2022-10-14 23:26:11",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "拉新活动！": [
        {
            "id": 41,
            "title": "黄金十月，神话降临活动开启。",
            "url": "",
            "create_time": "2022-10-08 19:27:46",
            "tag": "拉新活动！",
            "content": "<p>&nbsp; 灵镜视界神话系列新品鹦鹉上线！神话系列穷奇、饕餮溢价十倍，不容错过！转发详情图加本段文字至5个150人以上数字藏品群（灵镜视界官方群除外）QQ群客服处登记（客服QQ3395182054），即可获得一次白名单抽签机会，共500份。登记截止时间：10.9日13.00。累积六次未中签可熔炼成一次白名单优先购，买到就是赚到！点击链接获取财富密码～<img src=\"file:///C:\\Users\\1\\AppData\\Roaming\\Tencent\\QQTempSys\\%W@GJ$ACOF(TYDYECOKVDYB.png\">https://vip.lingjingsj.com/h5/#/pages/user/myCollects<img src=\"https://vip.lingjingsj.com/uploads/20221008/4c558ab9f383da023682f6d7267ecaec.jpg\"><br></p>",
            "update_time": "2022-10-09 00:41:37",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "东皇太一熔炼预告": [
        {
            "id": 37,
            "title": "【熔炼最新公告】",
            "url": "",
            "create_time": "2022-10-06 16:06:54",
            "tag": "东皇太一熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20221006/c5060118814b79b7b607cc8dd0cb174b.jpg\"><br></p>",
            "update_time": "2022-10-06 16:06:57",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "皇帝熔炼预告": [
        {
            "id": 34,
            "title": "【熔炼最新公告】",
            "url": "",
            "create_time": "2022-10-04 16:02:46",
            "tag": "皇帝熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20221004/a3cd386ba945927029a958d66e4ec5bf.jpg\"><br></p>",
            "update_time": "2022-10-04 16:03:20",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "伏羲熔炼预告": [
        {
            "id": 31,
            "title": "【熔炼最新公告】",
            "url": "",
            "create_time": "2022-10-02 16:35:44",
            "tag": "伏羲熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20221002/29ef99884ca790e60f0b13a650c8bc9d.jpg\"><br></p>",
            "update_time": "2022-10-02 16:35:47",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "凤凰熔炼预告": [
        {
            "id": 28,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-29 17:58:51",
            "tag": "凤凰熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20220929/45d597eec86650a4d1a00c239cf724d3.jpg\"><br></p>",
            "update_time": "2022-09-29 17:58:53",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "神农熔炼预告": [
        {
            "id": 26,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-28 18:13:09",
            "tag": "神农熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20220928/6ee63d51b17c362a15711c822c324c92.jpg\"><br></p>",
            "update_time": "2022-09-28 18:13:12",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "上周回购详情": [
        {
            "id": 24,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-27 17:53:00",
            "tag": "上周回购详情",
            "content": "<section powered-by=\"xiumi.us\"><h1><strong>灵镜视界原石回购</strong>&nbsp; &nbsp;&nbsp;</h1><p>&nbsp; &nbsp; &nbsp; 灵镜视界原石回购计划于8月22日00：00正式启动，道友们可将原石寄存在藏宝阁中，等待官方回购，<strong>本周回购价格</strong>及<strong>上周回购详情</strong>已公布，请各道友查阅！<br></p></section><p powered-by=\"xiumi.us\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p><p powered-by=\"xiumi.us\">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>第一阶段原石回购计划</strong></p><p powered-by=\"xiumi.us\"><img src=\"https://vip.lingjingsj.com/uploads/20220927/23f7b52f8c4470e3ca429a92db66d949.jpg\"><strong><br></strong></p><p powered-by=\"xiumi.us\">*注：第一周回收价格为399灵石，之后每周回收价格均高于上一周回收价格的最低价。原石回购期间，因鸿蒙宇宙不稳定，紫气无法诞生，回购结束后，紫气将会数倍迸发。&nbsp;&nbsp;<br></p><p powered-by=\"xiumi.us\"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</strong></p><p powered-by=\"xiumi.us\"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 上周回购原石编号</strong>&nbsp;&nbsp;</p><p powered-by=\"xiumi.us\"><img src=\"https://vip.lingjingsj.com/uploads/20220927/9bee78347d16df0c1b6cdb3aedfce264.jpg\"><br></p>",
            "update_time": "2022-09-27 17:53:02",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "盘古熔炼预告": [
        {
            "id": 23,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-26 18:58:10",
            "tag": "盘古熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20220926/07ff0fa2d17ee612b6dd2657610c9b6a.jpg\"><br></p>",
            "update_time": "2022-09-26 18:58:13",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "天狗熔炼预告": [
        {
            "id": 16,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-21 12:07:41",
            "tag": "天狗熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20220921/57f8e3fe61a99c99fad057845b0c500b.jpg\"><br></p>",
            "update_time": "2022-09-21 12:07:43",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "麒麟熔炼预告": [
        {
            "id": 13,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-13 15:43:28",
            "tag": "麒麟熔炼预告",
            "content": "<p><img src=\"https://vip.lingjingsj.com/uploads/20220913/a5b6bbc1b8f14c875f15e0cd91935234.jpg\"><br></p>",
            "update_time": "2022-09-13 15:43:31",
            "type": 1,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "藏宝阁添新宝": [
        {
            "id": 11,
            "title": "【最新公告】",
            "url": "",
            "create_time": "2022-09-09 12:15:04",
            "tag": "藏宝阁添新宝",
            "content": "<p>&nbsp; &nbsp;联名藏品“烧火棍”登录藏宝阁，各位道友可用灵气直接兑换。</p><p><br></p><p><br></p><p><br></p><p>&nbsp;&nbsp;</p>",
            "update_time": "2022-09-09 12:15:55",
            "type": 1,
            "is_push": 1,
            "praise": 47,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ],
    "最新公告": [
        {
            "id": 5,
            "title": "上周回购详情",
            "url": "https://mp.weixin.qq.com/s/u4yW76JF_7QQy5Lqe_JTLg",
            "create_time": "2022-09-06 17:15:05",
            "tag": "最新公告",
            "content": "",
            "update_time": "2022-09-06 17:15:17",
            "type": 2,
            "is_push": 1,
            "praise": 0,
            "browse": 0,
            "praise_count": 0,
            "image": ""
        }
    ]
}
"""