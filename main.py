import pywhatkit as kit
import webbrowser
import wikipedia
import pyjokes
import datetime

def initializer():
    print("Welcome to oversight ............")
    print("Type command ..........")
    global command
    command = input()
    
def progress():
    print("Type command ..........")
    global command,yt_dl_cmd,yt_auth_cmd,wk_sr_cmd,jk_gt_cmd , dt_gt_cmd
    command = input()
    
    yt_dl_cmd = "-ovr .yt-dl"
    yt_auth_cmd = "-ovr .yt-pl"

     
    wk_sr_cmd = "-ovr .wk-sr"

    jk_gt_cmd = "-ovr .jk-get"

    dt_gt_cmd = "-ovr .dt"
    
initializer()
yt_dl_cmd = "-ovr .yt-dl"
yt_auth_cmd = "-ovr .yt-pl"

 
wk_sr_cmd = "-ovr .wk-sr"

jk_gt_cmd = "-ovr .jk-get"

dt_gt_cmd = "-ovr .dt"


if yt_dl_cmd in command:
    url = command.replace(yt_dl_cmd,"").strip()
    webbrowser.open(url[:12] + "ss" + url[12:])
    progress()
    
if yt_auth_cmd in command:
    vid = command.replace(yt_auth_cmd,"").strip()
    kit.playonyt(vid)
    progress()

if wk_sr_cmd in command:
    sr_q = command.replace(wk_sr_cmd,"")
    print(wikipedia.summary(sr_q,1))
    progress()
    
