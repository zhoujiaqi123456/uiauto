#coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

from Modules.LoginAction import LoginAction
from pageObjects.HomePage import HomePage
from util.ObjectMap import getElement
from util.ParseConfigurationFile import ParseConfigFile
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from util.Log import *
from config.server_info import *



class TestLogin(unittest.TestCase):

    excelObj = ParseExcel(dataFilePath)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


    def test_Login(self):
        logger.info("开始执行登录脚本...")
        #获取是否执行列
        isExecuteUser = TestLogin.excelObj.get_col_values(login_isExecute)
        for idx, i in enumerate(isExecuteUser[1:]):
            start_time = time.time()
            if i == 'Y':
                username = TestLogin.excelObj.get_cell_value(idx + 2, acount_username)
                password = TestLogin.excelObj.get_cell_value(idx + 2, acount_password)
                logger.info("执行测试数据：%s,%s" % (username, password))
                try:
                    options = webdriver.ChromeOptions()
                    browser = webdriver.Chrome(options=options)
                    browser.maximize_window()
                    browser.get(loginpageUrl)
                    logger.info('启动浏览器，访问登录页面...')
                    LoginAction.login(username, password, browser)
                    logger.info('登录操作执行...')
                    try:
                        # browser.implicitly_wait(5)       # 如果在首页页面找到MDT管理系统logo，则通过测试用例，如果没找到该logo则测试用例未通过
                        homepage = HomePage(browser)
                        self.assertIs(homepage.logoDiv().is_displayed(), True)
                        logger.info('在首页页面找【MDT管理系统】logo')
                    except Exception as e:
                        # self.assertTrue(1 == 2)
                        logger.debug('在首页页面找不到【MDT管理系统】logo，失败，用例不通过')
                        TestLogin.excelObj.write_cell_value(idx + 2, login_testResult, 'fail', 'red')
                        TestLogin.excelObj.write_cell_value(idx + 2, login_time, str(time.time()-start_time)+'s', 'red')
                        raise e

                    else:
                        logger.info('在首页页面找到【MDT管理系统】logo，成功,用例通过')
                        TestLogin.excelObj.write_cell_value(idx + 2, login_testResult, 'success', 'green')
                        TestLogin.excelObj.write_cell_value(idx + 2, login_time, str(round((time.time() - start_time)/1000, 2)) + 's')

                except ElementNotVisibleException as e:

                    logger.error("数据问题，元素没有找到..")

                except NoSuchElementException as e:

                    logger.error("数据问题..重试")

                except Exception as e:

                    logger.error(e)

                    raise e
            else:
                continue

if __name__=="__main__":
    # unittest.main()

    #通过多个测试集合组成一个测试套
    testsuit = unittest.TestSuite()
    testsuit.addTest(TestLogin("test_Login"))
    #运行测试套，verbosity=2说明输出每个测试用例运行的详细信息
    unittest.TextTestRunner(verbosity=2).run(testsuit)
    print(str(round((time.time() - start_time)/1000, 2)) + 's')


