import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


def send_email(con="你好！"):
    _user = "15999543812@163.com"
    _pwd = "nickliqian2017"
    _to = "419845955@qq.com"

    # 使用MIMEText构造符合smtp协议的header及body
    msg = MIMEMultipart('related')
    subject = "以下是今天的报表，请查收！--" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # # msgRoot['From'] = Header("菜鸟教程", 'utf-8')
    msg["Subject"] = subject
    msg["From"] = _user
    msg["To"] = _to

    # 可供选择的内容
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p>一小时采集趋势</p>
    <p><img src="cid:image1"></p>
    """ + con
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # 指定图片为当前目录
    fp = open('result.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    s = smtplib.SMTP("smtp.163.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)  # 登陆服务器
    s.sendmail(_user, _to, msg.as_string())  # 发送邮件
    s.close()


def deal_data():
    df = pd.read_csv("./count.csv", names=["time", "total"], encoding="utf-8")
    df = df[-60:]
    tx = np.array(df['time'])
    ty = np.array(df['total'])
    # 两个图画一起
    plt.figure('data & model')
    plt.plot(tx, ty, 'k', lw=3)
    # 将当前figure的图保存到文件result.png
    plt.savefig('result.png')
    # 一定要加上这句才能让画好的图显示在屏幕上
    # plt.show()
    s = ""
    for i in df.split("\n"):
        a = "<li>" + i + "</li>"
        s += a
    return s


def check():
    df = deal_data()
    while True:
        try:
            send_email(con=df)
            break
        except smtplib.SMTPDataError as e:
            if isinstance(e, smtplib.SMTPSenderRefused):
                pass
            elif isinstance(e, smtplib.SMTPDataError):
                pass
            else:
                raise e
        time.sleep(20)


def main():
    s = deal_data()


if __name__ == '__main__':
    main()
