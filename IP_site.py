from colorama import  Fore
import socket

# ===============================

User = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Mr.Tak"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.CYAN+"卐 ").lower()

try:
    ip = socket.gethostbyname(User)
    print("IP = "+ip)
except :
    print("Make sure the domain is correct !!!")

    