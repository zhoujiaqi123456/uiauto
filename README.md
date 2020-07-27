# MDT_UIAutomation
##基于 selenium 的 web 自动化测试系统<br>
###一、 系统介绍<br>
####1.系统结构<br>
|访问限制|目录结构|功能描述|
|---|---|---|
| PUBLIC  | config     | 项目配置文件 |
| PUBLIC  | img        | 存放异常截图 |
| PUBLIC  | log        | 脚本运行日志 |
| PUBLIC  | Modules    | 元素操控逻辑 |
| PUBLIC  | pageObjects| 获取页面元素 |
| PUBLIC  | testData   | 测试用例数据 |
| PUBLIC  | testScripts| 测试用例脚本 |
| PUBLIC  | uitl       | 常用工具文件 |
```
####2.功能划分
|── MDT_UIAutomation
|   └── config -------------------------------------- 项目配置文件
|   └── img ----------------------------------------- 存放异常截图
|   └── log ----------------------------------------- 脚本运行日志
|   └── Modules ------------------------------------- 元素操控逻辑
|   └── pageObjects --------------------------------- 获取页面元素
|   └── testData ------------------------------------ 测试用例数据
|   └── testScripts --------------------------------- 测试用例脚本
|   └── uitl ---------------------------------------- 常用工具文件
```
####二、框架目标<br>
1.提供基于selenium的web项目自动化测试基本功能<br>
2.完善各种窗体元素操控方法封装<br>
3.完善随机生成数据方法封装<br>
4.完成UI交互验证异常捕获LOG和截图<br>
5.完成一键运行脚本发送测试报告等附件到邮箱<br>
6.完成一键安装运行环境脚本<br>
####三、模块说明<br>
#####&nbsp;&nbsp;&nbsp;(1) config<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 项目配置文件:<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 主要配置登录账号，元素定位信息，测试数据表列号，路由地址信息，log模板。<br>
#####&nbsp;&nbsp;&nbsp;(2) img<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 存放异常截图 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 针对UI交互的异常捕获生成截图<br>
#####&nbsp;&nbsp;&nbsp;(3) log<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 脚本运行日志 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 存放当前环境自动化测试系统的脚本运行日志<br>
#####&nbsp;&nbsp;&nbsp;(4) Modules<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 元素操控逻辑 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 依据获取到的页面元素进行元素操控逻辑封装。<br>
#####&nbsp;&nbsp;&nbsp;(5) pageObjects<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 获取页面元素 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 根据配置的元素定位信息，编写该元素获取的函数。<br>
#####&nbsp;&nbsp;&nbsp;(6) testData<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 测试用例数据 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Excel表一个sheet对应一个测试用例场景需要的测试用例数据，可写入测试结果和执行时间。<br>
#####&nbsp;&nbsp;&nbsp;(7) testScripts<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 测试用例脚本 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 通过Unitest实现UI自动化所需要覆盖的UI交互场景。<br>
#####&nbsp;&nbsp;&nbsp;(8) uitl<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 常用工具文件 :<br>
######&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 提供常用的工具包。

####四、技术选择<br>
1.Python3.x<br>
2.selenium<br>
3.Openpyxl<br>
4.unitest<br>