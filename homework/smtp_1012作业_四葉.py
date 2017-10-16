#-*-coding:utf-8-*-
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib
from homework.htmlreport_unittest_HttpRequest import HtmlReporter
import time
import logging

class SmtpTest:
    def __init__(self):
        pass

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def MailMessage(self,attachmentfile):
        msg=MIMEMultipart()
        msg['From'] = self._format_addr('四葉 <1076168822@qq.com>')
        # formataddr(Header("四葉", 'utf-8').encode(),"<1076168822@qq.com>")
        msg['To'] = self._format_addr('美华华 <204893985@qq.com>')
        # formataddr(Header("美华华", 'utf-8').encode(),"1076168822@qq.com")
        subject="四葉"+time.strftime('%Y-%m-%d_%H_%M')+"生成的"+attachmentfile.split("2")[0]+"测试报告"
        msg['Subject'] = Header(subject, 'utf-8').encode()
        msg.attach(MIMEText('来自四葉的单元测试报告', 'plain', 'utf-8'))
        with open(attachmentfile,'rb') as f:
            attachment=MIMEBase('html','html',filename=attachmentfile)
            attachment.add_header('Content-Disposition', 'attachment', filename=attachmentfile)
            attachment.add_header('Content-ID', '<0>')
            attachment.add_header('X-Attachment-Id', '0')
            attachment.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(attachment)
            # 添加到MIMEMultipart:
            msg.attach(attachment)
        return msg

    def MailSend(self,attachmentfile):
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login("1076168822@qq.com", "dlbfutsgvlsxjgaj")
            s.sendmail("1076168822@qq.com", "204893985@qq.com>", self.MailMessage(attachmentfile).as_string())
            logging.info("发送成功")
        except smtplib.SMTPException as e:
            logging.error("发送失败Error: %s" % e)
        finally:
            s.quit()

reporter=HtmlReporter()
mail=SmtpTest()
mail.MailSend(reporter.CreateReporter())






