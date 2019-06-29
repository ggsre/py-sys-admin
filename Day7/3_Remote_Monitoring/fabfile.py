from fabric.api import *

env.hosts=["student@10.142.0.3"]
env.password='your password'

def dir():
    run('mkdir fabric')
    print('Directory named fabric has been created on your host network')

def diskspace():
    run('df')

