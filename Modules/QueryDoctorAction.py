# -*- coding: utf-8 -*-
# @Time : 2020-07-20 12:12
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: QueryDoctorAction.py
# @Project : MDT_UIAutomation
# @Software: PyCharm
import time
from selenium import webdriver
from pageObjects.DoctorManagePage import DoctorManagePage
from config.server_info import *
from util.Log import *
from Modules.LoginAction import LoginAction
from Modules.AddDoctorAction import AddDoctorAction
from util.ParseConfigurationFile import ParseConfigFile
class QueryDoctorAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.QueryDoctor = DoctorManagePage(self.driver)
        self.parseCF = ParseConfigFile()
        self.QueryDoctorOptions = self.parseCF.getItemsSection('DoctorManagePage')
        logger.info("QueryDoctor..")

    def QueryDoctorAutoAction(self):
        '''
        添加随机数据查询医生
        '''
        AddDoctorAction(self.driver).addDoctorAutoAction()
        doctor_Number = AddDoctorAction(self.driver).get_doctorNumberAuto()
        try:
            time.sleep(2)
            if self.driver.current_url != AddDoctorPageUrl:
                logger.info('添加医师成功')
                self.driver.get(eval('doctorControlListPageUrl'))
                self.QueryDoctor.doctorNumberInput().send_keys(doctor_Number)
                self.QueryDoctor.doctorQueryButton().click()
            else:
                logger.info("添加医师失败")
                os.system('pause')
        except Exception as e:
            logger.error(e)
            raise e

    def QueryDoctorAction(self, doctor_name, doctor_IdNumber, doctor_Number, doctor_phoneNumber, doctor_email, doctor_remarks):
        '''

        :param doctor_name: 医生名字
        :param doctor_IdNumber: 医生身份证号
        :param doctor_Number: 医生编号
        :param doctor_phoneNumber: 医生手机号
        :param doctor_email: 医生邮箱
        :param doctor_remarks: 备注
        :return:
        '''
        AddDoctorAction(self.driver).addDoctorAction(doctor_name, doctor_IdNumber, doctor_Number, doctor_phoneNumber,
                                                     doctor_email, doctor_remarks)
        # try:
        #     time.sleep(2)
        #     if self.driver.current_url != AddDoctorPageUrl:
        #         logger.info('添加医师成功')
        self.driver.get(eval('doctorControlListPageUrl'))
        self.QueryDoctor.doctorNumberInput().send_keys(doctor_Number)
        self.QueryDoctor.doctorQueryButton().click()
        #     else:
        #         logger.info("添加医师失败")
        #         os.system('pause')
        # except Exception as e:
        #     logger.error(e)
        #     raise e

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get("http://47.96.186.244:8020/user/login")
    browser.maximize_window()
    LoginAction.login('yinchengjie', '123456', browser)
    url2 = r'http://47.96.186.244:8020/doctorControl/doctorControlList/add'
    time.sleep(1)
    browser.get(eval('url2'))
    queryDoctor = QueryDoctorAction(browser)
    queryDoctor.QueryDoctorAutoAction()
    # queryDoctor.QueryDoctorAction('殷诚杰', '230221193508216435', 'ba5a6caa-b46a-11ea-bbc5-9a00177b1001', 18042450864, '616107804@qq.com', '无')

