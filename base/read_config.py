import os
import configparser
proDir=os.path.split(os.path.realpath(__file__))[0]
configpath=os.path.join(proDir,"config.ini")
cf=configparser.ConfigParser()
cf.read(configpath)
def get_config(field,key):
    result=cf.get(field, key)
    return result
def set_config(field,key,value):
    fb=open(configpath,'w')
    cf.set(field, key, value)
    cf.write(fb)