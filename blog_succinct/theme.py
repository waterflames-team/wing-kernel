# -*- coding: UTF-8 -*-
import config
import markdown

#模板数据部分

def index(Which):

    #定义数据

    #取数据判定
    which = Which
    if which==1:
        pass
    else:
        print("错误：调用出错！！！")

#执行部分

theme_e = "blog_exhibition"
from blog_exhibition import theme
print("检测到主题blog-exhibition")

'''
主题blog-exhibition的准备区：
'''

#用户自定义数据
user = config.config_one(theme_e,"user")
photo = config.config_one(theme_e,"photo")
introduce = config.config_one(theme_e,"introduce")
word_max = int(config.config_two(theme_e,"word","max"))
friend_max = int(config.config_two(theme_e,"right","max"))



'''
主题blog-exhibition的合成区：
把用户自定义的数据和原来的index组成在一起变成网页写入到index.html
同时这么做方便进行文章、右侧菜单的增加
'''


f = open("index.html","w+",encoding = "utf-8")


'''原生成方法

hh = True
word = " "

while hh==True:

    word_md = open(theme_e+"/word/"+config.config_three(theme_e,"word",str(word_max),"from"),'r',encoding = "utf-8")
    word_md_nr = word_md.read()
    word_nr = markdown.markdown(word_md_nr, output_format='html5', extensions=['extra'])
    word_md.close()

    word = word+str(write_word_one+config.config_three(theme_e,"word",str(word_max),"id")+write_word_two+config.config_three(theme_e,"word",str(word_max),"title")+write_word_three+config.config_three(theme_e,"word",str(word_max),"date")+write_word_four+word_nr+write_word_five)
    word_max = word_max-1

    if word_max==0:
        hh=False

fj = True
friend = " "
right_zt = 0

right = str(right_one+config.config_two(theme_e,"right","name")+right_two)

while fj==True:
  
    friend = str(str(right_friend_one+config.config_three(theme_e,"right",str(friend_max),"from")+right_friend_two+config.config_three(theme_e,"right",str(friend_max),"name")+right_friend_three)+friend)
    friend_max = friend_max-1

    if friend_max==0:
        fj=False


right_ru = right+friend

nb = True
r_word = " "
word_max = int(config.config_two(theme_e,"word","max"))

while nb==True:
            
    r_word = str(right_word_one_b+config.config_three(theme_e,"word",str(word_max),"id")+right_word_two+config.config_three(theme_e,"word",str(word_max),"title")+right_word_three)+r_word
    word_max = word_max-1

    if word_max==0:
        nb=False

'''

parts = [



]

write_all = ''.join(parts)
write_all = str(write_all)
f.write(write_all)
f.close()