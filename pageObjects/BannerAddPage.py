from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class bannerAddPage:

    #获取bannerAddPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.bannerAddOptions = self.parseCF.getItemsSection('bannerAddPage')

    def picInput(self):
        try:
            locateType, locateExpression = self.bannerAddOptions['BannerAddPage.picInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def titleInput(self):
        try:
            locateType, locateExpression = self.bannerAddOptions['BannerAddPage.titleInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def actionInput(self):
        try:
            locateType, locateExpression = self.bannerAddOptions['BannerAddPage.actionInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
    def urlInput(self):
        try:
            locateType, locateExpression = self.bannerAddOptions['BannerAddPage.urlInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
