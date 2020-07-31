# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.CompanyAddSupplierManagementPage import CompanyAddSupplierManagementPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class CompanyAddSupplierManagementAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.CompanyAddSupplierManagement = CompanyAddSupplierManagementPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.CompanyAddSupplierManagementOptions = self.parseCF.getItemsSection('CompanyAddSupplierManagementPage')
        logger.info("CompanyAddSupplierManagement..")

    def CompanyAddSupplierManagementAction(self,name, companyPrefix, nameEn, invoice, country, usci, tel, addr, companyCode, settleType, businessType, startDate, endDate, companySize, contractor, contractorTel, financialOfficer, financialTel, financialClientCode, financialSupplierCode, bankCard, bankName, bankCreator, mailAddr, deposit, currency, contractFile, supplierType
):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.nameInput().send_keys(name)

        #参数为单下拉框 选择这个，否则删除
        NameSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.NameSelectorSelector'.lower()].split('>')[1]
        NameOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.NameOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.companyPrefixInput().send_keys(companyPrefix)

        #参数为单下拉框 选择这个，否则删除
        CompanyPrefixSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanyPrefixSelectorSelector'.lower()].split('>')[1]
        CompanyPrefixOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanyPrefixOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.nameEnInput().send_keys(nameEn)

        #参数为单下拉框 选择这个，否则删除
        NameEnSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.NameEnSelectorSelector'.lower()].split('>')[1]
        NameEnOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.NameEnOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.invoiceInput().send_keys(invoice)

        #参数为单下拉框 选择这个，否则删除
        InvoiceSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.InvoiceSelectorSelector'.lower()].split('>')[1]
        InvoiceOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.InvoiceOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.countryInput().send_keys(country)

        #参数为单下拉框 选择这个，否则删除
        CountrySelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CountrySelectorSelector'.lower()].split('>')[1]
        CountryOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CountryOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.usciInput().send_keys(usci)

        #参数为单下拉框 选择这个，否则删除
        UsciSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.UsciSelectorSelector'.lower()].split('>')[1]
        UsciOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.UsciOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.telInput().send_keys(tel)

        #参数为单下拉框 选择这个，否则删除
        TelSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.TelSelectorSelector'.lower()].split('>')[1]
        TelOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.TelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.addrInput().send_keys(addr)

        #参数为单下拉框 选择这个，否则删除
        AddrSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.AddrSelectorSelector'.lower()].split('>')[1]
        AddrOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.AddrOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.companyCodeInput().send_keys(companyCode)

        #参数为单下拉框 选择这个，否则删除
        CompanyCodeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanyCodeSelectorSelector'.lower()].split('>')[1]
        CompanyCodeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanyCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.settleTypeInput().send_keys(settleType)

        #参数为单下拉框 选择这个，否则删除
        SettleTypeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.SettleTypeSelectorSelector'.lower()].split('>')[1]
        SettleTypeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.SettleTypeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.businessTypeInput().send_keys(businessType)

        #参数为单下拉框 选择这个，否则删除
        BusinessTypeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BusinessTypeSelectorSelector'.lower()].split('>')[1]
        BusinessTypeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BusinessTypeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.startDateInput().send_keys(startDate)

        #参数为单下拉框 选择这个，否则删除
        StartDateSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.StartDateSelectorSelector'.lower()].split('>')[1]
        StartDateOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.StartDateOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.endDateInput().send_keys(endDate)

        #参数为单下拉框 选择这个，否则删除
        EndDateSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.EndDateSelectorSelector'.lower()].split('>')[1]
        EndDateOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.EndDateOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.companySizeInput().send_keys(companySize)

        #参数为单下拉框 选择这个，否则删除
        CompanySizeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanySizeSelectorSelector'.lower()].split('>')[1]
        CompanySizeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CompanySizeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.contractorInput().send_keys(contractor)

        #参数为单下拉框 选择这个，否则删除
        ContractorSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractorSelectorSelector'.lower()].split('>')[1]
        ContractorOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractorOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.contractorTelInput().send_keys(contractorTel)

        #参数为单下拉框 选择这个，否则删除
        ContractorTelSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractorTelSelectorSelector'.lower()].split('>')[1]
        ContractorTelOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractorTelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.financialOfficerInput().send_keys(financialOfficer)

        #参数为单下拉框 选择这个，否则删除
        FinancialOfficerSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialOfficerSelectorSelector'.lower()].split('>')[1]
        FinancialOfficerOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialOfficerOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.financialTelInput().send_keys(financialTel)

        #参数为单下拉框 选择这个，否则删除
        FinancialTelSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialTelSelectorSelector'.lower()].split('>')[1]
        FinancialTelOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialTelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.financialClientCodeInput().send_keys(financialClientCode)

        #参数为单下拉框 选择这个，否则删除
        FinancialClientCodeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialClientCodeSelectorSelector'.lower()].split('>')[1]
        FinancialClientCodeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialClientCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.financialSupplierCodeInput().send_keys(financialSupplierCode)

        #参数为单下拉框 选择这个，否则删除
        FinancialSupplierCodeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialSupplierCodeSelectorSelector'.lower()].split('>')[1]
        FinancialSupplierCodeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.FinancialSupplierCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.bankCardInput().send_keys(bankCard)

        #参数为单下拉框 选择这个，否则删除
        BankCardSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankCardSelectorSelector'.lower()].split('>')[1]
        BankCardOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankCardOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.bankNameInput().send_keys(bankName)

        #参数为单下拉框 选择这个，否则删除
        BankNameSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankNameSelectorSelector'.lower()].split('>')[1]
        BankNameOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankNameOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.bankCreatorInput().send_keys(bankCreator)

        #参数为单下拉框 选择这个，否则删除
        BankCreatorSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankCreatorSelectorSelector'.lower()].split('>')[1]
        BankCreatorOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.BankCreatorOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.mailAddrInput().send_keys(mailAddr)

        #参数为单下拉框 选择这个，否则删除
        MailAddrSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.MailAddrSelectorSelector'.lower()].split('>')[1]
        MailAddrOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.MailAddrOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.depositInput().send_keys(deposit)

        #参数为单下拉框 选择这个，否则删除
        DepositSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.DepositSelectorSelector'.lower()].split('>')[1]
        DepositOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.DepositOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.currencyInput().send_keys(currency)

        #参数为单下拉框 选择这个，否则删除
        CurrencySelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CurrencySelectorSelector'.lower()].split('>')[1]
        CurrencyOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.CurrencyOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.contractFileInput().send_keys(contractFile)

        #参数为单下拉框 选择这个，否则删除
        ContractFileSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractFileSelectorSelector'.lower()].split('>')[1]
        ContractFileOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.ContractFileOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddSupplierManagement.supplierTypeInput().send_keys(supplierType)

        #参数为单下拉框 选择这个，否则删除
        SupplierTypeSelectorSelector = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.SupplierTypeSelectorSelector'.lower()].split('>')[1]
        SupplierTypeOptionsOptions = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.SupplierTypeOptionsOptions'.lower()].split('>')[1]

