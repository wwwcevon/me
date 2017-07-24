# -*- coding: utf-8 -*-
import datetime
import mysql.connector


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
