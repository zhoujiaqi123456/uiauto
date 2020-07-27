# -*- coding: utf-8 -*-
# @Time : 2020-07-20 12:21
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: DoctorManagePage.py
# @Project : MDT_UIAutomation
# @Software: PyCharm
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *
from Modules.LoginAction import LoginAction

class DoctorManagePage:

    #获取DoctorManagePage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.QueryDoctorOptions = self.parseCF.getItemsSection('DoctorManagePage')

    def doctorNumberInput(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorNumberInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorNameInput(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element

    def doctorDepartmentInput(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorDepartmentInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorTitleSelector(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorTitleSelector'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorTitleOptions(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorTitleOptions'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorPhoneNumberInput(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorPhoneNumberInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorQueryButton(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorQueryButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorQueryInfoTd(self):
        try:
            locateType, locateExpression = self.QueryDoctorOptions['DoctorManagePage.doctorQueryInfoTd'.lower()].split('>')
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
    LoginAction.login('yinchengjie', '123456', browser, "http://47.96.186.244:8020/doctorControl/doctorControlList")
    doctor_manager_page = DoctorManagePage(browser)
    browser.implicitly_wait(1)
    doctor_manager_page.doctorNameInput().send_keys('123')
    # browser.quit()