import config as Config
from linebot import LineBotApi
from linebot.models import TextSendMessage

class LineBotApiClass:
    #設定値取得
    global line_bot_api = LineBotApi('')

    def __init__(self):
        Config.read_ini()
        nonlocal line_bot_api
        line_bot_api = LineBotApi(Config.dic_api_condig['channelaccesstoken'])

    def send_message(self, message):
        messages = TextSendMessage(text=message)
        line_bot_api.push_message(Config.dic_api_condig['userid'], messages=messages)