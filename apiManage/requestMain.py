#!/usr/bin/env python
# -*-coding:utf-8-*-

import requests
import json

class runApiMain:

    def __init__(self):
        self.s = requests.session()
    
    def send_post(self, url, data):
        # param_data = json.dump(data)
        resp = self.s.post(url=url, data=data)
        return resp.text

    def send_get(self, url, data):
        resp = self.s.get(url=url, data=data)
        return resp.text

    def run_Main(self, method='get', url=None, data=None):
        if method == 'get':
            resp = self.send_get(url, data)
        elif method == 'post':
            resp = self.send_post(url, data)
        return resp

if __name__ == "__main__":
    rAm = runApiMain()