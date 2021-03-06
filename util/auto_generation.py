from selenium import webdriver
import os,re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Ceshi(object):
    def automatic_generation_case(self, account, password,url,login_url,xpath,account_id,password_id,label):
        '''

        :param account: 登录账号
        :param password: 登录密码
        :param url: 要定位的新增页面的url
        :param login_url: 登录url
        :param xpath:  要解析的新增页面表单元素；'//div[contains(@class,"ant-col ant-form-item-label")]/label' 可不修改 大部分通用
        :param account_id: 登录账号 定位元素id
        :param password_id: 登录密码 定位元素id
        :param label: label属性
        :return:
        '''

        driver = webdriver.Chrome()
        current_window = driver.current_window_handle
        self.login_without_qr(driver, account, password,login_url,account_id,password_id)





        js = 'window.open("' + url + '");'
        driver.execute_script(js)

        # 页面中点击某个链接会弹出一个新的窗口，这样要去操作新窗口中的元素，这时就需要主机切换到新窗口进行操作。
        # 定位到新开页面的句柄
        handles = driver.window_handles
        for handle in handles:
            if handle == current_window:
                continue
        driver.switch_to.window(handle)

        allelements = driver.find_elements_by_xpath(xpath)
        label_for=[]
        label_fors = []
        for elements in allelements:
            label_for.append(elements.get_attribute(label))
        label_fors=list(filter(None, label_for))
        print(label_fors)
        with open(os.path.dirname(os.path.abspath('.'))+'/pageObjects/AddDoctorPageTemplate.py',mode='r') as f:
            content2=f.readlines()
        file_name = url.split('#')[1].split('?')[0].split('/')[-1].replace('-', '_')  +url.split('#')[1].split('?')[0].split('/')[-2].replace('-', '_')
        print(file_name)

        with open(os.path.dirname(os.path.abspath('.'))+'/'+'pageObjects'+'/'+self.underline_hump(file_name)+'Page'+'.py', mode='w+') as f:
            endcontent = []
            startcontent=[]
            for i ,c in enumerate(content2):
                if 'def doctorNameInput' in c:
                    startcontent = content2[:i]
                    endcontent = content2[i:]
            for u in startcontent:
                if 'AddDoctor' in u:
                    f.writelines(u.replace('AddDoctor',self.underline2_hump(file_name)))
                else:
                    f.writelines(u)

            for j,d in enumerate(label_fors):
                for ic in endcontent:
                    if 'AddDoctorPage.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctorOptions',self.underline2_hump(file_name)+'Options').replace('AddDoctorPage.doctorNameInput', self.underline2_hump(file_name)+'Page'+'.'+d+'Input'))
                        # f.writelines(ic.replace('AddDoctorPage.doctorNameInput', self.underline_hump(file_name)+'Page'+'.'+d+'Input').replace('AddDoctor',self.underline_hump(file_name)))


                    elif 'doctorName' in ic:
                        f.writelines(ic.replace('doctorName',d))

                    else:
                        f.writelines(ic)

        with open(os.path.dirname(os.path.abspath('.'))+'/Modules/AddDoctorActionTemplate.py',mode='r') as f:
            content_action=f.readlines()
        file_name = url.split('#')[1].split('?')[0].split('/')[-1].replace('-', '_')  +url.split('#')[1].split('?')[0].split('/')[-2].replace('-', '_')

        with open(os.path.dirname(os.path.abspath('.'))+'/'+'Modules'+'/'+self.underline_hump(file_name)+'Action'+'.py', mode='w+') as f:
            endcontent = []
            startcontent=[]
            for i ,c in enumerate(content_action):

                if '#若参数为文本框选择这个，否则删除' in c:
                    startcontent = content_action[:i]
                    endcontent = content_action[i:]
            for u in startcontent:
                if 'AddDoctor' in u:
                    f.writelines(u.replace('AddDoctor',self.underline2_hump(file_name)))
                elif 'addDoctor' in u:
                    f.writelines(u.replace('addDoctorAction(self):',self.underline2_hump(file_name)+
                                           'Action(self,'+str(label_fors).replace('[','').replace("'",""))
                                 .replace(']','')+'):'+'\n')
                else:
                    f.writelines(u)
            # f.writelines('#用于粘贴到方法里面作为参数  '+str(label_fors)+'\n\n')

            for j,d in enumerate(label_fors):
                for ic in endcontent:
                    if 'AddDoctor.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctor.doctorNameInput().send_keys(doctor_name)',
                                                self.underline2_hump(file_name)+'.'+d +
                                                'Input().send_keys('+d+')'))
                    elif 'doctorNameSelector' in ic:
                        f.writelines(ic.replace('doctorName', self.underline_hump(d))
                                     .replace('AddDoctor',self.underline2_hump(file_name)))
                    elif 'doctorNameOptions' in ic:
                        f.writelines(ic.replace('doctorName', self.underline_hump(d))
                                     .replace('AddDoctor', self.underline2_hump(file_name)))
                    else:
                        f.writelines(ic)
        with open(os.path.dirname(os.path.abspath('.'))+'/config/PageElementLocatorTemplate.ini',mode='r') as f:
            content_page=f.readlines()
        with open(os.path.dirname(os.path.abspath('.')) + '/' + 'config' + '/' + self.underline_hump(file_name) + '.ini', mode='w+') as f:
            startcontent_page=[]
            endcontent_page =[]
            for g, ic in enumerate(content_page):
                if '[AddDoctorPage]' in ic:
                    startcontent_page = content_page[:(g+1)]
                    endcontent_page = content_page[(g+1):]
            for u in startcontent_page:
                if '[AddDoctorPage]' in u:
                    f.writelines(u.replace('AddDoctor', self.underline2_hump(file_name)))
                else:
                    f.writelines(u)

            for j,d in enumerate(label_fors):
                for g,ic in enumerate(endcontent_page):
                    if 'AddDoctorPage.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctor',self.underline2_hump(file_name))
                                     .replace('doctorName', self.underline_hump(d)))
                    elif 'AddDoctorPage.doctorNameSelector' in ic:
                        f.writelines(ic.replace('AddDoctor',self.underline2_hump(file_name))
                                     .replace('doctorName', self.underline_hump(d))
                                     )
                    elif 'AddDoctorPage.doctorNameOptions' in ic:
                        f.writelines(ic.replace('AddDoctor', self.underline2_hump(file_name))
                                     .replace('doctorName', self.underline_hump(d))
                                     )

                    else:
                        f.writelines(ic)
        print("写入成功")


        f.close()


    def login_without_qr(self, browser, account, password,login_url,account_id,password_id):
        """
        :param browser: 浏览器
        :param account: 账号
        :param password: 密码
        :return: 0-发生错误；1-未发生错误
        """
        # 获取浏览器当前标签页句柄
        current_window = browser.current_window_handle
        # 新开标签页打开网址

        js = 'window.open("' + login_url + '");'
        print(js)
        browser.execute_script(js)

        # 页面中点击某个链接会弹出一个新的窗口，这样要去操作新窗口中的元素，这时就需要主机切换到新窗口进行操作。
        # 定位到新开页面的句柄
        handles = browser.window_handles
        for handle in handles:
            if handle == current_window:
                continue
        browser.switch_to.window(handle)
        # print browser.title

        # browser.get(url)
        browser.maximize_window()

        # 输入账号
        account_input = browser.find_element_by_id(account_id)
        if account_input is None:
            print('未找到账号输入框')
            return 0
        account_input.click()
        account_input.send_keys(account)

        #把 前端 密码框style="display: none;" 改成block
        container = browser.find_element_by_xpath('//form/div/div[3]/div/div[3]/div/div/span/span[1]')
        browser.execute_script("arguments[0].style.display = 'block';", container)


        password_input = browser.find_element_by_id(password_id)
        if password_input is None:
            print('未找到密码输入框')
            return 0
        password_input.click()
        password_input.send_keys(password)
        browser.implicitly_wait(5)

        # 点击登陆
        submit_array = browser.find_elements_by_class_name('ant-btn-lg')
        if len(submit_array) > 0:
            submit_array[0].click()

        else:
            print('未获取到提交按钮')
            return 0

        browser.find_element_by_xpath('//*[@id="app"]/div/div/header/div/a')

    def underline2_hump(self,underline_str):
        '''
        下划线形式字符串转成驼峰形式
        :param underline_str: 下划线形式字符串
        :return: 驼峰形式字符串
        '''
        # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
        sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
        return sub[0].upper()+sub[1:]

    def hump_to_underline(self, camelCaps, separator="_"):
        pattern = re.compile(r'([A-Z]{1})')
        sub = re.sub(pattern, separator + r'\1', camelCaps).lower()
        return sub

    def underline_hump(self,underline_str):
        '''
        下划线形式字符串转成驼峰形式
        :param underline_str: 下划线形式字符串
        :return: 驼峰形式字符串
        '''
        # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
        sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
        # sub[0].upper()
        return sub[0]+sub[1:]


if __name__ == "__main__":

    login_url = "http://47.99.104.87:7010/#/login"
    account = "admin"
    password = "123456"
    aa = 'http://47.99.104.87:6773/#/logistics/whole-price/add?type=0'
    bb = 'http://47.99.104.87:6773/#/merchants/supplier-management/company-add'
    cc='http://47.99.104.87:6773/#/merchants/customer-administration/company-add'
    zqb='http://47.99.104.87:7010/#/bannerAdd'
    zqb1 = 'http://47.99.104.87:7010/#/coupon/management/add'
    zhq1='http://47.99.104.87:7010/#/account/list/add'
    ww='http://47.99.104.87:7010/#/coupon/management/add'
    #xpath 可不修改，通用性
    xpath='//div[contains(@class,"ant-form-item-label")]/label'
    account_id='account'
    password_id='password'
    label='for'
    Ceshi().automatic_generation_case(account, password,ww,login_url,xpath,account_id,password_id,label)


