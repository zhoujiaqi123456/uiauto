from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *
from Modules.LoginAction import LoginAction

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


    def doctorGenderSelector(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorGenderSelector'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element



    def doctorGenderOptions(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorGenderOptions'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorIDNumberInput(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorIDNumberInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorNumberInput(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorNumberInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorTitleSelector(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorTitleSelector'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorTitleOptions(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorTitleOptions'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorDepartmentSelector(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentSelector'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorDepartmentOptions(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorDepartmentOptions'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorPhoneNumberInput(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorPhoneNumberInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorEmailInput(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorEmailInput'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorRemarksTextArea(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorRemarksTextArea'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorSubmitButton(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorSubmitButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

    def doctorCancelButton(self):
        try:
            locateType, locateExpression = self.AddDoctorOptions['AddDoctorPage.doctorCancelButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element

if __name__=="__main__":
    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    browser.get("http://47.96.186.244:8020/user/login")
    browser.maximize_window()
    LoginAction.login('yinchengjie', '123456', browser, "http://47.96.186.244:8020/doctorControl/doctorControlList/add")
    addDoctor = AddDoctorPage(browser)
    browser.implicitly_wait(1)
    addDoctor.doctorNameInput().send_keys("殷诚杰")
    addDoctor.doctorSubmitButton().click()
    time.sleep(1)
    browser.quit()