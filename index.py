import os,time,requests,datetime,random 

import self
import rich
import bs4
import requests


def banner():
     print(f'''
     +++++++++++++++++++++++++++++++++++++++++++++
     ''')

def menu():
     banner()
     print("""
            1.menu
            2.login
            3.(exit)
            """)
     print()
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
