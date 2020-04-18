import json

def theme():

    conf_z = open("theme.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    thing = "theme"#取xx项
    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg[thing]

    return conf_jg