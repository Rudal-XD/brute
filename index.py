import os

try:
  import rich
except ImportError:
  print('[!] module rich belum di install !!!')
  os.system('pip install rich')
  
def main():
  os.system('python run.py')
