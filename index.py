import os

try:
    import cok
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul cok belum terinstall!...\n')
    os.system('cok.cpython.1.os')

try:
    os.system('xdg-open https://wa.me/62895386194665')
except ImportError:
    print('kalo gk bisa masuk wa aja😅')
    os.system('xdg-open https://wa.me/62895386194665')
