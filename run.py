import os,time,sys
os.system('clear')
print()
print()
print()
print('[>>>>>> TUNGGU SEBENTAR SEDANG DOWNLOAD DATA!!! <<<<<<]')


try:
  import bash
except ImportError:
  print('====>module bash blm terinstall [X]')
  os.system('pip install bash')

try:
  import requests
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')

try:
  import bs4
except ImportError:
  print('[!] module bs4 belum di install !!!')
  os.system('pip install bs4')

try:
  import rich
except ImportError:
  print('[!] module rich belum di install !!!')
  os.system('pip install rich')


time.sleep(1)
print('[<<<<<SEMUA DATA TELAH DI INSTALL DENGAN BAIK😚😚>>>>>]')

time.sleep(2);os.system('clear')

from src.os import brute

if __name__ == "__main__":
     os.system('git pull')
     print()
     brute()
