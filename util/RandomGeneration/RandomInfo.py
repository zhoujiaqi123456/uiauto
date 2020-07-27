# -*- coding: utf-8 -*-
# @Time : 2020-07-20 10:07
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: RandomInfo.py
# @Project : python-selenium-UI-automation-frame
# @Software: PyCharm
"""
生成随机姓名、电话号码、身份证号、性别、银行卡号、邮箱
"""
import random
from util.RandomGeneration.province_id import province_id
from util.RandomGeneration.phone_number import phone_number


class RandomInfo(object):

    # 随机生成姓名
    def get_name():
        # 删减部分，比较大众化姓氏
        firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                    "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                    "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
        # 百家姓全部姓氏
        # firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
        #             "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
        #             "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
        #             "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
        #             "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
        # 百家姓中双姓氏
        firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
        # 女孩名字
        girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
        # 男孩名字
        boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
        # 名
        name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

        # 10%的机遇生成双数姓氏
        if random.choice(range(100)) > 10:
            firstName_name = firstName[random.choice(range(len(firstName)))]
        else:
            i = random.choice(range(len(firstName2)))
            firstName_name = firstName2[i:i + 2]

        sex = random.choice(range(2))
        name_1 = ""
        # 生成并返回一个名字
        if sex > 0:
            girl_name = girl[random.choice(range(len(girl)))]
            if random.choice(range(2)) > 0:
                name_1 = name[random.choice(range(len(name)))]
            return firstName_name + name_1 + girl_name
        else:
            boy_name = boy[random.choice(range(len(boy)))]
            if random.choice(range(2)) > 0:
                name_1 = name[random.choice(range(len(name)))]
            return firstName_name + name_1 + boy_name


    # 随机生成身份证号
    def get_idnum():
        id_num = ''
        # 随机选择地址码
        id_num +=str(random.choice(province_id))
        # 随机生成4-6位地址码
        for i in range(4):
            ran_num = str(random.randint(0, 9))
            id_num += ran_num
        b = RandomInfo.get_birthday()
        id_num+=b
        # 生成15、16位顺序号
        num = ''
        for i in range(2):
            num += str(random.randint(0, 9))
        id_num += num
        # 通过性别判断生成第十七位数字 男单 女双
        s = RandomInfo.get_sex()
        # print("性别:", s)
        if s =='男':
            # 生成奇数
            seventeen_num = random.randrange(1,9,2)
        else:
            seventeen_num = random.randrange(2,9,2)
        id_num+=str(seventeen_num)
        eighteen_num = str(random.randint(1,10))
        if eighteen_num == '10':
            eighteen_num = 'X'
        id_num += eighteen_num
        return id_num



    # 随机生成出生日期
    def get_birthday():
        # 随机生成年月日
        year = random.randint(1960, 2000)
        month = random.randint(1, 12)
        # 判断每个月有多少天随机生成日
        if year%4 ==0:
            if month in (1,3,5,7,8,10,12):
                day = random.randint(1,31)
            elif month in (4,6,9,11):
                day = random.randint(1,30)
            else:
                day = random.randint(1,29)
        else:
            if month in (1,3,5,7,8,10,12):
                day = random.randint(1,31)
            elif month in (4,6,9,11):
                day = random.randint(1,30)
            else:
                day = random.randint(1,28)
        # 小于10的月份前面加0
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        birthday = str(year)+str(month)+str(day)
        return birthday

    # 随机生成性别
    def get_sex():
        return random.choice(['男', '女'])
    # get_sex = lambda :random.choice(['男', '女'])


    # 随机生成手机号
    def get_tel():
        tel = ''
        tel+=str(random.choice(phone_number))
        ran = ''
        for i in range(8):
            ran += str(random.randint(0,9))
        tel +=ran
        return tel

    # 随机生成银行卡号
    def get_card_id():
        card_id = '62'
        for i in range(17):
            ran = str(random.randint(0,9))
            card_id += ran
        return card_id

    # 随机生成邮箱
    def get_email():
        email_suf = random.choice(['@163.com','@qq.com','@126.com','@sina.com','@sina.cn','@soho.com','@yeah.com'])
        phone = RandomInfo.get_tel()
        email = phone + email_suf
        # print("手机号:",phone)
        return email

if __name__ == '__main__':
    x = RandomInfo.get_name()
    print("姓名:", x)
    sex = RandomInfo.get_sex()
    print("性别：", sex)
    IdCardNum = RandomInfo.get_idnum()
    print("身份证号:", IdCardNum)
    email = RandomInfo.get_email()
    phone_number = RandomInfo.get_tel()
    print("手机号：", phone_number)
    print("邮箱:", email)
    BankCardNum = RandomInfo.get_card_id()
    print("银行卡号:", BankCardNum)