'''
准备区：
引入需要的插件和需要的数据
'''

#引入插件
import sys

#引入文件
import con

#准备数据
global out
out = None

theme = con.theme()
server_begin = 0

'''
函数区：
命名以主题前三个字幕为准
'''
class Out():

    def out(i=1):
        i_o = i
        if i_o == 1:
            sys.exit(-1)
        else:
            pass
out = Out

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

if len(sys.argv) == 1:#无的情况
    print("介绍")#同时打开后台服务器
    print('''
    灵翼是一个由非凡小王开发，折腾调协助维护的基于python3语言的一键建站系统
    您运行此步同时会启动后台
    如要关闭请按ctrl+4
    ''')
    server_begin = 1


if server_begin == 0:#判断无的情况是否已经经过，避免不必要的运行错误
    
    model = sys.argv[1]#如果前面的if通过，说明有东西，那么可以开始检测后面的内容

    if model == "s":#配置生效
        print("激活配置生效")
        out.out()#退出
    if model == "z":#使用指南
        print("使用指南：")
        print('''
        输入python3 wing.py XXX中XXX部分的东西
        s为激活配置生效
        z为使用指南
        v为版本号
        无为介绍同时打开后台的服务器
        ''')
        out.out()#退出
    if model == "v":#版本号
        print("版本号：")
        print('''
        目前程序开发中
        所有的开发版本都会在第三位做文章
        开发版本0.0.12（01版将完成部分东西的修改，不支持新增文章，02将重构)
        ''')
        out.out()#退出
    else:#错误的情况
        print("请确认你的激活方式是否错误")
        out.out()#退出

else:
    pass


