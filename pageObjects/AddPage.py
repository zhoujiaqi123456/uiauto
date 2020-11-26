from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AddPage:

    #获取AddPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.AddOptions = self.parseCF.getItemsSection('AddPage')

    def accountInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.account'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def productNameInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.ProductNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element

    def typeIdSelector(self):
        try:
            locateType, locateExpression = self.AddOptions[
                'AddPage.typeIdSelector'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def typeIdOptions(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.typeIdOptions'.lower()].split(
                '>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    # def typeIdInput(self):
    #     try:
    #         locateType, locateExpression = self.AddOptions['AddPage.typeIdInput'.lower()].split('>')
    #         element = getElement(self.driver, locateType, locateExpression)
    #     except Exception as e:
    #         logger.error(e)
    #     else:
    #         logger.info("找到元素"+locateExpression)
    #         return element
    def priceInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.PriceInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def depositInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.DepositInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def rentalInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.RentalInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def rentLimitPriceInput(self):
        try:
            locateType, locateExpression = self.AddOptions['AddPage.RentLimitPriceInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
