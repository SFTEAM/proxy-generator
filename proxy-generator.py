import sys
import requests 
import os
import time
import colorama
from colorama import Fore
from time import sleep
from sys import platform

os.system("cls & title proxy generator made by mkay")

Times = 1
Choice = input(f"[{Fore.YELLOW}INPUT{Fore.RESET}] (1)http/s (2) socks4 (3) socks5: ")
if Choice == "1":
           Url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

elif Choice == "2":

		Url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"

elif Choice == "3":

    Url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"

else:
    print(f"[{Fore.RED}ERROR{Fore.RESET}] Invalid syntax.")
    exit(0)
while 1:
    r = requests.get(Url)
    append = open("proxys.txt", "a")
    print(f"[{Fore.GREEN}SUCCESS{Fore.RESET}] Fresh proxy list has been found and scraped.")
    append.write(r.text)
    Times = Times + 1
    time.sleep(60)
    if platform == "linux" or "darwin":
        os.system("clear")
    else:
        os.system("cls")

# tool developed by mkay