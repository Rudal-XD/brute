import os

try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    os.system('xdg-open https://wa.me/62895386194665+opo')
except ImportError:
    print('kalo gk bisa masuk wa aja😅')
    os.system('xdg-open https://wa.me/62895386194665+error+bang')
