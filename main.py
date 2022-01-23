


try:
    from time import sleep
    import requests
    import re
    import os
    import threading
    import binascii
    from argparse import ArgumentParser
    from urllib import parse
    import base64
    import lxml
    import uuid
    import subprocess
    import random
    from multiprocessing.dummy import Pool as ThreadPool
    import multiprocessing
    import sys
    import argparse
    import json
    import time
    from colorama import init,Fore,Back
    from urllib.parse import quote
except ImportError:
    print('[Error] Import Mods Error')
##import##
class Api(object):
    def __init__(self, *args):
        self.HitArray = []
        self.BadArray = []
        self.ProxyArry = []
        self.GoodProxyArray = []
        self.BadProxyArray = []
        ##SaveArray##
        self.HitCount = 0
        self.BadCount = 0
        self.ProxyCount = 0
        self.GoodProxyCount = 0
        self.BadProxyCount = 0
        ##PrintCount##
    def ArrayAppend(arrayname,data):
        exec(f'{arrayname}.append({data})')
    def GetTempCount(tempname):
        return eval(f'self.{tempname}')
    def Import(python_Mods_Name):
        __import__(python_Mods_Name)
    def SetTempCount(tempname,setcount):
        exec(f'self.{tempname} = {setcount}')
##Sdk Apis##

class Information:
    combolist = []
    proxylist = []
    modslist = []
    namelist = []
    choice = 0
    
def WalkFile(file):
    namelist = []
    for root, dirs, files in os.walk(file):
        for f in files:
            if root == f'{os.getcwd()}\Mods':  
                namelist.append(os.path.join(root, f).split('\\')[len(os.path.join(root, f).split('\\'))-1].split('.')[0])
    return namelist
def ImportMods(modlist):
    for mod in modlist:
        Information.modslist.append(__import__(f'{mod}'))
def Print_info(fromer,text):
    print(f'{Fore.LIGHTMAGENTA_EX}{fromer}|{Fore.LIGHTGREEN_EX}[INFO] {text}')
def Print_error(fromer,text):
    print(f'{Fore.LIGHTMAGENTA_EX}{fromer}|{Fore.LIGHTRED_EX}[ERROR] {text}')
def Input_info(fromer,text):
    print(f'{Fore.LIGHTMAGENTA_EX}{fromer}|{Fore.LIGHTGREEN_EX}[INPUT] {text}:',end='')
    return input()
def ReadComboList():
    Information.combolist = open('Combo.txt','r').read().split('\n')
    Print_info('Main',f'Total Import {len(Information.combolist)} lines Combo') 
def ReadProxyList():
    Information.proxylist = open('Proxy.txt','r').read().split('\n')
    Print_info('Main',f'Total Import {len(Information.proxylist)} lines Proxy') 
def Print_ModList():
    Print_info('Main',f'Total import {len(Information.namelist)} Mods')
    Print_info('Main',f'Mods List:')
    for i in range(len(Information.namelist)):
        print(f'[{i}] {Information.namelist[i]}')
def SetTitleTimer():
    while True:
        mods = Information.modslist[Information.choice].ModInformation
        os.system(f'title [{mods.Mods_fromName}] HIT/BAD:[{mods.HitCount}/{mods.BadCount}] ALL/LEFT:[{len(Information.combolist)}/{len(Information.combolist)-(mods.BadCount+mods.HitCount)}]')
        open('reuslt.txt','w',encoding='utf-8').writelines(mods.HitArray)
        sleep(2)
if __name__ == '__main__':
    init(autoreset=True)
    sys.path.append(f'{os.getcwd()}\\Mods')
    Information.namelist = WalkFile(f'{os.getcwd()}\Mods')
    ReadComboList()
    ReadProxyList()
    ImportMods(Information.namelist)
    Print_ModList()
    Information.choice = int(Input_info('Main',f'Whitch are u want to Check?'))
    try:
        Information.modslist[Information.choice].ModInformation.lock = threading.Lock()
        Information.modslist[Information.choice].ModInformation.lock2 = threading.Lock()
    except:
        pass
    
    if Information.modslist[Information.choice].ModInformation.Mods_Cmduse:
        Information.modslist[Information.choice].ModInformation.Mods_Cmd = Input_info('Main',f'What Cmd Would u Want?')
    threadnum = int(Input_info('Main',f'Pls Set Your ThreadNum'))
    pool = ThreadPool(threadnum)
    Print_info('Main',f'Mods [{Information.namelist[Information.choice]}] Start Check')
    threading.Thread(target=SetTitleTimer).start()
    pool.map(Information.modslist[Information.choice].CheckTask,Information.combolist)
    Print_info('Main',f'Mods [{Information.namelist[Information.choice]}] Check Compelte!')
    Input_info('Main',f'Input any to end..')
    #Information.modslist[0].ModsApi.CheckTask( )
    