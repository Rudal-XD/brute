import os

try:
  import request 
  print('module requests telah ter install')
  import cok
except ImportError:
  print('[!] module requests belum di install !!!')
  os.system('pip install requests')
  
