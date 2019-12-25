import sys
import time

sys.path.append('./apitest')
sys.path.append('./db_operate')
from apiManage.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader

# 指定测试用例为当前文件夹下的 apiAutoTest 目录
test_dir = './apiAutoTest'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    runner.run(testsuit)
    fp.close()
