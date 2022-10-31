import os,sys,json

def clear():
    os.system('clear')
    sleep(1)
def back():
    os.system('menu')

def menu():
       print(f'''
       pilih yang mau di jalankan:
       1.youtube
       2.whatsaap
       3.exit
       ''')
       self.pilih():
       def pilih(self):
              if input('choose:'):
               if  '1' or '01':
                 r=get('xdg-open https://youtube.com/channel/UC5v_VjMTskJ6JjgxNLlXBCg')
               else:
                 exit()
               if  '2' or '02':
                 r=get('xdg-open https://wa.me.0895386194665')
               else:
                 exit()
               if  '3' or '03':
                 exit()
menu()
