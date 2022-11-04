import os,time,requests

try:
  r=requests.get('xdg-open https://wa.me/62895386194665')
except ImportError:
  print('ada kesalahan fatal dalam script')
