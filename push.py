import os
import requests

APP_ID = "wx4baca176cd4b4f17"
APP_SECRET = os.environ.get("WX_APP_SECRET")  # 从 GitHub Secret 读取
OPEN_ID = "oZmgn3d0JRbQqtvzfoA6ndvSwXW8"
TEMPLATE_ID = "7aY7BaHERkr8kGikDxHtKZCaLOy9f_3rPxOLbvELP6c"

def get_access_token():
    url = (
        f"https://api.weixin.qq.com/cgi-bin/token"
        f"?grant_type=client_credential"
        f"&appid={APP_ID}&secret={APP_SECRET}"
    )
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

    response = requests.post(url, json=data)
    print(response.json())

if __name__ == "__main__":
    send_message()
