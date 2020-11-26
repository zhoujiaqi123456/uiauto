# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.AddlistPage import AddlistPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class AddlistAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.Addlist = AddlistPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddlistOptions = self.parseCF.getItemsSection('AddlistPage')
        logger.info("Addlist..")

    def AddlistAction(self,account, name, roleId
):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.Addlist.accountInput().send_keys(account)

        #参数为单下拉框 选择这个，否则删除
        AccountSelectorSelector = self.AddlistOptions['AddlistPage.AccountSelectorSelector'.lower()].split('>')[1]
        AccountOptionsOptions = self.AddlistOptions['AddlistPage.AccountOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.Addlist.nameInput().send_keys(name)

        #参数为单下拉框 选择这个，否则删除
        NameSelectorSelector = self.AddlistOptions['AddlistPage.NameSelectorSelector'.lower()].split('>')[1]
        NameOptionsOptions = self.AddlistOptions['AddlistPage.NameOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.Addlist.roleIdInput().send_keys(roleId)

        #参数为单下拉框 选择这个，否则删除
        RoleIdSelectorSelector = self.AddlistOptions['AddlistPage.RoleIdSelectorSelector'.lower()].split('>')[1]
        RoleIdOptionsOptions = self.AddlistOptions['AddlistPage.RoleIdOptionsOptions'.lower()].split('>')[1]

