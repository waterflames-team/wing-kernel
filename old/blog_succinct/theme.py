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
    three = '的博客</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav mr-auto"><li class="nav-item active"><a class="nav-link" href="index.html">首页</a></li><li class="nav-item"><a class="nav-link" href="word.html">文章</a></li><li class="nav-item"><a class="nav-link" href="jieshao.html">介绍<span class="sr-only">(current)</span></a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
    three_js = '的博客</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav mr-auto"><li class="nav-item"><a class="nav-link" href="index.html">首页</a></li><li class="nav-item"><a class="nav-link" href="word.html">文章</a></li><li class="nav-item active"><a class="nav-link" href="jieshao.html">介绍<span class="sr-only">(current)</span></a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
    three_wd = '的博客</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav mr-auto"><li class="nav-item"><a class="nav-link" href="index.html">首页</a></li><li class="nav-item active"><a class="nav-link" href="word.html">文章</a></li><li class="nav-item"><a class="nav-link" href="jieshao.html">介绍<span class="sr-only">(current)</span></a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
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

    three_t ='</div></li></ul></div></nav>'

    #index_du
    three_j = '<div class="alert alert-success" role="alert"><h4 class="alert-heading">'
    #leo
    four = '的博客</h4><hr><p>欢迎来到'
    #leo
    five = '的博客</p><p>这里就是博客的首页了</p></div><hr><div class="card"><div class="card-body"><h5 class="card-title">文章</h5><h6 class="card-subtitle mb-2 text-muted"></h6><p class="card-text">查看全部文章</p><a href="word.html" class="card-link">跳转——>></a></div></div><br><div class="card"><div class="card-body"><h5 class="card-title">介绍</h5><h6 class="card-subtitle mb-2 text-muted"></h6><p class="card-text">介绍介绍'
    #leo
    six = '</p><a href="jieshao.html" class="card-link">跳转——>></a></div></div>'
    #index_du

    #jieshi_du---
    jieshi_one = '<div class="alert alert-success" role="alert"><h4 class="alert-heading">'
    #leo韩
    jieshi_two = '的博客</h4><hr><p>欢迎来到'
    #Leo韩
    jieshi_three = '的博客</p><p>这里就是'
    #Leo韩
    jieshi_four_a = '的介绍了</p></div><div class="alert alert-info" role="alert"><h4 class="alert-heading"><img src="'
    
    jieshi_four_b = '的介绍了</p></div><div class="alert alert-info" role="alert"><h4 class="alert-heading">'
    #TODO 无图
    #头像
    jieshi_five = '" alt="" width="70px" class="rounded-circle">'
    #Leo韩
    jieshi_six = '</h4><hr><p>'
    #个人介绍
    jieshi_seven = '</p></div>'
    #jieshi_du---

    #wd_du---
    wd_one = '<div class="alert alert-success" role="alert"><h4 class="alert-heading">'
    #Leo韩
    wd_two = '的博客</h4><hr><p>欢迎来到'
    #Leo
    wd_three = '的博客</p><p>这里就是博客的文章汇集地了</p></div><div class="row">'
    
    ##-wdxh-
    wd_lb_one = '<div class="col-sm-6" style="margin: 10 0 0 0"><div class="card"><div class="card-body"><h5 class="card-title">'
    #题目
    wd_lb_two = '</h5><p class="card-text">'
    #概要
    wd_lb_three = '</p><a href="'
    #id(.html)
    wd_lb_four = '" class="btn btn-primary">查看</a></div></div></div>'
    ##-wdxh-

    wd_four = '</div>'
    #wd_du---

    #word_du---
    #直接进循环
    word_one = '<div class="alert alert-success" role="alert"><h4 class="alert-heading">'
    #标题
    word_two = '</h4><hr><p>'
    #简述
    word_three = '</p></div><div class="container-fluid"><div class="row"><main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4"><div data-spy="scroll" data-target="#navbar-example3" data-offset="0"><p>'
    #内容
    word_four = '</p></div></main></div></div>'
    #word_du---

    six_t = '<br><hr><footer class="bd-footer text-muted"><div class="container-fluid p-3 p-md-5"><p>© 2020 '
    #leo
    seven = ' | Make by wing<div class="d-flex align-items-center"><a href="#top" target="_self">返回顶部</a></div></p></div></footer><!--head、small--></div></div></div><!--head、small--><script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script></body></html>'

    #取数据判定
    which = Which
    if which==1:
        return one
    if which==2:
        return two

    #nav
    if which==3:
        return three
    if which=="3_js":
        return three_js
    if which=="3_wd":
        return three_wd
    #nav

    if which==31:
        return three_o

    #friend
    if which=="f_1":
        return friend_one
    if which=="f_2":
        return friend_two
    if which=="f_3":
        return friend_three
    #friend

    if which==32:
        return three_t

    #index_du
    if which==33:
        return three_j
    if which==4:
        return four
    if which==5:
        return five
    if which==6:
        return six
    #index_du

    #jieshao_du
    if which=="js_1":
        return jieshi_one
    if which=="js_2":
        return jieshi_two
    if which=="js_3":
        return jieshi_three
    if which=="js_4_a":
        return jieshi_four_a #有图
    if which=="js_4_b":
        return jieshi_four_b #无图
    if which=="js_5":
        return jieshi_five
    if which=="js_6":
        return jieshi_six
    if which=="js_7":
        return jieshi_seven
    #jiehsao_du
    
    #wd_du
    if which=="wd_1":
        return wd_one
    if which=="wd_2":
        return wd_two
    if which=="wd_3":
        return wd_three

    if which=="lb_1":
        return wd_lb_one
    if which=="lb_2":
        return wd_lb_two
    if which=="lb_3":
        return wd_lb_three
    if which=="lb_4":
        return wd_lb_four

    if which=="wd_4":
        return wd_four
    #wd_du
    #word_du
    if which=="word_1":
        return word_one
    if which=="word_2":
        return word_two
    if which=="word_3":
        return word_three
    if which=="word_4":
        return word_four
    #word_du

    if which==62:
        return six_t
    if which==7:
        return seven
    else:
        print("错误：调用出错！！！")


#执行部分

theme_e = "blog_succinct"
print("检测到主题blog_succinct")

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
index(32),
index(33),user,index(4),user,index(5),user,index(6),
index(62),user,index(7)
]

write_all = ''.join(parts)
write_all = str(write_all)
f.write(write_all)
f.close()


'''
jieshao
'''
j = open("web/jieshao.html","w+",encoding = "utf-8")

#TODO 这里是图片加入的部分

if photo == "#":

    print("无图")

    js = [
    index(1),user,index(2),user,index("3_js"),config.config_two(theme_e,"right","name"),index(31),
    friend,
    index(32),
    index("js_1"),user,index("js_2"),user,index("js_3"),user,index("js_4_b"),user,index("js_6"),introduce,index("js_7"),
    index(62),user,index(7)
    ]

else:
    js = [
    index(1),user,index(2),user,index("3_js"),config.config_two(theme_e,"right","name"),index(31),
    friend,
    index(32),
    index("js_1"),user,index("js_2"),user,index("js_3"),user,index("js_4_a"),photo,index("js_5"),user,index("js_6"),introduce,index("js_7"),
    index(62),user,index(7)
    ]

g_js = ''.join(js)
g_js = str(g_js)
j.write(g_js)
j.close()


'''
word
'''

ld = True
lb = " "
wd = " "

while ld==True:#文章循环
    #列表
    lb = str(str(index("lb_1")+config.config_three(theme_e,"word",str(word_max),"title")+index("lb_2")+config.config_three(theme_e,"word",str(word_max),"generalization")+index("lb_3")+str(word_max)+'.html'+index("lb_4"))+lb)
    #文章
    j = open("web/"+str(word_max)+".html","w+",encoding = "utf-8")

    word_md = open(theme_e+"/word/"+config.config_three(theme_e,"word",str(word_max),"from"),'r',encoding = "utf-8")
    word_md_nr = word_md.read()
    word_nr = markdown.markdown(word_md_nr, output_format='html5', extensions=['extra'])
    word_md.close()

    js = [
    index(1),user,index(2),user,index("3_wd"),config.config_two(theme_e,"right","name"),index(31),
    friend,
    index(32),
    index("word_1"),config.config_three(theme_e,"word",str(word_max),"title"),index("word_2"),config.config_three(theme_e,"word",str(word_max),"generalization"),index("word_3"),word_nr,index("word_4"),
    index(62),user,index(7)
    ]

    g_js = ''.join(js)
    g_js = str(g_js)
    j.write(g_js)
    j.close()
    #判定
    word_max = word_max-1

    if word_max==0:
        ld=False


j = open("web/word.html","w+",encoding = "utf-8")

js = [
index(1),user,index(2),user,index("3_wd"),config.config_two(theme_e,"right","name"),index(31),
friend,
index(32),
index("wd_1"),user,index("wd_2"),user,index("wd_3"),lb,index("wd_4"),
index(62),user,index(7)
]


g_js = ''.join(js)
g_js = str(g_js)
j.write(g_js)
j.close()

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