# -*- coding: UTF-8 -*-
import json

def theme():

    conf_z = open("theme/theme.json",'r',encoding = "utf-8")
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    thing = "theme"#取xx项
    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[thing]

    return conf_jg

def config_one(theme,xiang):
    theme_c = theme
    xiang_c = xiang

    conf_z = open(theme_c+"/config.json",'r',encoding = "utf-8")
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[xiang_c]

    return conf_jg

def config_two(theme,xiang_one,xiang_two):
    theme_c = theme
    xiang_one_c = xiang_one
    xiang_two_c = xiang_two

    conf_z = open(theme_c+"/config.json",'r',encoding = "utf-8")
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[xiang_one_c][xiang_two_c]

    return conf_jg

def config_three(theme,xiang_one,xiang_two,xiang_three):
    theme_c = theme
    xiang_one_c = xiang_one
    xiang_two_c = xiang_two
    xiang_three_c = xiang_three

    conf_z = open(theme_c+"/config.json",'r',encoding = "utf-8")
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[xiang_one_c][xiang_two_c][xiang_three_c]

    return conf_jg

def config_four(theme,xiang_one,xiang_two,xiang_three,xiang_four):
    theme_c = theme
    xiang_one_c = xiang_one
    xiang_two_c = xiang_two
    xiang_three_c = xiang_three
    xiang_four_c = xiang_four

    conf_z = open(theme_c+"/config.json",'r',encoding = "utf-8")
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[xiang_one_c][xiang_two_c][xiang_three_c][xiang_four_c]

    return conf_jg