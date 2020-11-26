import unittest
import random
from selenium import webdriver
from testScripts import testZqbLogin
from Modules.AddAction import AddAction

class TestAddProduct(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:


        # TestAddProduct.browser = webdriver.Chrome()
        # TestAddProduct.browser.maximize_window()
        # logging.info("开始登陆...")
        #
        # login = testZqbLogin.TestLogin()
        # login.login_without_qr(TestAddProduct.browser)

    def testAddProduct(self):
        driver = webdriver.Chrome()
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

        #点击商品管理 菜单

        driver.find_element_by_xpath('//*[@id="app"]/div/aside/ul/li[2]').click()
        #点击新增 按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[3]/div/div/div/div/div[2]/div/div/button').click()



        #添加商品
        productName='商品名称'+str(random.randint(1,1000))
        price='4980.00'
        deposit='1980.00'
        rental='1000.00'
        rentLimitPrice='5000.00'
        picture='/Users/zhehe/Downloads/ffc25492-0339-4403-af64-2552f8a2fc95.jpeg'
        productcontent='商品描述'+str(random.randint(1,1000))
        AddAction(driver).AddAction(productName, price, deposit, rental, rentLimitPrice,picture,productcontent)








