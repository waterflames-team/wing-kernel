# -*- coding: UTF-8 -*-
import config
import markdown

#模板数据部分

def index(Which):

    #定义数据
    one = '<html><head><title>'
    #Leo
    two = '的博客</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body><!--head、small--><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><div class="container-fluid"><div class="row"><nav class="col-md-2 d-none d-md-block bg-light sidebar"><div class="sidebar-sticky"></div></nav></div><!--head、small--><nav class="navbar navbar-expand-lg navbar-light bg-light"><a class="navbar-brand" href="#">'
    #leo
    three = '的博客</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav mr-auto"><li class="nav-item active"><a class="nav-link" href="index.html">首页</a></li><li class="nav-item"><a class="nav-link" href="word/index.html">文章</a></li><li class="nav-item"><a class="nav-link" href="jieshao.html">介绍<span class="sr-only">(current)</span></a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
    #友情链接
    three_o = '</a><div class="dropdown-menu" aria-labelledby="navbarDropdown">'
    
    '''
    friend双页通用
    '''
    friend_one = '<a class="dropdown-item" href="'
    #链接
    friend_two = '">'
    #name
    friend_three = '</a>'
    '''
    friend双页通用
    '''

    three_t ='</div></li></ul></div></nav><div class="alert alert-success" role="alert"><h4 class="alert-heading">'
    #leo
    four = '的博客</h4><hr><p>欢迎来到'
    #leo
    five = '的博客</p><p>这里就是博客的首页了</p></div><hr><div class="card"><div class="card-body"><h5 class="card-title">文章</h5><h6 class="card-subtitle mb-2 text-muted"></h6><p class="card-text">查看全部文章</p><a href="word/index.html" class="card-link">跳转——>></a></div></div><br><div class="card"><div class="card-body"><h5 class="card-title">介绍</h5><h6 class="card-subtitle mb-2 text-muted"></h6><p class="card-text">介绍介绍'
    #leo
    six = '</p><a href="jieshao.html" class="card-link">跳转——>></a></div></div><br><hr><footer class="bd-footer text-muted"><div class="container-fluid p-3 p-md-5"><p>© 2020 '
    #leo
    seven = ' | Make by wing<div class="d-flex align-items-center"><a href="#top" target="_self">返回顶部</a></div></p></div></footer><!--head、small--></div></div></div><!--head、small--><script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script></body></html>'

    #取数据判定
    which = Which
    if which==1:
        return one
    if which==2:
        return two
    if which==3:
        return three
    if which==31:
        return three_o

    if which=="f_1":
        return friend_one
    if which=="f_2":
        return friend_two
    if which=="f_3":
        return friend_three
    
    if which==32:
        return three_t
    if which==4:
        return four
    if which==5:
        return five
    if which==6:
        return six
    if which==7:
        return seven
    else:
        print("错误：调用出错！！！")


#执行部分

theme_e = "blog_succinct"
from blog_succinct import theme
print("检测到主题blog-exhibition")

'''
准备区：
'''

#用户自定义数据
user = config.config_one(theme_e,"user")
photo = config.config_one(theme_e,"photo")
introduce = config.config_one(theme_e,"introduce")
word_max = int(config.config_two(theme_e,"word","max"))
friend_max = int(config.config_two(theme_e,"right","max"))



'''
合成区：
把用户自定义的数据和原来的index组成在一起变成网页写入到index.html
同时这么做方便进行文章、右侧菜单的增加
'''

'''
index
'''
f = open("web/index.html","w+",encoding = "utf-8")

fj = True
friend = " "

while fj==True:
  
    friend = str(str(index("f_1")+config.config_three(theme_e,"right",str(friend_max),"from")+index("f_2")+config.config_three(theme_e,"right",str(friend_max),"name")+index("f_3"))+friend)
    friend_max = friend_max-1

    if friend_max==0:
        fj=False

parts = [
index(1),user,index(2),user,index(3),config.config_two(theme_e,"right","name"),index(31),
friend,
index(32),user,index(4),user,index(5),user,index(6),index(7)
]

write_all = ''.join(parts)
write_all = str(write_all)
f.write(write_all)
f.close()



#参考
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