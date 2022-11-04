import os,time,requests

try:
  r=requests.get('https://google.com')
except ImportError:
  print('error')
