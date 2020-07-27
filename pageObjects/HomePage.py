from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class HomePage:

    #获取HomePage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection('HomePage')

    def logoDiv(self):
        try:
            locateType, locateExpression = self.loginOptions['HomePage.logoDiv'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def accountDiv(self):
        try:
            locateType, locateExpression = self.loginOptions['HomePage.accountDiv'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def logoutLink(self):
        try:
            locateType, locateExpression = self.loginOptions['HomePage.logoutLink'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element



if __name__=="__main__":
    from selenium import webdriver
    import time

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)

    browser.get("http://47.96.186.244:8020/user/login")
    browser.maximize_window()
    login = LoginPage(browser)
    browser.implicitly_wait(1)
    login.usernameInput().send_keys("yinchengjie")
    login.passwordInput().send_keys("123456")
    login.loginButton().click()
    time.sleep(1)
    # get the session cookie  
    # cookie = [item["name"]+"="+item["value"] for item in browser.get_cookies()]
    token = browser.execute_script('return localStorage.getItem("Access-Token");')
    print(token)
    browser.quit()