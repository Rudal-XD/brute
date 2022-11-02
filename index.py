import os

try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import nodejs
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul nodejs belum terinstall!...\n')
    os.system('apt install nodejs')

try:
    import mechanize
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul mechanize belum terinstall!...\n')
    os.system('pip install mechanize')


from cok import brute

if __name__ == '__main__':
     os.system('git pull');os.system('clear')
