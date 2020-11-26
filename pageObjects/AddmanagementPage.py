from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AddmanagementPage:

    #获取AddmanagementPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.AddmanagementOptions = self.parseCF.getItemsSection('AddmanagementPage')

    def couponNoInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.couponNoInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def titleInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.titleInput'.lower()].split('>')
            print(locateType,locateExpression)
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element

    def sceneInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.sceneInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def typeInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.typeInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def timeInput1(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.timeInput1'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element

    def timeInput2(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.timeInput2'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def reachedAmountInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.reachedAmountInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def discountAmountInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.discountAmountInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def userIdsInput(self):
        try:
            locateType, locateExpression = self.AddmanagementOptions['AddmanagementPage.userIdsInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
