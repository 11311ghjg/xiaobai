import os
import time

import requests
import hashlib
SECRET_KEY = "QJ1OV4tfpl"
APP_KEY = "20f45751ab1cc7e0"

def get_announcement():
    url = "http://121.37.210.30/Announcement/get_announcement.php"
    r = requests.get(url)
    print(r.text)
def generate_sign(params, secret_key):
    """
    签名算法已经验证无误，它会根据传入的参数和密钥生成正确的签名。
    """
    # 确保在计算前移除可能存在的 sign 键
    if 'sign' in params:
        del params['sign']
    sorted_keys = sorted(params.keys())
    query_string_parts = []
    for key in sorted_keys:
        query_string_parts.append(f"{key}={params[key]}")
    query_string = "&".join(query_string_parts)
    string_to_sign = query_string + secret_key
    md5 = hashlib.md5()
    md5.update(string_to_sign.encode('utf-8'))
    return md5.hexdigest()


def query(user):
    url = "https://www.52bjy.com/api/app/envcash.php"
    payload = {
        "action": "awardlist",
        "genre":0,
        "appkey": APP_KEY,
        "merchant_id": 2,
        "type":"award",
        "method": "getsigninfo",
        "username": user,
    }
    payload['sign'] = generate_sign(payload, SECRET_KEY)
    headers = {
        "Host": "www.52bjy.com",
        "Connection": "keep-alive",
        "xweb_xhr": "1",
        "EnvConnection": "test",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wxadd84841bd31a665/114/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    res = requests.get(url, headers=headers,params=payload).json()
    if res['code'] == 200:
        print(f"账户余额查询成功:{res['data']['award_amount']} 元")
    else:
        print(f"账户余额查询失败")


def sign_in(user):
    """
    发起签到请求。
    """
    url = "https://www.52bjy.com/api/app/hsy.php"
    payload = {
        "action": "user",
        "app": "hsywx",
        "appkey": APP_KEY,
        "merchant_id": 2,
        "method": "qiandao",
        "username": user,
        "version": 4
    }
    payload['sign'] = generate_sign(payload, SECRET_KEY)
    headers = {
        "Host": "www.52bjy.com",
        "Connection": "keep-alive",
        "xweb_xhr": "1",
        "EnvConnection": "test",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://servicewechat.com/wxadd84841bd31a665/114/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    try:
        # 关键修正：使用 GET 方法和 params 参数
        res = requests.get(url, headers=headers, params=payload, timeout=10)
        res.raise_for_status()
        response_json = res.json()
        print(f"签到成功: {response_json.get('message', '无消息')}")
        return response_json
    except requests.exceptions.RequestException as e:
        print(f"签到失败: {e}")
        return None

def main():
    get_announcement()
    print(f"回收猿每日签到")

    users = os.getenv('hsytoken')
    if not users:
        print(f"请将用户名填入环境变量hsytoken，多账号&分割，或新建变量")
    else:
        users = users.split('&')
        print(f"找到了:{len(users)}个账号")
        for user in users:
            print(f"账号：:{user}开始任务")
            query(user)
            time.sleep(3)
            sign_in(user)



if __name__ == "__main__":
    main()