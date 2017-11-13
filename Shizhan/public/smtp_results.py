#-*-coding:utf-8-*-
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib
import logging
import configparser
import os




class SmtpResults:
    def __init__(self,path):
        self.cf = configparser.ConfigParser()
        self.cf.read(path,encoding="utf-8")

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def smtpResults(self,attachmentfile):
        msg=MIMEMultipart()
        msg['From'] = self._format_addr(self.cf.get("EMAIL", "msg['From']"))
        # formataddr(Header("四葉", 'utf-8').encode(),"<1076168822@qq.com>")
        msg['To'] = self._format_addr(self.cf.get("EMAIL", "msg['To']"))
        # formataddr(Header("美华华", 'utf-8').encode(),"1076168822@qq.com")
        subject=self.cf.get("EMAIL", "subject")
        msg['Subject'] = Header(subject, 'utf-8').encode()
        msg.attach(MIMEText('来自四葉的单元测试报告', 'plain', 'utf-8'))
        with open(attachmentfile,'rb') as f:
            attachment=MIMEBase('html','html',filename=attachmentfile)
            attachment.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', os.path.split(os.path.realpath(attachmentfile))[1]))
            attachment.add_header('Content-ID', '<0>')
            attachment.add_header('X-Attachment-Id', '0')
            attachment.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(attachment)
            # 添加到MIMEMultipart:
            msg.attach(attachment)
        return msg

    def MailSend(self,attachmentfile):
        global s
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login("1076168822@qq.com", "ooizuperphhrjhhd")
            s.sendmail(self.cf.get("EMAIL", "msg_from"), self.cf.get("EMAIL", "msg_from"), self.smtpResults(attachmentfile).as_string())
            logging.info("发送成功")
        except smtplib.SMTPException as e:
            logging.error("发送失败Error: %s" % e)
        finally:
            s.quit()








