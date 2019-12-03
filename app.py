import requests
import re
import random
from bs4 import BeautifulSoup
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

line_bot_api = LineBotApi('輸入你自己的')
handler = WebhookHandler('輸入你自己的')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

def control(anss):
    gmail_user = '你的發信mail'
    gmail_password = '你的發信mail密碼' # your gmail password

    msg = MIMEText('cmd' + '`' + anss) #文章內容
    msg['Subject'] = 'line bot control'
    msg['From'] = gmail_user
    msg['To'] = '你的收信mail'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    print('Email sent!')
    content = '收到~~'
    return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    while True:
        replyy = (event.message.text).split('=')
        ans = replyy[1]
        if replyy[0] == "cmd":
            content = control(ans)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=content))
            break
        else:
            break
    return 0

if __name__ == "__main__":
    app.run()
