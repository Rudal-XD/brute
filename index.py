import os,time,requests,datetime,random 

import rich
import bs4
import requests

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU,
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE

def banner():
     print(f'''
╭━━•›ꪶ ཻུ۪۪ꦽꦼ̷⸙ ━ ━ ━ ━ ꪶ ཻུ۪۪ꦽꦼ̷⸙‹•━━╮
┃╭┈─────────────⩵꙰ཱི࿐
┃╰── ⏤͟͟͞GOOD BYE ──➤ ↶↷
╰━━•›ꪶ ཻུ۪۪ꦽꦼ̷⸙ ━ ━ ━ ━ ꪶ ཻུ۪۪ꦽꦼ̷⸙‹•━━͙✩̣̣̣̣
 ▬▭▬▭▬ ✦✧✦ ▬▭▬▭▬
╭━━•›〘 STATUS 〙
│➳ LEAVING FROM
│➳ ${metadata.subject}
╰━ ━ ━ ━ ━ ━ ━ ━ ━ ━•⩵꙰ཱི࿐
 ▬▭▬▭▬ ✦✧✦ ▬▭▬▭▬
╭━━•›〘 SUBSCRIBE 〙
│➳ Channel YouTube
│➳ FARIZ MODS
│➳ https://youtube.com/channel/UCmfGOnP_M0ucKN8Y5Y4yBOQ
╰━ ━ ━ ━ ━ ━ ━ ━ ━ ━•⩵꙰ཱི࿐
 ▬▭▬▭▬ ✦✧✦ ▬▭▬▭▬

© FARIZ V5
     ''')

def menu():
     banner()
     print("""
            1.menu
            2.login
            3.(exit)
            """)
     print('error')
     self.pilih()

def pilih(self):
   print()
   usna = input('choose:')
   if usna in ['']:
       print('masukan nomer nya')
   elif usna in ['1']:
       print()
       r=requests.get('https://google.com')
   else:
       exit()
      


if __name__ == "__main__":
  os.system('git pull');os.system('clear')
  #print('loading')
  #print()
  print()
  menu()
  print()
