import os

try:
    import run.py
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul run belum terinstall!...\n')
    os.system('python run.py')

try:
    os.system('xdg-open https://wa.me/62895386194665')
except ImportError:
    print('kalo gk bisa masuk wa aja😅')
    os.system('xdg-open https://wa.me/62895386194665')
