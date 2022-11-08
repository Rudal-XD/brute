import os
try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import bs4
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Rich belum terinstall!...\n')
    os.system('pip install rich')
#################################################################################
from cok import brute

if __name__ == '__main__':
    os.system("git pull");os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...");os.system("rm -rf results/IG/OK/...");os.system("rm -rf results/IG/CP/...")
   # os.system("clear")
   # print("please wait....")
   # print()
   # print("script sedang dalam perbaikan..")
   # exit()
    brute()
