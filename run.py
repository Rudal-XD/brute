import os,time


os.system('clear')
print()
print()
print('[>>>>>> TUNGGU SEBENTAR SEDANG DOWNLOAD DATA!!! <<<<<<]')


try:
  import bash
  print('====>module bash telah ter install [✓]')
except ImportFinally:
  print('====>Module bash succes ter install [✓]')
except ImportError:
  print('====>module bash blm terinstall [X]')
  os.system('pip install bash')

try:
  time.sleep(1)
  import requests
  print('====>module requests telah ter install [✓]')
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')
try:
  time.sleep(1)
  import bs4
  print('====>module bs4 telah ter install [✓]')
except ImportError:
  print('[!] module bs4 belum di install !!!')
  os.system('pip install bs4')

try:
  time.sleep(1)
  import rich
  print('====>module rich telah ter install[✓]')
except ImportError:
  print('[!] module rich belum di install !!!')
  os.system('pip install rich')


time.sleep(1)
print('[<<<<<SEMUA DATA TELAH DI INSTALL DENGAN BAIK😚😚>>>>>]')

time.sleep(2);os.system('clear');os.system('python index.py')
