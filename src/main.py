import os,sys,date,time

def banner():
     banner('bang kok Lo kocak sih')

def main():
     banner()
     print(f'''
            1.menu
            2.main
            3.[exit]
            ''')
            self.pilih()

     def pilih(self):
        usna = input('nomor:')
        print()
        if usna in ['']:
        print()
        elif usna in ['1']:
            try:
              import rich
              print('module telah di install')
            except ImportError:
              print('module blm di install')
              os.system('pip install rich')
        
       elif usna in ['2']:
            exit()

if __name__ == "__main__":
     down()
     done()
