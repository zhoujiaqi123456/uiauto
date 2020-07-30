from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class AddDoctorPage:

    #获取AddDoctorPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.AddDoctorOptions = self.parseCF.getItemsSection('AddDoctorPage')

    def doctorNameInput(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorNameInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element
