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


    def test_login_correct_account_and_correct_password(self):
        '''正确的用户名和密码'''
        # 需注意兼容同一个账号登录过于频繁可能需要输入图片中的校验码或者一小时后再输入
        login_playload = {"account": "13944444004", "password": "123456"}
        login_res = self.run_request.run_main(self.login_url, 'POST', login_playload)
        self.result = json.loads(login_res.text)
        self.assertEqual(self.result['code'],'200')

    def test_login_correct_account_but_wrong_password(self):
        '''正确的用户名，错误密码'''
        login_playload = {"account": "13944444004", "password": "1346874547afsd"}
        login_res = self.run_request.run_main(self.login_url, 'POST', login_playload)
        self.result = json.loads(login_res.text)
        self.assertEqual(self.result["code"],"10021")
        self.assertEqual(self.result["msg"],"登录密码错误")


if __name__ == '__main__':
    unittest.main()
