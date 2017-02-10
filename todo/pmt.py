# -*- coding: utf-8 -*-
import requests
from datetime import datetime


class PMT:
    MY_USERNAME = 'cai.ziwen'
    engineers = []
    assignments = []
    tasks = []
    my_id = None

    def fetch_all(self):
        url = 'http://pmt.corp.qianka.com/api/schedule/engineers-{}-{}'
        today = datetime.now().strftime('%Y%m%d')
        url = url.format(today, today)
        rs = requests.get(url).json()['payload']
        self.engineers = rs['engineers']
        self.assignments = rs['assignments']
        self.tasks = rs['tasks']

    @property
    def myid(self):
        if self.my_id is not None:
            return self.my_id
        if self.engineers == []:
            self.fetch_all()
        for e_id, e in self.engineers.items():
            if e['username'] == self.MY_USERNAME:
                self.my_id = e_id
                return e_id
        return None

    @property
    def my_tasks(self):
        if self.assignments == []:
            self.fetch_all()
        my_tasks= []
        for a in self.assignments:
            if int(a['engineer']['id']) == int(self.myid):
                my_tasks += [_['id'] for _ in a['tasks']]

        return [self.tasks[str(_)]['title'] for _ in my_tasks]

if __name__ == '__main__':
    pmt = PMT()
    for _ in pmt.my_tasks:
        print(_)
