import requests

# ====== 在这里填你的信息 ======
APP_ID = "你的AppID"
APP_SECRET = "你的AppSecret"
OPEN_ID = "你的OpenID"
TEMPLATE_ID = "你的TemplateID"

def get_access_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    return requests.get(url).json()["access_token"]

def send_message():
    token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={token}"
    data = {
        "touser": OPEN_ID,
        "template_id": TEMPLATE_ID,
        "data": {
            "date": {"value": "2026-06-11"},
            "weather": {"value": "晴 26℃"},
            "msg": {"value": "早安，今天也要加油！"}
        }
    }
    print(requests.post(url, json=data).json())

if __name__ == "__main__":
    send_message()
