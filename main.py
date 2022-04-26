import pywhatkit as kit
import webbrowser
import wikipedia
import pyjokes
import datetime
import random
print("[Welcome to oversight ............]")

    
yt_dl_cmd = "-ovr .yt-dl"
yt_auth_cmd = "-ovr .yt-pl"

             
wk_sr_cmd = "-ovr .wk-sr"

jk_gt_cmd = "-ovr .jk-gt"

dt_gt_cmd = "-ovr .dt"





while True:
      try:
         command = input("$")
         if yt_dl_cmd in command:
            url = command.replace(yt_dl_cmd,"").strip()
            webbrowser.open(url[:12] + "ss" + url[12:])
            continue
    
         if yt_auth_cmd in command:
            vid = command.replace(yt_auth_cmd,"").strip()
            print("Redirecting...........")
            kit.playonyt(vid)
            continue

         if wk_sr_cmd in command:
            sr_q = command.replace(wk_sr_cmd,"").strip()
            print(wikipedia.summary(sr_q,3))
            continue
         if jk_gt_cmd == command:
            jokes = pyjokes.get_jokes()
            
            print(random.choice(jokes))
            continue
      except:
         print("Command not found")
         continue









    
