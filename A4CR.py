import os,time,platform

print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)

os.system('git pull')

os.system('xdg-open https://www.facebook.com/profile.php?id=100085565361943')

logo = ("""\033[1;37m       d8888     d8888   .d8888b.  8888888b.  

                 d88888    d8P888  d88P  Y88b 888   Y88b 

                d88P888   d8P 888  888    888 888    888 

               d88P 888  d8P  888  888        888   d88P 

              d88P  888 d88   888  888        8888888P"  

             d88P   888 8888888888 888    888 888 T88b   

            d8888888888       888  Y88b  d88P 888  T88b  

           d88P     888       888   "Y8888P"  888   T88b 

                                                         

(!)══════════════════════════════════════════

(!) Author   : IMTIAZ AKING

(!) Guthub   : AKING110

(!) Facebook : MR.AKING.07

(!) Type     : FREE

(!) Version  : 1.2.1

\033[1;37m(!)══════════════════════════════════════════""")

def Run():

	bit = platform.architecture()[0]	os.system('clear')

	print(logo)

	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')

	print('[1] FILE CLONE \n[2] RANDOM CLONE\n[0] Exit')

	Aking = input('[•] Choose : ')

	if Aking =='1':

		if bit =='32bit':

			import FILE.py

		elif bit =='64bit':

			import FILE.py

	elif Aking =='2':

		if bit =='32bit':

			import RNDM.py

		elif bit =='64bit':

			import RNDM.py

Run()
