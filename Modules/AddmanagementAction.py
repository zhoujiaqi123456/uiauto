# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.AddmanagementPage import AddmanagementPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class AddmanagementAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.Addmanagement = AddmanagementPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddmanagementOptions = self.parseCF.getItemsSection('AddmanagementPage')
        logger.info("Addmanagement..")

    def AddmanagementAction(self, title, time1,time2, reachedAmount, discountAmount):
        '''
        读取传参数据操作
        :param
        :return:
        '''


        #若参数为文本框选择这个，否则删除
        self.Addmanagement.titleInput().send_keys(title)




        #参数为单下拉框 选择这个，否则删除

        #
        # self.driver.find_element_by_xpath('//*[@id="scene"]/div/div/div').click()
        # self.Addmanagement.userIdsInput().send_keys('/html/body/div[3]/div/div/div/ul[1]')

        sceneSelector = self.AddmanagementOptions['AddmanagementPage.sceneSelector'.lower()].split('>')[1]
        sceneOptions = self.AddmanagementOptions['AddmanagementPage.sceneOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, sceneSelector, sceneOptions)


        #参数为单下拉框 选择这个，否则删除
        typeSelector = self.AddmanagementOptions['AddmanagementPage.typeSelector'.lower()].split('>')[1]
        typeOptions = self.AddmanagementOptions['AddmanagementPage.typeOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, typeSelector, typeOptions)



        #若参数为文本框选择这个，否则删除
        self.Addmanagement.timeInput1().send_keys(time1)
        self.Addmanagement.timeInput2().send_keys(time2)

        # #参数为单下拉框 选择这个，否则删除
        # timeSelector = self.AddmanagementOptions['AddmanagementPage.timeSelector'.lower()].split('>')[1]
        # timeOptions = self.AddmanagementOptions['AddmanagementPage.timeOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.Addmanagement.reachedAmountInput().send_keys(reachedAmount)


        #若参数为文本框选择这个，否则删除
        self.Addmanagement.discountAmountInput().send_keys(discountAmount)

        userIdsSelector = self.AddmanagementOptions['AddmanagementPage.userIdsSelector'.lower()].split('>')[1]
        userIdsOptions = self.AddmanagementOptions['AddmanagementPage.userIdsOptions'.lower()].split('>')[1]
        SelectorUtils().selector_choose(self.driver, userIdsSelector, userIdsOptions)


        # logging.info("--滑到页面底部--")
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execute_script(js)
        #
        # self.driver.find_element_by_xpath('//*[@id="userIds"]/div/div').click()
        # logging.info("--滑到页面底部--")
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execute_script(js)
        #
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[11]').click()
        #
