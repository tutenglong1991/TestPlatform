#!/usr/bin/env python
# -*-coding:utf-8-*-

import requests
import json
import time


class runApiMain:

    def __init__(self):
        self.session = requests.session()

    # GBT平台登录处理
    def login_GBT(self):
        checkLogin_headers = {
            'Accept-Encoding': 'utf-8',
            'User-Agent': 'hemeilong',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        checkLogin_url = 'http://user.hqygou.com/login/index/checklogin'
        checkLogin_data = {'username': 'qiuchaoguang', 'password': '123456'}
        # 先调用户中心的登录接口
        self.run_main('post', url=checkLogin_url, req_data=checkLogin_data, headers=checkLogin_headers)
        # 再调php的http://www.trader-gb.com/base/login/login接口，生成cookie
        doLogin_headers = {
            'Accept-Encoding': 'utf-8',
            'User-Agent': 'hemeilong',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        php_get_cookie_url = 'http://www.trader-gb.com/base/login/login'
        self.run_main('get', url=php_get_cookie_url, headers=doLogin_headers)
        return self.session.cookies

    def send_post(self, url=None, post_data=None, headers=None):
        if headers['Content-Type'] == 'application/json':
            post_resp = self.session.post(url=url, json=post_data, headers=headers).text
        else:
            post_resp = self.session.post(url=url, data=post_data, headers=headers).text
        return post_resp

    def send_get(self, url=None, get_data=None, headers=None):
        get_resp = self.session.get(url=url, data=get_data, headers=headers).text
        return get_resp

    def run_main(self, method, url=None, req_data=None, headers=None):
        if method == 'get':
            response = self.send_get(url=url, get_data=req_data, headers=headers)
        elif method == 'post':
            response = self.send_post(url=url, post_data=req_data, headers=headers)
        return response


if __name__ == "__main__":
    rAm = runApiMain()
