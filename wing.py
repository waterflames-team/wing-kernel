'''
准备区：
引入需要的插件和需要的数据
'''

#引入插件
import sys
import re

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


def exh(theme):
    theme_e = theme
    from blog_exhibition import theme
    print("检测到主题blog-exhibition")

    '''
    主题blog-exhibition的准备区：
    '''

    #用户自定义数据
    user = con.config_one(theme_e,"user")
    photo = con.config_one(theme_e,"photo")
    introduce = con.config_one(theme_e,"introduce")
    word_max = int(con.config_two(theme_e,"word","max"))

    if word_max == 1:
        title = con.config_three(theme_e,"word","1","title")
        date = con.config_three(theme_e,"word","1","date")
        content = con.config_three(theme_e,"word","1","content")
        word_modle = 0
    else:
        '''
        title_one = con.config_three(theme_e,"word","1","title")
        date_one = con.config_three(theme_e,"word","1","date")
        content_one = con.config_three(theme_e,"word","1","content")
        '''
        word_modle = 1
        pass

    friend_max = int(con.config_three(theme_e,"right","friend","max"))
    if friend_max == 1:
        name = con.config_four(theme_e,"right","friend","1","name")
        f_from = con.config_four(theme_e,"right","friend","1","from")
        friend_modle = 0
    else:
        friend_modle = 1
        pass

    #模板数据
    write_one = theme.write_one()
    write_two = theme.write_two()
    write_three = theme.write_three()
    write_four = theme.write_four()
    write_five = theme.write_five()
    write_six = theme.write_six()
    write_seven = theme.write_seven()

    '''
    主题blog-exhibition的合成区：
    把用户自定义的数据和原来的index组成在一起变成网页写入到index.html
    同时这么做方便进行文章、右侧菜单的增加
    '''
    f = open("index.html","w+")
    parts = [write_one,user,write_two,user,write_three,user,write_four,photo,write_five,user,write_six,introduce]
    write_all = ''.join(parts)
    write_all = str(write_all)
    f.write(write_all)
    f.close()

'''
运行区：
以sys组件读取python3 wing.py XXX中XXX部分的东西
s为激活配置生效
z为使用指南
v为版本号
无为介绍
'''


print('''
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│                           wing                               │
│      gitee: https://gitee.com/lingkonggzs/lingkong-wing      │
│                  by ffxw0720 & lingkong                      │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
''')

if len(sys.argv) == 1:#无的情况
    print("介绍")
    print('''
    灵翼是一个由非凡小王开发，折腾调协助维护的基于python3语言的一键建站系统
    ''')
    server_begin = 1


if server_begin == 0:#判断无的情况是否已经经过，避免不必要的运行错误
    
    model = sys.argv[1]#如果前面的if通过，说明有东西，那么可以开始检测后面的内容

    if model == "s":#配置生效
        print("激活配置生效")

        if theme=="blog_exhibition":
            exh(theme)
        else:
            pass

        print("完成")
        out.out()#退出
    if model == "z":#使用指南
        print("使用指南：")
        print('''
        输入python3 wing.py XXX中XXX部分的东西
        s为激活配置生效
        z为使用指南
        v为版本号
        ''')
        out.out()#退出
    if model == "v":#版本号
        print("版本号：")
        print('''
        目前程序开发中
        所有的开发版本都会在第三位做文章
        开发版本0.0.20（01版将完成部分东西的修改,新增文章,新建右侧栏,02将根据用户体验新增其他功能，并且开始制作server版)
        ''')
        out.out()#退出
    else:#错误的情况
        print("请确认你的激活方式是否错误")
        out.out()#退出

else:
    pass


