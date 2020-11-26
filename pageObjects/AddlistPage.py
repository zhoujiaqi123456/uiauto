from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AddlistPage:

    #获取AddlistPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.AddlistOptions = self.parseCF.getItemsSection('AddlistPage')

    def accountInput(self):
        try:
            locateType, locateExpression = self.AddlistOptions['AddlistPage.account'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def nameInput(self):
        try:
            locateType, locateExpression = self.AddlistOptions['AddlistPage.name'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def roleIdInput(self):
        try:
            locateType, locateExpression = self.AddlistOptions['AddlistPage.roleId'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
