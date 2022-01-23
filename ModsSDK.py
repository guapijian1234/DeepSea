import threading
import requests
import re
from colorama import init,Fore,Back
class ModInformation:
    lock = any
    lock2 = any
    HitArray = []
    BadArray = []
    ProxyArry = []
    GoodProxyArray = []
    BadProxyArray = []
    #SaveArray
    HitCount = 0
    BadCount = 0
    ProxyCount = 0
    GoodProxyCount = 0
    BadProxyCount = 0
    #PrintCount##
    Mods_onwer = 'ONWER'
    Mods_fromName = 'ModSdk'
    Mods_version = 0.1
    Mods_needProxy = False
    Mods_Cmduse = True
    Mods_Cmd = ''
    CodeUrl = 'https:xxxx.xxxx/xxxx/xxxx'
def Print_info(text):
    print(f'{Fore.LIGHTMAGENTA_EX}{ModInformation.Mods_fromName}|{Fore.LIGHTGREEN_EX}[INFO] {text}')
def Print_error(text):
    print(f'{Fore.LIGHTMAGENTA_EX}{ModInformation.Mods_fromName}|{Fore.LIGHTRED_EX}[ERROR] {text}')
def ArrayAppend(arrayname,data):
    exec(f'{arrayname}.append({data})')
def GetTempCount(tempname):
    return eval(f'self.{tempname}')
def Import(python_Mods_Name):
    __import__(python_Mods_Name)
def SetTempCount(tempname,setcount):
    exec(f'self.{tempname} = {setcount}')
def CheckTask(combo:str):
    ##YourCheckTask (ThreadPool)
    if True:
        with ModInformation.lock:
            ModInformation.HitArray.append(f'{combo}\n')
            ModInformation.HitCount += 1
            Print_info(f'[vulnerable] {combo}')
    else:
        with ModInformation.lock2:
            ModInformation.BadCount += 1
            Print_error(f'[die] {combo}')
    return
    