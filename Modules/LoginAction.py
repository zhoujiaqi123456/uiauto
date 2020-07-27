#coding=utf-8
from selenium.webdriver import ActionChains

from pageObjects.LoginPage import LoginPage
from util.Log import *
from selenium import webdriver

class LoginAction:
    def __init__(self):
        logger.info("login..")

    @staticmethod
    def login(username, password, browser, source_url=None):
        '''
        登陆，并返回token且跳转到source_url
        :param username:
        :param password:
        :param browser:
        :param source_url:
        :return:登陆token
        '''
        try:

            # browser.get("https://plogin.m.jd.com/user/login.action")
            page = LoginPage(browser)
            page.usernameInput().send_keys(username)
            page.passwordInput().send_keys(password)
            page.loginButton().click()
            # browser.implicitly_wait(1)

            while (1):
                # verify_code(browser)
                try:
                    # 这个条件不同情况下调用需要修改
                    browser.implicitly_wait(1)
                    # element = browser.find_element_by_xpath('// *[ @ class = "jcap_refresh"]')
                    element = browser.find_element_by_xpath('//*[@id="logo"]')
                    if(element):
                        logger.info("登录成功！")
                    token = browser.execute_script('return localStorage.getItem("Access-Token");')
                    if source_url:
                        browser.get(source_url)
                    return token
                except Exception as e:
                    logger.info("登录失败！")
                    # get the session cookie  
                    # cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
                    # print cookie  
                    # cookiestr = ';'.join(cookie)
                    browser.implicitly_wait(1)
                    token = browser.execute_script('return localStorage.getItem("Access-Token");')
                    if source_url:
                        browser.get(source_url)
                    return token

        except Exception as e:
            logger.error(e)
            raise e

    # 退出登录
    def logout(self, browser):
        # 页面右上角账户悬停出现下拉框
        viewBox = browser.find_element_by_xpath('//*[@id="app"]/section/section/div/header[2]/div/div')
        ActionChains(browser).move_to_element(viewBox).perform()
        browser.find_element_by_xpath('/html/body/div[3]/div/div/ul/li').click()

if __name__=="__main__":

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get("http://47.96.186.244:8020/user/login")
    browser.delete_all_cookies()
    token = LoginAction.login('yinchengjie', '123456', browser, "http://47.96.186.244:8020/dashboard")
    # print(cookie)
    # for key, value in cookie.items():
    #     print(key, value)
    print(token)
    browser.quit()