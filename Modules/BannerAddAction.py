# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.BannerAddPage import BannerAddPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class BannerAddAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.BannerAdd = BannerAddPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.BannerAddOptions = self.parseCF.getItemsSection('BannerAddPage')
        logger.info("BannerAdd..")

    def BannerAddAction(self,pic, title, action, url
):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.bannerAdd.picInput().send_keys(pic)

        #参数为单下拉框 选择这个，否则删除
        picSelector = self.BannerAddOptions['BannerAddPage.picSelector'.lower()].split('>')[1]
        picOptions = self.BannerAddOptions['BannerAddPage.picOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.bannerAdd.titleInput().send_keys(title)

        #参数为单下拉框 选择这个，否则删除
        titleSelector = self.BannerAddOptions['BannerAddPage.titleSelector'.lower()].split('>')[1]
        titleOptions = self.BannerAddOptions['BannerAddPage.titleOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.bannerAdd.actionInput().send_keys(action)

        #参数为单下拉框 选择这个，否则删除
        actionSelector = self.BannerAddOptions['BannerAddPage.actionSelector'.lower()].split('>')[1]
        actionOptions = self.BannerAddOptions['BannerAddPage.actionOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.bannerAdd.urlInput().send_keys(url)

        #参数为单下拉框 选择这个，否则删除
        urlSelector = self.BannerAddOptions['BannerAddPage.urlSelector'.lower()].split('>')[1]
        urlOptions = self.BannerAddOptions['BannerAddPage.urlOptions'.lower()].split('>')[1]

