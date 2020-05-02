# -*- coding: UTF-8 -*-
import config
import markdown

def write_one():

    write_one = '<html><head><title>'
    return write_one

def write_two():

    write_two = '的博客</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body><!--head、small--><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><!--head、small--><br><div class="alert alert-primary" role="alert"><h4 class="alert-heading">'

    return write_two

def write_three():

    write_three = '的博客</h4><hr><p>欢迎来到'

    return write_three

def write_four():

    write_four = '的博客</p><p>这里就是博客的首页了</p></div><br><div class="alert alert-info" role="alert"><h4 class="alert-heading"><img src="'

    return write_four

def write_five():

    #https://gitee.com/ffxw0720/img/raw/master/leo.JPG
    write_five = '" alt="" width="70px" class="rounded-circle">'
   

    return write_five

def write_six():

    #Leo韩
    write_six = '</h4><hr><p>'
   
    
    return write_six
    #个人介绍


def write_seven():

    write_seven = '</p></div><div class="container-fluid"><div class="row"><main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">'
   
    return write_seven

def write_word_one():
    word_one = '<div data-spy="scroll" data-target="#navbar-example3" data-offset="0"><h1 id="'
   
    return word_one
    #id

def write_word_two():
    
    word_two = '">'
   
    return word_two
    #标题

def write_word_three():
    word_three = '</h1><h6 class="card-subtitle mb-2 text-muted">'
   
    return word_three
    #日期

def write_word_four():
    word_four = '</h6><p>'
   
    return word_four
    #内容

def write_word_five():
    word_five = '</p></div>'
   
    return word_five

def write_eight():#只做结束，不做下个的开头

    write_eight = '</main>'
   
    return write_eight

def write_nine():
    write_eight = '<nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"><hr><br>'
   
    return write_eight 

def right_one():
    right_one = '<ul class="nav flex-column"><p class="lead">'
   
    return right_one
    #友情链接

def right_two():
    right_two = '</p>'
   
    return right_two

def right_friend_one():
    right_friend_one = '<li class="nav-item"><a class="nav-link" href="'
   
    return right_friend_one
    #链接

def right_friend_two():
    right_friend_two = '"><span data-feather="home"></span>'
   
    return right_friend_two
    #友链名

def right_friend_three():
    right_friend_three = '</a></li>'
   
    return right_friend_three

def right_word_one():
    right_word_one = '<br><hr><br><ul class="nav flex-column"><p class="lead">文章跳转</p><li class="nav-item">'
   
    return right_word_one


def right_word_one_b():
    right_word_one_b = '<a class="nav-link" href="#'
    return right_word_one_b
    #id

def right_word_two():
    right_word_two = '"><span data-feather="home"></span>'
   
    return right_word_two
    #文章标题

def right_word_three():
    right_word_three = '</a></li>'
   
    return right_word_three

def right_five():
    right_word_five = '</ul></div></nav>'
   
    return right_word_five

def write_ten():
    write_ten = '</div></div><br><hr>'
   
    return write_ten

def write_ele():
    write_ele = '<footer class="bd-footer text-muted"><div class="container-fluid p-3 p-md-5"><p>© 2020 '
   
    return write_ele
    #leo韩

def write_twl():
    write_twl = ' | Make by wing<div class="d-flex align-items-center"><a href="#top" target="_self">返回顶部</a></div></p></div></footer><!--head、small--></div></div></div><!--head、small--><script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script></body></html>'
   
    return write_twl




#主要部分


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



#模板数据
write_one = write_one()
write_two = write_two()
write_three = write_three()
write_four = write_four()
write_five = write_five()
write_six = write_six()
write_seven = write_seven()

write_word_one = write_word_one()
write_word_two = write_word_two()
write_word_three = write_word_three()
write_word_four = write_word_four()
write_word_five = write_word_five()
write_eight = write_eight()
write_nine = write_nine()

right_one = right_one()
right_two = right_two()
right_friend_one = right_friend_one()
right_friend_two = right_friend_two()
right_friend_three = right_friend_three()

right_word_one = right_word_one()
right_word_one_b = right_word_one_b()
right_word_two = right_word_two()
right_word_three = right_word_three()
right_five = right_five()
write_ten = write_ten()
write_ele = write_ele()
write_twl = write_twl()

'''
主题blog-exhibition的合成区：
把用户自定义的数据和原来的index组成在一起变成网页写入到index.html
同时这么做方便进行文章、右侧菜单的增加
'''


f = open("web/index.html","w+",encoding = "utf-8")

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

parts = [

write_one,user,write_two,user,write_three,user,write_four,photo,write_five,user,write_six,introduce,#介绍
write_seven,#总文章的开始
word,
write_eight,write_nine,
right_ru,
right_word_one,
r_word,
right_five,write_ten,write_ele,user,write_twl

]

write_all = ''.join(parts)
write_all = str(write_all)
f.write(write_all)
f.close()