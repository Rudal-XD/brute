import os

try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    os.system('git pull')
except ImportError:
    print('xdg-open https://google.com')
