import unittest
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common import desired_capabilities

from testScripts import testZqbLogin
from Modules.AddmanagementAction import AddmanagementAction

class TestAddmanagement(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:


        # TestAddProduct.browser = webdriver.Chrome()
        # TestAddProduct.browser.maximize_window()
        # logging.info("开始登陆...")
        #
        # login = testZqbLogin.TestLogin()
        # login.login_without_qr(TestAddProduct.browser)

    def testAddmanagementPage(self):
        # driver = webdriver.Chrome()
        driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        current_window = driver.current_window_handle
        login = testZqbLogin.TestLogin()
        login.login_without_qr(driver)



        # 页面中点击某个链接会弹出一个新的窗口，这样要去操作新窗口中的元素，这时就需要主机切换到新窗口进行操作。
        # 定位到新开页面的句柄
        handles =driver.window_handles
        for handle in handles:
            if handle == current_window:
                continue
            driver.switch_to.window(handle)

        #点击优惠券管理 菜单

        driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[5]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[5]/ul/li[1]').click()
        #点击新增 按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[3]/div/div/div/div/div[2]/div/div/button').click()



        #添加优惠券
        title='优惠券名称'
        time1='2020-11-19'
        time2 = '2020-11-20'
        reachedAmount='4980.00'
        discountAmount='1980.00'
        AddmanagementAction(driver).AddmanagementAction(title, time1,time2, reachedAmount, discountAmount)








