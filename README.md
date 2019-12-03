# Pc-Remote-Controller-server

這是一個使用line-bot遠端控制電腦的code(server)



### **環境**
Python3.6

### **原理**
使用email的收發來達成遠端操控的目的，linebot發送郵件，再由電腦中的程式接收，執行命令

### **先備條件**

 1. 會將linebot發佈到伺服器(作者是使用Heroku)
 2. 擁有兩個email信箱(此處使用gmail範例)
 3. 會將伺服器和linebot連接(line-api)
 4. 作者很懶，上方不會請google

### **架設方法**

 1. 把它下載下來
 2. 打開app.py並修改下方的code

```python
line_bot_api = LineBotApi('輸入你自己的')
handler = WebhookHandler('輸入你自己的')
```

```python
def control(anss):
    gmail_user = '你的發信mail' # <------這裡
    gmail_password = '你的發信mail密碼' # <------這裡

    msg = MIMEText('cmd' + '`' + anss) #文章內容
    msg['Subject'] = 'line bot control'
    msg['From'] = gmail_user
    msg['To'] = '你的收信mail'# <------這裡

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # 不是使用gmail，465要改，改成多少自己google
    
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    print('Email sent!')
    content = '收到~~'
    return content
```
 3.發佈到Heroku
 4.如果還沒下載client端，左轉client端 https://github.com/luisbvcc1/Pc-Remote-Controller-client
### **使用方法**
這裡的code只有實現cmd指令控制電腦，如果要自己新增功能，依樣畫葫蘆就可以了~~

 1. 打開你的client端
 2. 對你的line機器人發:**cmd=你要的指令**
 3. 10秒內如果沒反應，那就看下方的問題解決

### **問題排除**

 1. **gmail不給登入授權:**
可以參考這篇文章，蠻清楚的
https://blog.csdn.net/qianghaohao/article/details/79331895
 2. **line串接的問題**
自行排除，我懶得的打XD
 3. **自己改過code，噴錯**
自己debug
