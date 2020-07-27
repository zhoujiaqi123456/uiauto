# -*- coding: utf-8 -*-
# @Time : 2020-07-20 14:45
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: testAddDoctor.py
# @Project : MDT_UIAutomation
# @Software: PyCharm
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from Modules.LoginAction import LoginAction
from Modules.QueryDoctorAction import QueryDoctorAction
from Modules.AddDoctorAction import AddDoctorAction
from pageObjects.DoctorManagePage import DoctorManagePage
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *
from config.accounts import *
from config.server_info import *

class TestAddDoctorAuto(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        TestAddDoctorAuto.browser = webdriver.Chrome()
        TestAddDoctorAuto.browser.maximize_window()
        logger.info("开始登陆...")
        TestAddDoctorAuto.browser.get(loginpageUrl)
        TestAddDoctorAuto.login_cookie = LoginAction.login(account, password, TestAddDoctorAuto.browser)

    @classmethod
    def tearDownClass(cls) -> None:
        TestAddDoctorAuto.browser.quit()


    def test_AddDoctorAuto(self):
        logger.info("开始执行添加医生脚本...")
        #获取是否执行列
        pc = ParseConfigFile()
        scriptnum = 2;
        for i in range(0,scriptnum):
            start_time = time.time()
            logger.info("执行测试数据：")
            try:
                TestAddDoctorAuto.browser.get(pc.getUrl('AddDoctorPageUrl'))
                logger.info('启动浏览器，访问添加医生页面...')
                # 如果在在医生管理列表查询刚添加的医生，则通过测试用例，如果没找到该医生则测试用例未通过
                queryDoctor = QueryDoctorAction(TestAddDoctorAuto.browser)
                queryDoctor.QueryDoctorAutoAction()
                doctormanagerpage = DoctorManagePage(TestAddDoctorAuto.browser)
                logger.info('在医生管理列表查询刚添加的医生')
                try:
                    doctorNumberAuto = AddDoctorAction(TestAddDoctorAuto.browser).get_doctorNumberAuto()
                    self.assertEqual(doctormanagerpage.doctorQueryInfoTd().text, doctorNumberAuto, True)
                    logger.info('在医生管理列表查询到刚添加的医生，成功,用例通过')

                except Exception as e:
                    # self.assertTrue(1 == 2)
                    logger.debug('在医生管理列表查询不到刚添加的医生，失败，用例不通过')
                    raise e

            except ElementNotVisibleException as e:
                logger.error("数据问题，元素没有找到..")

            except NoSuchElementException as e:
                logger.error("数据问题..重试")

            except Exception as e:
                logger.error(e)
                raise e


if __name__ == '__main__':
    # unittest.main()

    # 通过多个测试集合组成一个测试套
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestAddDoctorAuto("test_AddDoctorAuto"))
    # 运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)
    print(str(round((time.time() - start_time) / 1000, 2)) + 's')