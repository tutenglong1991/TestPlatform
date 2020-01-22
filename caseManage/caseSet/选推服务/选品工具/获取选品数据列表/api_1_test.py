import unittest
import json
import os
import sys
from apiManage import requestMain

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义临时(程序退出即失效)搜索路径的优先顺序，序号从0开始，表示最大优先级
sys.path.insert(0, parentdir)


class LoginEventTest(unittest.TestCase):
    '''  登录接口测试 '''
    def setUp(self):
        self.run_request = requestMain.runApiMain()
        self.login_url = 'https://testpassport.rabbitpre.com/api/sso/login'
        print('--------执行用例前执行了setUp方法-----------------')

    def tearDown(self):
        # print(self.result)
        print('--------------执行用例后执行了tearDown方法--------------')
        print(self.result)

    def test_login_null_account_and_null_password(self):
        '''参数为空'''
        login_playload = {"account": "", "password": ""}
        login_res = self.run_request.run_main(self.login_url, 'POST', login_playload)
        self.result = json.loads(login_res.text)
        self.assertEqual(self.result['code'],'10010')
        self.assertEqual(self.result["msg"], "请输入账号")


if __name__ == '__main__':
    unittest.main()
