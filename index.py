import os
import sys
import rich

try:
   print('male or female')
   print()
   r=requests.get('https://google.com')
except IOError:
   print('jangan kosong kak')
   os.system('git pull')
