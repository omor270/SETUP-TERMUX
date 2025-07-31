
import os,sys,time

def omor(ab):
	for x in ab:
		
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.1)
		
os.system("clear")

# Show your Facebook ID at the top
omor("\033[1;36m\n\n\n      Follow Developer Facebook ID: \n")
time.sleep(0.1)

os.system("xdg-open https://www.facebook.com/omor270")
os.system("clear")

omor("\n\n\n     \033[1;32mSystem Loding...")
os.system("clear")								
omor("\n\n\n     \033[1;31mSystem Loding Successfully....\n ")

ab= input("    \033[1;33mYour Name; ")

omor(f"     \033[1;34mHay Ehical {ab};")

os.system("clear")	

print("""\033[1;35m
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

 ██████  ███    ███  ██████  ██████  
██    ██ ████  ████ ██    ██ ██   ██ 
██    ██ ██ ████ ██ ██    ██ ██████  
██    ██ ██  ██  ██ ██    ██ ██   ██ 
 ██████  ██      ██  ██████  ██   ██ 
   

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[≋] DEVELOPER  :   MD OMOR FARUK
[≋] FACEBOOK   : HM OMOR
[≋] GITHUB   :   omor270
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")



# Termux packages
print("\033[1;34m")
os.system("pkg update -y && pkg upgrade -y")
os.system("pkg install -y bash zsh proot termux-tools")
os.system("pkg install -y clang make cmake automake autoconf")
os.system("pkg install -y python python2 ruby perl nodejs")
os.system("pkg install -y curl wget openssh inetutils net-tools nmap")
os.system("pkg install -y zip unzip tar p7zip")
os.system("pkg install -y git nano vim")
os.system("pkg install -y figlet toilet neofetch cmatrix proot-distro")

# Python pip upgrade and modules
print("\033[1;32m")
os.system("pip install --upgrade pip")
os.system("pip install requests bs4 lxml colorama pyfiglet termcolor scapy rich flask")

# Ruby gem
print("\033[1;36m")
os.system("gem install lolcat")



# Useful tools for hacking & dev
print("\033[1;37m")
os.system("pkg install -y openssl tsu dnsutils termux-api")
os.system("pkg install -y gnupg openssh-dev")
os.system("pkg install -y hydra sqlmap")
os.system("pkg install -y python3-pip")

# Extra tools
print("\033[1;38m")
os.system("pkg install -y tree htop lsof man grep")
os.system("pkg install -y nodejs-lts")

# Optional but useful
print("\033[1;34m")

os.system("pip install tqdm httpx")
os.system("pip install speedtest-cli")
os.system("pkg install -y golang")

omor("\033[1;35mYou Successfully Completed Termux Full Setup!")