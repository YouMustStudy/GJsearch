#!/usr/bin/python
# coding=utf-8


import time
import telepot
from pprint import pprint
from datetime import date, datetime, timedelta
from XMLParse import make_companyList
from search_code import *
import noti


def replyAptData(user, sigun):
    print(user, sigun)
    res_list = make_companyList(cityList[sigun], "")
    msg = ''
    for com in res_list:
        r = com.getTeleString()
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '해당하는 데이터가 없습니다.' )

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('검색') and len(args)>1:
        print('try to 지역', args[1])
        replyAptData( chat_id, args[1] )
    elif text.startswith('지원'):
        print('try to 확인')
        noti.sendMessage(chat_id, '지원 도시 : 수원시, 성남시, 의정부시, 안양시, 부천시, 광명시, 평택시, 동두천시, 안산시, 고양시, 과천시, 구리시, 남양주시, 오산시, 시흥시, 군포시, 의왕시, 하남시, 용인시, 파주시, 이천시, 안성시, 김포시, 화성시, 광주시, 양주시, 포천시, 여주시, 연천군, 가평군, 양평군')
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n지역 [지역번호], 지원 중 하나의 명령을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)