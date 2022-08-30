# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import smtplib
import threading
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "report"))
report_file = os.path.abspath(os.path.join(report_dir, "report.html"))


class Email:
    def __init__(self):
        global host, user, password, port, sender, title, receiver
        host = "smtp.163.com"
        user = "15623865453@163.com"
        password = "Zcx20180208"
        sender = "easyme2046@163.com"
        # get receiver list
        # self.value = localReadConfig.get_email("receiver")
        self.receiver = ["newlang@126.com"]
        # for n in str(self.value).split(","):
        #     self.receiver.append(n)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "Interface test Report" + " " + date
        self.msg = MIMEMultipart('related')

    def config_header(self):
        """
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        # define email template
        f = open(report_file, encoding="utf-8")
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'utf-8')
        self.msg.attach(content_plain)



    def send_email(self):
        self.config_header()
        self.config_content()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
        except Exception as ex:
            pass


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
    email.send_email()
