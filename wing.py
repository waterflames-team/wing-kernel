# -*- coding: UTF-8 -*-

'''
准备区：
引入需要的插件和需要的数据
'''

#引入插件
import sys
import markdown

#引入文件
import config

#准备数据
global out
out = None

theme = config.theme()
server_begin = 0

'''
函数区：
命名以主题前三个字幕为准
'''
class Out():

    def out(self=None):
        sys.exit(-1)

out = Out


'''
运行区：
以sys组件读取python3 wing.py XXX中XXX部分的东西
无为激活配置生效
z为使用指南
v为版本号
'''


print('''
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│                        lingkong-wing                         │
│      gitee: https://gitee.com/lingkonggzs/lingkong-wing      │
│                  by ffxw0720 & lingkong                      │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
''')

if len(sys.argv) == 1:#无的情况
    print("激活配置生效")

    if theme=="blog_exhibition":
        from blog_exhibition import theme
    if theme=="blog_succinct":
        from blog_succinct import theme
    else:
        pass

    print("完成")
    server_begin = 1
    out.out()#退出
    


if server_begin == 0:#判断无的情况是否已经经过，避免不必要的运行错误
    
    model = sys.argv[1]#如果前面的if通过，说明有东西，那么可以开始检测后面的内容

    if model == "z":#使用指南
        print("使用指南：")
        print('''
        输入python3 wing.py XXX中XXX部分的东西
        无为激活配置生效
        z为使用指南
        v为版本号
        ''')
        out.out()#退出
    if model == "s":#提醒
        print("温馨提示：")
        print('''
        您所做的是旧版操作，
        新版启动请执行"python3 wing.py"
        ''')
        out.out()#退出
    if model == "v":#版本号
        print("版本号：")
        print('''
        目前程序开发中
        所有的开发版本都会在第三位做文章
        V2.2.57-211025
        ''')
        out.out()#退出
    else:#错误的情况
        print("请确认你的激活方式是否错误")
        out.out()#退出

else:
    pass
