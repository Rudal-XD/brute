import os

try:
  import request 
  print('module requests telah ter install')
  import cok
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')
  
try:
  import bs4
  print('module requests telah ter install')
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install bs4')
  

try:
  import rich
  print('module rich telah ter install')
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install rich')
  
