import sys
import os
import time
from caseManage.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import json


class caseRunnerObj:

    def manualRunCase(self, **resp):
        for key in resp:
            dict_key = json.loads(key)
        case_list = dict_key['runningCase']
        print(case_list)
        # 根据前端传过来的用例参数属性查找到特定用例再添加到测试集合中
        for cases in case_list:
            project_id = cases['caseProName']
            module = cases['caseModule']
            api_id = cases['caseApiName']
            case_dir = '\\caseSet\\%s\\%s\\%s' % (project_id, module, api_id)
            base_dir = os.path.dirname(os.path.realpath(__file__))
            test_dir = base_dir + case_dir
            print(test_dir)
            testSuit = defaultTestLoader.discover(start_dir=test_dir, pattern='*_test.py', top_level_dir=base_dir)
        print(testSuit)
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = os.path.dirname(os.path.abspath(__file__)) + './report/' + now + '_result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='接口自动化测试',
                                description='运行环境：Python3, Sqlite3, Requests, unittest ')
        runner.run(testSuit)
        fp.close()
        return {'code': 200, 'msg': '执行完成'}


if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据
    caseRunner = caseRunnerObj()
