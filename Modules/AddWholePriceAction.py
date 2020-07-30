# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.AddWholePricePage import AddWholePricePage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class AddWholePriceAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.AddWholePrice = AddWholePricePage(self.driver)
        self.parseCF = ParseConfigFile()
        self.AddWholePriceOptions = self.parseCF.getItemsSection('AddWholePricePage')
        logger.info("AddWholePrice..")

    def AddWholePriceAction(self,startPort, endPort, carrier, startDock, endDock, transitPort, proxyCode, dayOfWeekStartAndEnd, sailRange, startFreeBox, endFreeBox, expireDate, portCharge, remark
):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.startPortInput().send_keys(startPort)

        #参数为单下拉框 选择这个，否则删除
        StartPortSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.StartPortSelectorSelector'.lower()].split('>')[1]
        StartPortOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.StartPortOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.endPortInput().send_keys(endPort)

        #参数为单下拉框 选择这个，否则删除
        EndPortSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.EndPortSelectorSelector'.lower()].split('>')[1]
        EndPortOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.EndPortOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.carrierInput().send_keys(carrier)

        #参数为单下拉框 选择这个，否则删除
        CarrierSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.CarrierSelectorSelector'.lower()].split('>')[1]
        CarrierOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.CarrierOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.startDockInput().send_keys(startDock)

        #参数为单下拉框 选择这个，否则删除
        StartDockSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.StartDockSelectorSelector'.lower()].split('>')[1]
        StartDockOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.StartDockOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.endDockInput().send_keys(endDock)

        #参数为单下拉框 选择这个，否则删除
        EndDockSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.EndDockSelectorSelector'.lower()].split('>')[1]
        EndDockOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.EndDockOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.transitPortInput().send_keys(transitPort)

        #参数为单下拉框 选择这个，否则删除
        TransitPortSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.TransitPortSelectorSelector'.lower()].split('>')[1]
        TransitPortOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.TransitPortOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.proxyCodeInput().send_keys(proxyCode)

        #参数为单下拉框 选择这个，否则删除
        ProxyCodeSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.ProxyCodeSelectorSelector'.lower()].split('>')[1]
        ProxyCodeOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.ProxyCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.dayOfWeekStartAndEndInput().send_keys(dayOfWeekStartAndEnd)

        #参数为单下拉框 选择这个，否则删除
        DayOfWeekStartAndEndSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.DayOfWeekStartAndEndSelectorSelector'.lower()].split('>')[1]
        DayOfWeekStartAndEndOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.DayOfWeekStartAndEndOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.sailRangeInput().send_keys(sailRange)

        #参数为单下拉框 选择这个，否则删除
        SailRangeSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.SailRangeSelectorSelector'.lower()].split('>')[1]
        SailRangeOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.SailRangeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.startFreeBoxInput().send_keys(startFreeBox)

        #参数为单下拉框 选择这个，否则删除
        StartFreeBoxSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.StartFreeBoxSelectorSelector'.lower()].split('>')[1]
        StartFreeBoxOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.StartFreeBoxOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.endFreeBoxInput().send_keys(endFreeBox)

        #参数为单下拉框 选择这个，否则删除
        EndFreeBoxSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.EndFreeBoxSelectorSelector'.lower()].split('>')[1]
        EndFreeBoxOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.EndFreeBoxOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.expireDateInput().send_keys(expireDate)

        #参数为单下拉框 选择这个，否则删除
        ExpireDateSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.ExpireDateSelectorSelector'.lower()].split('>')[1]
        ExpireDateOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.ExpireDateOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.portChargeInput().send_keys(portCharge)

        #参数为单下拉框 选择这个，否则删除
        PortChargeSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.PortChargeSelectorSelector'.lower()].split('>')[1]
        PortChargeOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.PortChargeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.AddWholePrice.remarkInput().send_keys(remark)

        #参数为单下拉框 选择这个，否则删除
        RemarkSelectorSelector = self.AddWholePriceOptions['AddWholePricePage.RemarkSelectorSelector'.lower()].split('>')[1]
        RemarkOptionsOptions = self.AddWholePriceOptions['AddWholePricePage.RemarkOptionsOptions'.lower()].split('>')[1]

