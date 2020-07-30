# -*- coding: utf-8 -*-
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

    def addDoctorAction(self):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.AddDoctor.doctorNameInput().send_keys(doctor_name)

        #参数为单下拉框 选择这个，否则删除
        doctorNameSelector = self.AddDoctorOptions['AddDoctorPage.doctorNameSelector'.lower()].split('>')[1]
        doctorNameOptions = self.AddDoctorOptions['AddDoctorPage.doctorNameOptions'.lower()].split('>')[1]

