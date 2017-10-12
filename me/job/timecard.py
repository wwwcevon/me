# -*- coding: utf-8 -*-
import datetime
import mysql.connector
import requests
import json


class Timecard:

    @staticmethod
    def today(user_id=19):
        cnx = mysql.connector.connect(user='root', password='qianka',
                                      host='172.16.3.250',
                                      database='oa')
        cursor = cnx.cursor()
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        query = """SELECT clock_in FROM `time_card_log`
 WHERE user_id=%s AND date='%s' """ % (user_id, date)
        cursor.execute(query)
        for (clock_in,) in cursor:
            clock_in = datetime.datetime.strptime(clock_in, '%H:%M:%S')
            clock_out = clock_in + datetime.timedelta(hours=9)
            print(clock_out.strftime('%H:%M:%S'))
        cursor.close()
        cnx.close()

    @staticmethod
    def notify():
        api_url = [
            'https://oapi.dingtalk.com/robot/send?access_token=ba08001b38a6af724138569396eebb45fd6967884868f490787fea743ddd34ac',
            'https://oapi.dingtalk.com/robot/send?access_token=640dba2a6afa5f500a67f994c20263f41441040b5566974c52f7a0419e2d4942'
        ]
        user_ids = {
            13: ['18616749402',0],
            16: ['15996316757',0],
            19: ['13162929931',0],
            31: ['18616930697',0],
            51: ['15901611079',0],
            18: ['18501620205',1],
            64: ['18321427305',1],
            17: ['15277337765',0],
            32: ['13162929650',0],
            235: ['18717844230',0],
            231: ['18221331934',0],
            15: ['15316098561',0],
        }
        cnx = mysql.connector.connect(user='root', password='qianka',
                                      host='172.16.3.250',
                                      database='oa')
        cursor = cnx.cursor()
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        user_id_str = ','.join([str(_) for _ in user_ids])
        query = """SELECT user_id, clock_in FROM `time_card_log`
 WHERE user_id in (%s) AND date='%s' """ % (user_id_str, date)
        cursor.execute(query)
        for (user_id, clock_in,) in cursor:
            clock_in = datetime.datetime.strptime(clock_in, '%H:%M:%S')
            now = datetime.datetime.now()
            clock_out = datetime.datetime(
                year=now.year,
                month=now.month,
                day=now.day,
                hour=clock_in.hour+9,
                minute=clock_in.minute,
                second=clock_in.second)
            if  now.minute == clock_out.minute and now.hour == clock_out.hour:
                data = {
                    'msgtype': 'text',
                    'text': {
                        'content': '你可以下班啦～'
                    },
                    'at': {
                        'atMobiles': [user_ids[user_id][0]]
                    }
                }
                rs = requests.post(api_url[user_ids[user_id][1]], json=data)
                print('notify %s' % user_id)
        cursor.close()
        cnx.close()
