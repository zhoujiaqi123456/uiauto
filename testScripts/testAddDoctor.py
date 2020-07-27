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
from pageObjects.DoctorManagePage import DoctorManagePage
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from util.Log import *
from config.VarConfig import *
from config.accounts import *
from config.server_info import *

class TestAddDoctor(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    @classmethod
    def setUpClass(cls) -> None:
        TestAddDoctor.browser = webdriver.Chrome()
        TestAddDoctor.browser.maximize_window()
        logger.info("开始登陆...")
        TestAddDoctor.browser.get(loginpageUrl)
        TestAddDoctor.login_cookie = LoginAction.login(account, password, TestAddDoctor.browser)

    @classmethod
    def tearDownClass(cls) -> None:
        TestAddDoctor.browser.quit()


    def test_AddDoctor(self):
        logger.info("开始执行添加医生脚本...")
        #获取是否执行列
        isExecuteUser = TestAddDoctor.excelObj.get_col_values(adddoctor_isExecute, sheet_name='添加医师')
        pc = ParseConfigFile()
        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            if i == 'Y':
                doctorName = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_name)
                doctorIDNumber = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_IdNumber)
                doctorNumber = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_Number)
                doctorPhoneNumber = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_phoneNumber)
                doctorEmail = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_email)
                doctorRemarks = TestAddDoctor.excelObj.get_cell_value(idx + 2, doctor_remarks)
                logger.info("执行测试数据：%s,%s,%s,%s,%s,%s" % (doctorName, doctorIDNumber, doctorNumber, doctorPhoneNumber ,doctorEmail ,doctorRemarks))
                try:
                    TestAddDoctor.browser.get(pc.getUrl('AddDoctorPageUrl'))
                    logger.info('启动浏览器，访问添加医生页面...')
                    # 如果在在医生管理列表查询刚添加的医生，则通过测试用例，如果没找到该医生则测试用例未通过
                    queryDoctor = QueryDoctorAction(TestAddDoctor.browser)
                    # queryDoctor.QueryDoctorAutoAction()
                    queryDoctor.QueryDoctorAction(doctorName, doctorIDNumber, doctorNumber, doctorPhoneNumber, doctorEmail, doctorRemarks)
                    doctormanagerpage = DoctorManagePage(TestAddDoctor.browser)
                    logger.info('在医生管理列表查询刚添加的医生')
                    try:
                        self.assertEqual(doctormanagerpage.doctorQueryInfoTd().text, doctorNumber, True)
                        # doctorNumberAuto = AddDoctorAction(TestAddDoctor.browser).get_doctorNumberAuto()
                        # self.assertEqual(doctormanagerpage.doctorQueryInfoTd().text, doctorNumberAuto, True)
                        logger.info('在医生管理列表查询到刚添加的医生，成功,用例通过')
                        TestAddDoctor.excelObj.write_cell_value(idx + 2, adddoctor_testResult, 'success', 'green')
                        TestAddDoctor.excelObj.write_cell_value(idx + 2, adddoctor_time, str(round((time.time() - start_time)/1000, 2)) + 's')

                    except Exception as e:
                        # self.assertTrue(1 == 2)
                        logger.debug('在医生管理列表查询不到刚添加的医生，失败，用例不通过')
                        TestAddDoctor.excelObj.write_cell_value(idx + 2, adddoctor_testResult, 'fail', 'red')
                        TestAddDoctor.excelObj.write_cell_value(idx + 2, adddoctor_time, str(time.time()-start_time)+'s', 'red')
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
    testsuit.addTest(TestAddDoctor("test_AddDoctor"))
    # 运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)
    print(str(round((time.time() - start_time) / 1000, 2)) + 's')