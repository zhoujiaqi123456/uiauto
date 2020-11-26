import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
class TestLogin():
    def test_login_withoupytestt_qr(self, account='admin', password='123456', login_url='http://manager.xiawakeji.com/#/login', account_id='account', password_id='password'):
        """
        :param browser: 浏览器
        :param account: 账号
        :param password: 密码
        :return: 0-发生错误；1-未发生错误
        """
        # browser=webdriver.Chrome()

        browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        # 获取浏览器当前标签页句柄
        current_window = browser.current_window_handle
        # 新开标签页打开网址

        js = 'window.open("' + login_url + '");'
        print(js)
        browser.execute_script(js)

        # 页面中点击某个链接会弹出一个新的窗口，这样要去操作新窗口中的元素，这时就需要主机切换到新窗口进行操作。
        # 定位到新开页面的句柄
        handles = browser.window_handles
        for handle in handles:
            if handle == current_window:
                continue
        browser.switch_to.window(handle)
        # print browser.title

        # browser.get(url)
        browser.maximize_window()

        # 输入账号
        account_input = browser.find_element_by_id(account_id)
        if account_input is None:
            print('未找到账号输入框')
            return 0
        account_input.click()
        account_input.send_keys(account)

        # 把 前端 密码框style="display: none;" 改成block
        container = browser.find_element_by_xpath('//form/div/div[3]/div/div[3]/div/div/span/span[1]')
        browser.execute_script("arguments[0].style.display = 'block';", container)

        password_input = browser.find_element_by_id(password_id)
        if password_input is None:
            print('未找到密码输入框')
            return 0
        password_input.click()
        password_input.send_keys(password)
        browser.implicitly_wait(5)

        # 点击登陆
        submit_array = browser.find_elements_by_class_name('ant-btn-lg')
        if len(submit_array) > 0:
            submit_array[0].click()

        else:
            print('未获取到提交按钮')
            return 0

        browser.find_element_by_xpath('//*[@id="app"]/div/div/header/div/a')
