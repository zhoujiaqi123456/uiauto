# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pageObjects.CompanyAddCustomerAdministrationPage import CompanyAddCustomerAdministrationPage
from util.Log import *
from Modules.LoginAction import LoginAction
from util.SelectorUtils import SelectorUtils
from util.ParseConfigurationFile import ParseConfigFile
from util.RandomGeneration.RandomInfo import RandomInfo
class CompanyAddCustomerAdministrationAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.CompanyAddCustomerAdministration = CompanyAddCustomerAdministrationPage(self.driver)
        self.parseCF = ParseConfigFile()
        self.CompanyAddCustomerAdministrationOptions = self.parseCF.getItemsSection('CompanyAddCustomerAdministrationPage')
        logger.info("CompanyAddCustomerAdministration..")

    def CompanyAddCustomerAdministrationAction(self,name, companyPrefix, nameEn, invoice, country, usci, tel, countryCode, addr, companyCode, settleType, businessType, startDate, endDate, companySize, contractor, contractorTel, financialOfficer, financialTel, financialClientCode, relateSalesmanCodeList, relateCsrCodeList, bankCard, bankName, bankCreator, sendMailPerson, mailAddr, eposit, currency, credit, isSupplier, level, mailEmail, clientType, contractFile
):
        '''
        读取传参数据操作
        :param
        :return:
        '''

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.nameInput().send_keys(name)

        #参数为单下拉框 选择这个，否则删除
        NameSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.NameSelectorSelector'.lower()].split('>')[1]
        NameOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.NameOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.companyPrefixInput().send_keys(companyPrefix)

        #参数为单下拉框 选择这个，否则删除
        CompanyPrefixSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanyPrefixSelectorSelector'.lower()].split('>')[1]
        CompanyPrefixOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanyPrefixOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.nameEnInput().send_keys(nameEn)

        #参数为单下拉框 选择这个，否则删除
        NameEnSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.NameEnSelectorSelector'.lower()].split('>')[1]
        NameEnOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.NameEnOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.invoiceInput().send_keys(invoice)

        #参数为单下拉框 选择这个，否则删除
        InvoiceSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.InvoiceSelectorSelector'.lower()].split('>')[1]
        InvoiceOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.InvoiceOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.countryInput().send_keys(country)

        #参数为单下拉框 选择这个，否则删除
        CountrySelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CountrySelectorSelector'.lower()].split('>')[1]
        CountryOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CountryOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.usciInput().send_keys(usci)

        #参数为单下拉框 选择这个，否则删除
        UsciSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.UsciSelectorSelector'.lower()].split('>')[1]
        UsciOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.UsciOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.telInput().send_keys(tel)

        #参数为单下拉框 选择这个，否则删除
        TelSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.TelSelectorSelector'.lower()].split('>')[1]
        TelOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.TelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.countryCodeInput().send_keys(countryCode)

        #参数为单下拉框 选择这个，否则删除
        CountryCodeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CountryCodeSelectorSelector'.lower()].split('>')[1]
        CountryCodeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CountryCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.addrInput().send_keys(addr)

        #参数为单下拉框 选择这个，否则删除
        AddrSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.AddrSelectorSelector'.lower()].split('>')[1]
        AddrOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.AddrOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.companyCodeInput().send_keys(companyCode)

        #参数为单下拉框 选择这个，否则删除
        CompanyCodeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanyCodeSelectorSelector'.lower()].split('>')[1]
        CompanyCodeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanyCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.settleTypeInput().send_keys(settleType)

        #参数为单下拉框 选择这个，否则删除
        SettleTypeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.SettleTypeSelectorSelector'.lower()].split('>')[1]
        SettleTypeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.SettleTypeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.businessTypeInput().send_keys(businessType)

        #参数为单下拉框 选择这个，否则删除
        BusinessTypeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BusinessTypeSelectorSelector'.lower()].split('>')[1]
        BusinessTypeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BusinessTypeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.startDateInput().send_keys(startDate)

        #参数为单下拉框 选择这个，否则删除
        StartDateSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.StartDateSelectorSelector'.lower()].split('>')[1]
        StartDateOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.StartDateOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.endDateInput().send_keys(endDate)

        #参数为单下拉框 选择这个，否则删除
        EndDateSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.EndDateSelectorSelector'.lower()].split('>')[1]
        EndDateOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.EndDateOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.companySizeInput().send_keys(companySize)

        #参数为单下拉框 选择这个，否则删除
        CompanySizeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanySizeSelectorSelector'.lower()].split('>')[1]
        CompanySizeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CompanySizeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.contractorInput().send_keys(contractor)

        #参数为单下拉框 选择这个，否则删除
        ContractorSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractorSelectorSelector'.lower()].split('>')[1]
        ContractorOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractorOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.contractorTelInput().send_keys(contractorTel)

        #参数为单下拉框 选择这个，否则删除
        ContractorTelSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractorTelSelectorSelector'.lower()].split('>')[1]
        ContractorTelOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractorTelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.financialOfficerInput().send_keys(financialOfficer)

        #参数为单下拉框 选择这个，否则删除
        FinancialOfficerSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialOfficerSelectorSelector'.lower()].split('>')[1]
        FinancialOfficerOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialOfficerOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.financialTelInput().send_keys(financialTel)

        #参数为单下拉框 选择这个，否则删除
        FinancialTelSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialTelSelectorSelector'.lower()].split('>')[1]
        FinancialTelOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialTelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.financialClientCodeInput().send_keys(financialClientCode)

        #参数为单下拉框 选择这个，否则删除
        FinancialClientCodeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialClientCodeSelectorSelector'.lower()].split('>')[1]
        FinancialClientCodeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.FinancialClientCodeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.relateSalesmanCodeListInput().send_keys(relateSalesmanCodeList)

        #参数为单下拉框 选择这个，否则删除
        RelateSalesmanCodeListSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.RelateSalesmanCodeListSelectorSelector'.lower()].split('>')[1]
        RelateSalesmanCodeListOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.RelateSalesmanCodeListOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.relateCsrCodeListInput().send_keys(relateCsrCodeList)

        #参数为单下拉框 选择这个，否则删除
        RelateCsrCodeListSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.RelateCsrCodeListSelectorSelector'.lower()].split('>')[1]
        RelateCsrCodeListOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.RelateCsrCodeListOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.bankCardInput().send_keys(bankCard)

        #参数为单下拉框 选择这个，否则删除
        BankCardSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankCardSelectorSelector'.lower()].split('>')[1]
        BankCardOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankCardOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.bankNameInput().send_keys(bankName)

        #参数为单下拉框 选择这个，否则删除
        BankNameSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankNameSelectorSelector'.lower()].split('>')[1]
        BankNameOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankNameOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.bankCreatorInput().send_keys(bankCreator)

        #参数为单下拉框 选择这个，否则删除
        BankCreatorSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankCreatorSelectorSelector'.lower()].split('>')[1]
        BankCreatorOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.BankCreatorOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.sendMailPersonInput().send_keys(sendMailPerson)

        #参数为单下拉框 选择这个，否则删除
        SendMailPersonSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.SendMailPersonSelectorSelector'.lower()].split('>')[1]
        SendMailPersonOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.SendMailPersonOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.mailAddrInput().send_keys(mailAddr)

        #参数为单下拉框 选择这个，否则删除
        MailAddrSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.MailAddrSelectorSelector'.lower()].split('>')[1]
        MailAddrOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.MailAddrOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.epositInput().send_keys(eposit)

        #参数为单下拉框 选择这个，否则删除
        EpositSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.EpositSelectorSelector'.lower()].split('>')[1]
        EpositOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.EpositOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.currencyInput().send_keys(currency)

        #参数为单下拉框 选择这个，否则删除
        CurrencySelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CurrencySelectorSelector'.lower()].split('>')[1]
        CurrencyOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CurrencyOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.creditInput().send_keys(credit)

        #参数为单下拉框 选择这个，否则删除
        CreditSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CreditSelectorSelector'.lower()].split('>')[1]
        CreditOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.CreditOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.isSupplierInput().send_keys(isSupplier)

        #参数为单下拉框 选择这个，否则删除
        IsSupplierSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.IsSupplierSelectorSelector'.lower()].split('>')[1]
        IsSupplierOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.IsSupplierOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.levelInput().send_keys(level)

        #参数为单下拉框 选择这个，否则删除
        LevelSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.LevelSelectorSelector'.lower()].split('>')[1]
        LevelOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.LevelOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.mailEmailInput().send_keys(mailEmail)

        #参数为单下拉框 选择这个，否则删除
        MailEmailSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.MailEmailSelectorSelector'.lower()].split('>')[1]
        MailEmailOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.MailEmailOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.clientTypeInput().send_keys(clientType)

        #参数为单下拉框 选择这个，否则删除
        ClientTypeSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ClientTypeSelectorSelector'.lower()].split('>')[1]
        ClientTypeOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ClientTypeOptionsOptions'.lower()].split('>')[1]

        #若参数为文本框选择这个，否则删除
        self.CompanyAddCustomerAdministration.contractFileInput().send_keys(contractFile)

        #参数为单下拉框 选择这个，否则删除
        ContractFileSelectorSelector = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractFileSelectorSelector'.lower()].split('>')[1]
        ContractFileOptionsOptions = self.CompanyAddCustomerAdministrationOptions['CompanyAddCustomerAdministrationPage.ContractFileOptionsOptions'.lower()].split('>')[1]

