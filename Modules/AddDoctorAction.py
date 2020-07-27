# -*- coding: utf-8 -*-
# @Time : 2020-07-15 11:08
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: AddDoctorAction.py
# @Project : MDT_UIAutomation
# @Software: PyCharm
import time
from selenium import webdriver
from pageObjects.AddDoctorPage import AddDoctorPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class AddDoctorAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.AddDoctor = AddDoctorPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddDoctorOptions = self.parseCF.getItemsSection('AddDoctorPage')
        logger.info("AddDoctor..")

    def addDoctorAction(self, doctor_name, doctor_IdNumber, doctor_Number, doctor_phoneNumber, doctor_email, doctor_remarks):
        '''
        读取传参数据操作
        :param doctor_name: 医生名称
        :param doctor_IdNumber: 医生身份证号
        :param doctor_Number: 医生编号
        :param doctor_phoneNumber: 医生手机号
        :param doctor_email: 医生邮箱
        :param doctor_remarks: 备注
        :return:
        '''
        self.AddDoctor.doctorNameInput().send_keys(doctor_name)
        doctorGenderSelector = self.AddDoctorOptions['AddDoctorPage.doctorGenderSelector'.lower()].split('>')[1]
        doctorGenderOptions = self.AddDoctorOptions['AddDoctorPage.doctorGenderOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorGenderSelector, doctorGenderOptions)
        self.AddDoctor.doctorIDNumberInput().send_keys(doctor_IdNumber)
        self.AddDoctor.doctorNumberInput().send_keys(doctor_Number)
        doctorTitleSelector = self.AddDoctorOptions['AddDoctorPage.doctorTitleSelector'.lower()].split('>')[1]
        doctorTitleOptions = self.AddDoctorOptions['AddDoctorPage.doctorTitleOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorTitleSelector, doctorTitleOptions)
        doctorDepartmentSelector = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentSelector'.lower()].split('>')[1]
        doctorDepartmentOptions = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorDepartmentSelector, doctorDepartmentOptions)
        self.AddDoctor.doctorPhoneNumberInput().send_keys(doctor_phoneNumber)
        self.AddDoctor.doctorEmailInput().send_keys(doctor_email)
        self.AddDoctor.doctorRemarksTextArea().send_keys(doctor_remarks)
        self.AddDoctor.doctorSubmitButton().click()
        time.sleep(2)



    #随机数据自动化方法
    def addDoctorAutoAction(self):
        '''
        添加医生随机数据操作
        :return: 医生编号
        '''
        self.AddDoctor.doctorNameInput().send_keys(RandomInfo.get_name())
        doctorGenderSelector = self.AddDoctorOptions['AddDoctorPage.doctorGenderSelector'.lower()].split('>')[1]
        doctorGenderOptions = self.AddDoctorOptions['AddDoctorPage.doctorGenderOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorGenderSelector, doctorGenderOptions)
        self.AddDoctor.doctorIDNumberInput().send_keys(RandomInfo.get_idnum())
        self.AddDoctor.doctorNumberInput().send_keys(RandomInfo.get_idnum())
        global  doctorNumberAuto
        doctorNumberAuto = self.AddDoctor.doctorNumberInput().get_attribute('value')
        doctorTitleSelector = self.AddDoctorOptions['AddDoctorPage.doctorTitleSelector'.lower()].split('>')[1]
        doctorTitleOptions = self.AddDoctorOptions['AddDoctorPage.doctorTitleOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorTitleSelector, doctorTitleOptions)
        doctorDepartmentSelector = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentSelector'.lower()].split('>')[1]
        doctorDepartmentOptions = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, doctorDepartmentSelector, doctorDepartmentOptions)
        self.AddDoctor.doctorPhoneNumberInput().send_keys(RandomInfo.get_tel())
        self.AddDoctor.doctorEmailInput().send_keys(RandomInfo.get_email())
        self.AddDoctor.doctorRemarksTextArea().send_keys("备注")
        self.AddDoctor.doctorSubmitButton().click()




    def get_doctorNumberAuto(self):
        print('医生编号' + doctorNumberAuto)
        return doctorNumberAuto


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get("http://47.96.186.244:8020/user/login")
    browser.maximize_window()
    token = LoginAction.login('yinchengjie', '123456', browser)
    url2 = r'http://47.96.186.244:8020/doctorControl/doctorControlList/add'
    time.sleep(1)
    browser.get(eval('url2'))
    time.sleep(3)
    addDoctor = AddDoctorAction(browser)
    addDoctor.addDoctorAutoAction()