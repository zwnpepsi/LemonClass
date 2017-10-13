from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import logging

msg_1=MIMEText("这是一封来自四葉的测试邮件","plain","utf-8")
msg_1['From'] = "四葉"
msg_1['To'] = "1076168822@qq.com"
msg_1['Subject'] = Header(u'来自四葉的问候', 'utf-8').encode()   #四葉的单元测试报告

try:
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login("1076168822@qq.com","dlbfutsgvlsxjgaj")
    s.sendmail("1076168822@qq.com","1076168822@qq.com",msg_1.as_string())
    print("发送成功")
except s.SMTPEXCEPTION as e:
    print("发送失败")
    logging.error("发送失败")
finally:
    s.quit()