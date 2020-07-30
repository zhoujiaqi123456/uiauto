from selenium import webdriver
import os,re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Ceshi(object):
    def automatic_generation_case(self, account, password,url,login_url):

        driver = webdriver.Chrome()
        self.login_without_qr(driver, account, password,login_url)


        driver.get(url)

        allelements = driver.find_elements_by_xpath('//div[contains(@class,"ant-col ant-form-item-label")]/label')
        label_fors=[]
        for elements in allelements:
            label_fors.append(elements.get_attribute('for'))
        with open(os.path.dirname(os.path.abspath('.'))+'/pageObjects/AddDoctorPageTemplate.py',mode='r') as f:
            content2=f.readlines()
        file_name = url.split('#')[1].split('?')[0].split('/')[-1].replace('-', '_') + '_' +url.split('#')[1].split('?')[0].split('/')[-2].replace('-', '_')

        with open(os.path.dirname(os.path.abspath('.'))+'/'+'pageObjects'+'/'+self.underline_hump(file_name)+'Page'+'.py', mode='w+') as f:
            endcontent = []
            startcontent=[]
            for i ,c in enumerate(content2):
                if 'def doctorNameInput' in c:
                    startcontent = content2[:i]
                    endcontent = content2[i:]
            for u in startcontent:
                if 'AddDoctor' in u:
                    f.writelines(u.replace('AddDoctor',self.underline_hump(file_name)))
                else:
                    f.writelines(u)

            for j,d in enumerate(label_fors):
                for ic in endcontent:
                    if 'AddDoctorPage.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctor',self.underline_hump(file_name))
                                     .replace('AddDoctorPage.doctorNameInput', self.underline_hump(file_name)+'Page'+'.'+d))

                    elif 'doctorName' in ic:
                        f.writelines(ic.replace('doctorName',d))

                    else:
                        f.writelines(ic)

        with open(os.path.dirname(os.path.abspath('.'))+'/Modules/AddDoctorActionTemplate.py',mode='r') as f:
            content_action=f.readlines()
        file_name = url.split('#')[1].split('?')[0].split('/')[-1].replace('-', '_') + '_' +url.split('#')[1].split('?')[0].split('/')[-2].replace('-', '_')

        with open(os.path.dirname(os.path.abspath('.'))+'/'+'Modules'+'/'+self.underline_hump(file_name)+'Action'+'.py', mode='w+') as f:
            endcontent = []
            startcontent=[]
            for i ,c in enumerate(content_action):

                if '#若参数为文本框选择这个，否则删除' in c:
                    startcontent = content_action[:i]
                    endcontent = content_action[i:]
            for u in startcontent:
                if 'AddDoctor' in u:
                    f.writelines(u.replace('AddDoctor',self.underline_hump(file_name)))
                elif 'addDoctor' in u:
                    f.writelines(u.replace('addDoctorAction(self):',self.underline_hump(file_name)+
                                           'Action(self,'+str(label_fors).replace('[','').replace("'",""))
                                 .replace(']','')+'):'+'\n')
                else:
                    f.writelines(u)
            # f.writelines('#用于粘贴到方法里面作为参数  '+str(label_fors)+'\n\n')

            for j,d in enumerate(label_fors):
                for ic in endcontent:
                    if 'AddDoctor.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctor.doctorNameInput().send_keys(doctor_name)',
                                                self.underline_hump(file_name)+'.'+d +
                                                'Input().send_keys('+d+')'))
                    elif 'doctorNameSelector' in ic:
                        f.writelines(ic.replace('doctorName', self.underline_hump(d)+'Selector')
                                     .replace('AddDoctor',self.underline_hump(file_name)))
                    elif 'doctorNameOptions' in ic:
                        f.writelines(ic.replace('doctorName', self.underline_hump(d)+'Options')
                                     .replace('AddDoctor', self.underline_hump(file_name)))
                    else:
                        f.writelines(ic)
        with open(os.path.dirname(os.path.abspath('.'))+'/config/PageElementLocatorTemplate.ini',mode='r') as f:
            content_page=f.readlines()
        with open(os.path.dirname(os.path.abspath('.')) + '/' + 'config' + '/' + self.underline_hump(file_name)+ '.ini', mode='w+') as f:
            startcontent_page=[]
            endcontent_page =[]
            for g, ic in enumerate(content_page):
                if '[AddDoctorPage]' in ic:
                    startcontent_page = content_page[:(g+1)]
                    endcontent_page = content_page[(g+1):]
            print(startcontent_page)
            for u in startcontent_page:
                if '[AddDoctorPage]' in u:
                    f.writelines(u.replace('AddDoctor', self.underline2_hump(file_name)))
                else:
                    f.writelines(u)

            for j,d in enumerate(label_fors):
                for g,ic in enumerate(endcontent_page):
                    if 'AddDoctorPage.doctorNameInput' in ic:
                        f.writelines(ic.replace('AddDoctor',self.underline_hump(file_name))
                                     .replace('doctorName', self.underline2_hump(d)))


        f.close()


    def login_without_qr(self, browser, account, password,login_url):
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
        account_input = browser.find_element_by_id('email')
        if account_input is None:
            print('未找到账号输入框')
            return 0
        account_input.click()
        account_input.send_keys(account)
        # 输入密码
        password_input = browser.find_element_by_id('password')
        if password_input is None:
            print('未找到密码输入框')
            return 0
        password_input.click()
        password_input.send_keys(password)
        # 点击登陆
        submit_array = browser.find_elements_by_class_name('ant-btn-lg')
        if len(submit_array) > 0:
            submit_array[0].click()

            # 等待元素加载
            WebDriverWait(browser, 30, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/header/div[2]/a/div/p[1]'))
            )
            # 判断是否登录成功
            real_account = browser.find_element_by_xpath('//*[@id="app"]/div/div/header/div[2]/a/div/p[1]').text

            if real_account == account:
                return 1
            else:
                print('登录失败')
                return 0

        else:
            print('未获取到提交按钮')
            return 0

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
        sub[0].upper()
        return sub[0].upper()+sub[1:]


if __name__ == "__main__":

    login_url = "http://47.99.104.87:6773/#/login"
    account = "TAL0077"
    password = "123456"
    aa = 'http://47.99.104.87:6773/#/logistics/whole-price/add?type=0'
    bb = 'http://47.99.104.87:6773/#/merchants/supplier-management/company-add'
    cc='http://47.99.104.87:6773/#/merchants/customer-administration/company-add'
    Ceshi().automatic_generation_case(account, password,aa,login_url)
