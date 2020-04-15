'''
准备区：
引入需要的插件和需要的数据
'''

#引入插件
import sys

#引入文件
import con

#准备文件
theme = con.theme()

'''
函数区：
命名以主题前三个字幕为准
'''

def exh():
    print("检测到主题blog-exhibition")


'''
运行区：
以sys组件读取python3 wing.py XXX中XXX部分的东西
s为激活配置生效
z为使用指南
v为版本号
无为介绍同时打开后台的服务器
'''

print("欢迎使用wing")

#无的情况
if len(sys.argv) == 1:
    print("介绍")#同时打开后台服务器
    sys.exit(-1)#退出
    
model = sys.argv[1]#如果前面的if通过，说明有东西，那么可以开始检测后面的内容

if model == "s":
    print("激活配置生效")
    sys.exit(-1)#退出
if model == "z":
    print("使用指南")
    sys.exit(-1)#退出
if model == "v":
    print("版本号")
    sys.exit(-1)#退出
else:
    print("请确认你的激活方式是否错误")
    sys.exit(-1)#退出