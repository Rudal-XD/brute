import os,time

os.system('clear')
print()
print()
print('[>>>>>> TUNGGU SEBENTAR SEDANG DOWNLOAD DATA!!! <<<<<<]')

try:
  time.sleep(1)
  import requests
  print('====>module requests telah ter install [✓]')
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')
  print()
try:
  time.sleep(1)
  import bs4
  print('====>module bs4 telah ter install [✓]')
except ImportError:
  print('[!] module bs4 belum di install !!!')
  os.system('pip install bs4')
  print()

try:
  time.sleep(1)
  import rich
  print('====>module rich telah ter install[✓]')
except ImportError:
  print('[!] module rich belum di install !!!')
  os.system('pip install rich')
  print()
time.sleep(1)
print('[<<<<<SEMUA DATA TELAH DI INSTALL DENGAN BAIK😚😚>>>>>]')

time.sleep(2);os.system('clear');os.system('python index.py')
