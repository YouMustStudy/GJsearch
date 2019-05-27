# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def send_mail(addr, text, binimage):
    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"

    senderAddr = "kimgw926@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = addr   # 받는 사람 email 주소.
    wd = "****************************"

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "GJSearch 검색결과!"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    HtmlPart = MIMEText(text, 'plain', _charset='UTF-8')

    ImagePart = MIMEImage(binimage)

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)
    msg.attach(ImagePart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, wd)
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()