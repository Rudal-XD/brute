import os

try:
  import requests
  print('module requests telah ter install [✓]')
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')
  
try:
  sleep(1)
  import bs4
  print('module bs4 telah ter install [✓]')
except ImportError:
  print('[!] module bs4 belum di install !!!')
  os.system('pip install bs4')
  

try:
  import rich
  print('module rich telah ter install[✓]')
except ImportError:
  print('[!] module rich belum di install !!!')
  os.system('pip install rich')


os.system('clear');os.system('python run.py')
