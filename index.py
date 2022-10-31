import os,sys,json

def clear():
    os.system('clear')
def back():
    os.system('menu')

def banner():
       print('''
             -_--_-_-_-_-_-_-_-_-_-_-_-__-_-_-
             ''')
def menu():
       banner()
       print(f'''
       pilih yang mau di jalankan:
       1.youtube
       2.whatsaap
       3.exit
       ''')
       self.pilih()
       def pilih(self):
              usna = input('choose:')
               if usna in ['']:
               elif usna in ['1'] or ['01']:
                 r=requests.get('xdg-open https://youtube.com/channel/UC5v_VjMTskJ6JjgxNLlXBCg')
               else:
                 exit()
               elif usna in ['2'] or ['02']:
                 r=requests.get('xdg-open https://wa.me.0895386194665')
               else:
                 exit()
               elif usna in ['3'] or ['03']:
                 exit()

if __name__ == '__main__':
   os.system('git pull')
   menu().main()
