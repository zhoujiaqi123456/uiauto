from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class CompanyAddSupplierManagementPage:

    #获取CompanyAddSupplierManagementPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.CompanyAddSupplierManagementOptions = self.parseCF.getItemsSection('CompanyAddSupplierManagementPage')

    def nameInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def companyPrefixInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def nameEnInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def invoiceInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def countryInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def usciInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def telInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def addrInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def companyCodeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def settleTypeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def businessTypeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def startDateInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def endDateInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def companySizeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def contractorInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def contractorTelInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def financialOfficerInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def financialTelInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def financialClientCodeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def financialSupplierCodeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def bankCardInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def bankNameInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def bankCreatorInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def mailAddrInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def depositInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def currencyInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def contractFileInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def supplierTypeInput(self):
        try:
            locateType, locateExpression = self.CompanyAddSupplierManagementOptions['CompanyAddSupplierManagementPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
