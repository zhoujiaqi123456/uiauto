from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AddWholePricePage:

    #获取AddWholePricePage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.AddWholePriceOptions = self.parseCF.getItemsSection('AddWholePricePage')

    def startPortInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def endPortInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def carrierInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def startDockInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def endDockInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def transitPortInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def proxyCodeInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def dayOfWeekStartAndEndInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def sailRangeInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def startFreeBoxInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def endFreeBoxInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def expireDateInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def portChargeInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def remarkInput(self):
        try:
            locateType, locateExpression = self.AddWholePriceOptions['AddWholePricePage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
