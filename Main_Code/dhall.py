# -*- coding: utf-8 -*-
import os,sys
from os import system
import random
from time import sleep
from core.tools import *
os.system('clear')
def ban():
  print ('''\033[91m┌───────────────────────────────────────────────┐
│                                               │
│     ██████╗ ██╗  ██╗       █████╗ ██╗         │
│     ██╔══██╗██║  ██║      ██╔══██╗██║         │
│     ██║  ██║███████║█████╗███████║██║         │
│     ██║  ██║██╔══██║╚════╝██╔══██║██║         │
│     ██████╔╝██║  ██║      ██║  ██║███████╗    │
│     ╚═════╝ ╚═╝  ╚═╝      ╚═╝  ╚═╝╚══════╝    │
│                            \033[93m Version : 1.0\033[91m     │
└───────────────────────────────────────────────┘

         \033[0m \033[0;37;41m Termux All Tool Installer\033[0m

''')
ban()
def dh():
  print ('\033[92m_' *50)
  print ('\n')
  print (' \033[96m Author   : \033[95m Dark Hunter 141')
  print (' \033[96m Github   : \033[95m https://github.com/DH-AL/')
  print (' \033[96m Coded By : \033[95m Naiyan AR Rahman')
  print (' \033[96m           \033[95m  Ashrafi Abir')
  print ('\n')
  print ('\033[92m_' *50)
  print ('\n')
dh()

def main():
  print ("\033[91m[\033[0m1\033[91m] \033[93m  Phishing Tools")
  print ("\033[91m[\033[0m2\033[91m] \033[93m  Brute Forcing Tools")
  print ("\033[91m[\033[0m3\033[91m] \033[93m  Cloning Tools")
  print ("\033[91m[\033[0m4\033[91m] \033[93m  Vulnerability Scanning Tools")
  print ("\033[91m[\033[0m5\033[91m] \033[93m  Information Gathering Tools")
  print ("\033[91m[\033[0m6\033[91m] \033[93m  Tracing and Tracking Tools")
  print ("\033[91m[\033[0m7\033[91m] \033[93m  Exploitation Tools")
  print ("\033[91m[\033[0m8\033[91m] \033[93m  Password Cracking Tools")
  print ("\033[91m[\033[0m9\033[91m] \033[93m  Wifi Hacking Tools")
  print ("\033[91m[\033[0m10\033[91m] \033[93m Bombing Tools")
  print ("\033[91m[\033[0m11\033[91m] \033[93m DDOS Tools")
  print ("\033[91m[\033[0m12\033[91m] \033[93m Malware Tools")
  print ("\033[91m[\033[0m13\033[91m] \033[93m Termux Special Packages")
  print ("\033[91m[\033[0m14\033[91m] \033[93m Another Hacking Tools")
  print ("\033[91m[\033[0m15\033[91m] \033[93m Kali Linux Installer")
  print ("\033[91m[\033[0m16\033[91m] \033[93m Metasploit Installer")
  print ("\033[91m[\033[0m17\033[91m] \033[93m Advanced Web Application Penetration Tester")
  print ("\033[91m[\033[0m18\033[91m] \033[93m Help")
  print ("\033[91m[\033[0m00\033[91m] \033[93m Exit")
  print ('\n')
main()
def Anon():
  try:
   
   x =input( '\033[92m[!] Enter Your Options :\033[96m ')
  except KeyboardInterrupt:
   print(O)
   exit()
  system("clear")
  if x == "1" or x == "01":
     Phish()
     Restart()
  elif x == "2" or x == "02":
     Brute()
     Restart()
  elif x == "3" or x == "03":
     Clone()
     Restart()
  elif x == "4" or x == "04":
     Vuln()
     Restart()
  elif x == "5" or x == "05":
     Info()
     Restart()
  elif x == "6" or x == "06":
     Trac()
     Restart()
  elif x == "7" or x == "07":
     Exp()
     Restart()
  elif x == "8" or x == "08":
     Pass()
     Restart()
  elif x == "9" or x == "09":
     Wifi()
     Restart()
  elif x == "10":
     Bom()
     Restart()
  elif x == "11":
     DDOS()
     Restart()
  elif x == "12":
     Mal()
     Restart()
  elif x == "13":
     Special()
     Restart()
  elif x == "14":
     Ano()
     Restart()
  elif x == "15":
     os.system('cd $HOME && git clone https://github.com/darkhunter141/kkali-installer')
  elif x == "16":
     os.system('cd $HOME && git clone https://github.com/darkhunter141/metasploit-installer')
  elif x == "17":
     os.system('cd $HOME && pkg install python2 && git clone https://github.com/darkhunter141/Web-Hunter && cd Web-Hunter && python2 menu.pypkg install python2 && git clone https://github.com/darkhunter141/Web-Hunter')
  elif x == "18":
     os.system('cat README.md')
     input('\033[91m Press Entet To Back Main Menu')
     os.system('python dhall.py')
  elif x == "0" or x == "00":
     os.system('xdg-open https://github.com/DH-AL/')
     exit()
  else:
     BackToMenu()
Anon()
