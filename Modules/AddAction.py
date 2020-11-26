# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.AddPage import AddPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
from selenium.webdriver.support.ui import Select

class AddAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.Add = AddPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddOptions = self.parseCF.getItemsSection('AddPage')
        logger.info("Add..")

    def AddAction(self, productName, price, deposit, rental, rentLimitPrice,picture,productcontent
):
        '''
        读取传参数据操作
        :param
        :return:
        '''
        #
        # #若参数为文本框选择这个，否则删除
        # self.Add.accountInput().send_keys(account)
        #
        # #参数为单下拉框 选择这个，否则删除
        # AccountSelectorSelector = self.AddOptions['AddPage.AccountSelectorSelector'.lower()].split('>')[1]
        # AccountOptionsOptions = self.AddOptions['AddPage.AccountOptionsOptions'.lower()].split('>')[1]


        self.Add.productNameInput().send_keys(productName)

        #参数为单下拉框 选择这个，否则删除
        self.typeIdSelector = self.AddOptions['AddPage.typeIdSelector'.lower()].split('>')[1]
        self.typeIdOptions= self.AddOptions['AddPage.typeIdOptions'.lower()].split('>')[1]


        SelectorUtils().selector_choose(self.driver, self.typeIdSelector, self.typeIdOptions)


        self.Add.priceInput().send_keys(price)

        self.Add.depositInput().send_keys(deposit)


        self.Add.rentalInput().send_keys(rental)

        self.Add.rentLimitPriceInput().send_keys(rentLimitPrice)

        logging.info("--滑到页面底部--")
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

        # 把 前端 style="display: none;" 改成block
        container = self.driver.find_element_by_xpath("//*[@id='app']//input[contains(@type,'file')]")
        self.driver.execute_script("arguments[0].style.display = 'block';", container)

        self.driver.find_element_by_xpath("//*[@id='app']//input[contains(@type,'file')]").send_keys(picture)

        self.driver.find_element_by_xpath("//div[@class='productBottom']//div[@class='mt32 ant-row']//div[@contenteditable='true']").send_keys(productcontent)
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[3]/div/div/div[3]/div[3]/div[4]/div/button[1]").click()





