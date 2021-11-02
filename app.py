import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):         
##    if  re.match(".*笑死.*",event.message.text):
##          line_bot_api.reply_message(
##              event.reply_token,
##              TextSendMessage(text='笑死'))

    if  re.match(".*好想喝酒.*",event.message.text):   ##########  好想喝酒
        
        if event.source.user_id == alice:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='只與你又來了'))
              
        if event.source.user_id == sandy:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='小心計時器'))
              
        if event.source.user_id == han:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='亂講  你又不是只與'))

    if  re.match("宏匯廣場",event.message.text):   ##########  宏匯廣場
        
        if event.source.user_id == alice:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='這是一個悲慘的故事'))
              
        if event.source.user_id == sandy:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='你還敢提?'))
              
        if event.source.user_id == han:
              line_bot_api.reply_message(
                  event.reply_token,
                  TextSendMessage(text='弄得全身濕 辛苦你了'))

    if  re.match(".*幹.*",event.message.text):  ######    幹
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='噓 不要亂罵髒話'))
        
    if  re.match("諧咖",event.message.text):  ######    諧咖
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='誰'))

    if  re.match(".*哇咧.*",event.message.text):  ######    哇咧
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='在哇咧我打破你的頭'))

    if  re.match(".*=.*=.*",event.message.text):  ######    哇咧
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='=='))
        



        
##    line_bot_api.reply_message(
##        event.reply_token,
##        TextSendMessage(text=event.message.text))
