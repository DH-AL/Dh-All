import os,sys,random
from os import system
from time import sleep
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
W = "\033[1;37m"
O = "\033[0m"
colors = [Y,B,G,R,Y]
A = random.choice(colors)
def Phish():
    print ("""\n  {}[{}1{}]{} Evilgin2X
  {}[{}2{}]{} PhishX
  {}[{}3{}]{} HiddenEye
  {}[{}4{}]{} Shellphish
  {}[{}5{}]{} Socialfish
  {}[{}6{}]{} BlackEye
  {}[{}7{}]{} Weeman
  {}[{}8{}]{} Zphisher
  {}[{}9{}]{} NexPhisher
  {}[{}10{}]{} T-Phish
  {}[{}11{}]{} ADV-Phishing
  {}[{}12{}]{} Recreating Phishing
  {}[{}13{}]{} MrPhish
  {}[{}14{}]{} LordPhish
  {}[{}15{}]{} GoPhish
  {}[{}16{}]{} Lowbait
  {}[{}17{}]{} URL Master
  {}[{}18{}]{} FotoSploit
  {}[{}19{}]{} Phisher
  {}[{}20{}]{} Shark
  {}[{}21{}]{} MaskPhish
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
     phish = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
     print(O)
     exit()
    print(G)
    sleep(0.5)
    if phish == "1" or phish == "01":
       system("clear")
       Evilginx()
       print (" Installed Succesfully ")
    elif phish == "2" or phish == "02":
       system("clear")
       Phishx()
       print (" Installed Succesfully ")
    elif phish == "3" or phish == "03":
       system("clear")
       HiddenEye()
       print (" Installed Succesfully ")
    elif phish == "4" or phish == "04":
       system("clear")
       Shellphish()
       print (" Installed Succesfully ")
    elif phish == "5" or phish == "05":
       system("clear")
       SocialFish()
       print (" Installed Succesfully ")
    elif phish == "6" or phish == "06":
       system("clear")
       BlackEye()
       print (" Installed Succesfully ")
    elif phish == "7" or phish == "07":
       system("clear")
       weeman()
       print (" Installed Succesfully ")
    elif phish == "8" or phish == "08":
       system("clear")
       Zphisher()
       print (" Installed Succesfully ")
    elif phish == "9" or phish == "09":
       system("clear")
       Nexphisher()
       print (" Installed Succesfully ")
    elif phish == "10":
       system("clear")
       Tphish()
       print (" Installed Succesfully ")
    elif phish == "11":
       system("clear")
       ADVphishing()
       print ("Intalled Succesfully ")
    elif phish == "12":
       system("clear")
       RecreatorPhishing()
       print (" Installed Succesfully ")
    elif phish == "13":
       system("clear")
       mrphish()
       print (" Installed Succesfully ")
    elif phish == "14":
       system("clear")
       lordphish()
       print (" Installed Succesfully ")
    elif phish == "15":
       system("clear")
       gophish()
       print (" Installed Succesfully ")
    elif phish == "16":
       system("clear")
       Shellphish()
    elif phish == "17":
       system("clear")
       EvilUrl()
    elif phish == "18":
       system("clear")
       FotoSploit()
    elif phish == "19":
       system("clear")
       phisher()
    elif phish == "20":
       system("clear")
       shark()
    elif phish == "21":
       system("clear")
       maskphish()
    elif phish == "99":
       BackToMenu()
    elif phish == "0" or phish == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()



def Brute():
    print("""\n  {}[{}1{}]{} Hydra
  {}[{}2{}]{} Black-Hydra
  {}[{}3{}]{} BruteX
  {}[{}4{}]{} Facebook-cracker
  {}[{}5{}]{} Firecrack
  {}[{}6{}]{} Facebook-Bruteforce
  {}[{}7{}]{} FB-Cracker
  {}[{}8{}]{} FBbrute
  {}[{}9{}]{} FBB
  {}[{}10{}]{} BluForce-FB
  {}[{}11{}]{} Instahack
  {}[{}12{}]{} Instabrute
  {}[{}13{}]{} Instainsane
  {}[{}14{}]{} Instax
  {}[{}15{}]{} Intar
  {}[{}16{}]{} InstaShell
  {}[{}17{}]{} Bruteforce_new
  {}[{}18{}]{} BruteSpray
  {}[{}19{}]{} SocialBox-Termux
  {}[{}20{}]{} Plutus
  {}[{}21{}]{} XBruteForcer
  {}[{}22{}]{} cupp
  {}[{}23{}]{} Lazybee
  {}[{}24{}]{} Pass-Gen
  {}[{}25{}]{} P-Gen
  {}[{}26{}]{} Wordlister
  {}[{}27{}]{} Crunch
  {}[{}28{}]{} GobinWordGenerator
  {}[{}29{}]{} Indonesiun-Wordlister
  {}[{}30{}]{} password-list
  {}[{}31{}]{} Brute19
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      brute = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if brute == "1" or brute == "01":
       system("clear")
       Hydra()
       print (" Installed Succesfully ")
    elif brute == "2" or brute == "02":
       system("clear")
       BlackHydra()
       print (" Installed Succesfully ")
    elif brute == "3" or brute == "03":
       system("clear")
       Brutex()
       print (" Installed Succesfully ")
    elif brute == "4" or brute == "04":
       system("clear")
       facebookcracker()
       print (" Installed Succesfully ")
    elif brute == "5" or brute == "05":
       system("clear")
       Firecrack()
       print (" Installed Succesfully ")
    elif brute == "6" or brute == "06":
       system("clear")
       facebookbruteforce()
       print (" Installed Succesfully ")
    elif brute == "7" or brute == "07":
       system("clear")
       FBcracker()
       print (" Installed Succesfully ")
    elif brute == "8" or brute == "08":
       system("clear")
       FBbrute()
       print (" Installed Succesfully ")
    elif brute == "9" or brute == "09":
       system("clear")
       fbb()
       print (" Installed Succesfully ")
    elif brute == "10":
       system("clear")
       blueforce()
       print (" Installed Succesfully ")
    elif brute == "11":
       system("clear")
       Instahack()
       print (" Installed Succesfully ")
    elif brute == "12":
       system("clear")
       Instabrute()
       print (" Installed Succesfully ")
    elif brute == "13":
       system("clear")
       Instainsane()
       print (" Installed Succesfully ")
    elif brute == "14":
       system("clear")
       Instax()
       print (" Installed Succesfully ")
    elif brute == "15":
       system("clear")
       intar()
       print (" Installed Succesfully ")
    elif brute == "16":
       system("clear")
       Instashell()
       print (" Installed Succesfully ")
    elif brute == "17":
       system("clear")
       BRUTEFORCERnew()
       print (" Installed Succesfully ")
    elif brute == "18":
       system("clear")
       Brutespray()
       print (" Installed Succesfully ")
    elif brute == "19":
       system("clear")
       socialbox()
       print (" Installed Succesfully ")
    elif brute == "20":
       system("clear")
       plutus()
       print (" Installed Succesfully ")
    elif brute == "21":
       system("clear")
       xbruteforcer()
       print (" Installed Succesfully ")
    elif brute == "22":
       system("clear")
       cupp()
       print (" Installed Succesfully ")
    elif brute == "23":
       system("clear")
       Lazybee()
       print (" Installed Succesfully ")
    elif brute == "24":
       system("clear")
       Passgen()
       print (" Installed Succesfully ")
    elif brute == "25":
       system("clear")
       pgen()
       print (" Installed Succesfully ")
    elif brute == "26":
       system("clear")
       Wordlister()
       print (" Installed Succesfully ")
    elif brute == "27":
       system("clear")
       crunch()
       print (" Installed Succesfully ")
    elif brute == "28":
       system("clear")
       GoblinWordGenerator()
       print (" Installed Succesfully ")
    elif brute == "29":
       system("clear")
       Indonationwordlist()
       print (" Installed Succesfully ")
    elif brute == "30":
       system("clear")
       passwordlist()
       print (" Installed Succesfully ")
    elif brute == "31":
       system("clear")
       bruter19()
       print (" Installed Succesfully ")
    elif brute == "99":
       BackToMenu()
    elif brute == "0" or brute == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()


def Clone():
    print ("""\n  {}[{}1{}]{} Dark-FB
  {}[{}2{}]{} OSIF
  {}[{}3{}]{} FBI
  {}[{}4{}]{} ASU
  {}[{}5{}]{} Exif-Tool
  {}[{}6{}]{} Inshackle
  {}[{}7{}]{} BlackMafia
  {}[{}8{}]{} Instahack
  {}[{}9{}]{} InsFollow
  {}[{}10{}]{} Afgcrack
  {}[{}11{}]{} OSI-IG
  {}[{}12{}]{} Auto-IG
  {}[{}13{}]{} Lucifer
  {}[{}14{}]{} Without
  {}[{}15{}]{} Fast-clone
  {}[{}16{}]{} BXI
  {}[{}17{}]{} Sensei
  {}[{}18{}]{} Bad-Robo
  {}[{}19{}]{} ToolSig
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      clone = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if clone == "1" or clone == "01":
       system("clear")
       Darkfb()
       print (" Installed Succesfully ")
    elif clone == "2" or clone == "02":
       system("clear")
       OSIF()
       print (" Installed Succesfully ")
    elif clone == "3" or clone == "03":
       system("clear")
       FBI()
       print (" Installed Succesfully ")
    elif clone == "4" or clone == "04":
       system("clear")
       ASU()
       print (" Installed Succesfully ")
    elif clone == "5" or clone == "05":
       system("clear")
       Exiftool()
       print (" Installed Succesfully ")
    elif clone == "6" or clone == "06":
       system("clear")
       Inshackle()
       print (" Installed Succesfully ")
    elif clone == "7" or clone == "07":
       system("clear")
       blackmafia()
       print (" Installed Succesfully ")
    elif clone == "8" or clone == "08":
       system("clear")
       instahack()
       print (" Installed Succesfully ")
    elif clone == "9" or clone == "09":
       system("clear")
       insfollow()
       print (" Installed Succesfully ")
    elif clone == "10":
       system("clear")
       afgcrack()
       print (" Installed Succesfully ")
    elif clone == "11":
       system("clear")
       osiig()
       print (" Installed Succesfully ")
    elif clone == "12":
       system("clear")
       autoig()
       print (" Installed Succesfully ")
    elif clone == "13":
       system("clear")
       lucifer()
       print (" Installed Succesfully ")
    elif clone == "14":
       system("clear")
       without()
       print (" Installed Succesfully ")
    elif clone == "15":
       system("clear")
       fastclone()
       print (" Installed Succesfully ")
    elif clone == "16":
       system("clear")
       bxi()
       print (" Installed Succesfully ")
    elif clone == "17":
       system("clear")
       sensei()
       print (" Installed Succesfully ")
    elif clone == "18":
       system("clear")
       badrobo()
       print (" Installed Succesfully ")
    elif clone == "19":
       system("clear")
       toolsig()
       print (" Installed Succesfully ")
    elif clone == "99":
       BackToMenu()
    elif clone == "0" or clone == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()


def Vuln():
    print ("""  {}[{}1{}]{} Slowloris
  {}[{}2{}]{} Nikto
  {}[{}3{}]{} Nmap
  {}[{}4{}]{} Sqlmap
  {}[{}5{}]{} Sqliv
  {}[{}6{}]{} Visql
  {}[{}7{}]{} Sqlmate
  {}[{}8{}]{} Click-Jacking
  {}[{}9{}]{} Psqli-Pro
  {}[{}10{}]{} Wp-Plugin-Scanner
  {}[{}11{}]{} Recon-ng
  {}[{}12{}]{} Nscan
  {}[{}13{}]{} Red-Hawk
  {}[{}14{}]{} Cyberscan
  {}[{}15{}]{} ReconDog
  {}[{}16{}]{} ReconSpider
  {}[{}17{}]{} Wordpresscan
  {}[{}18{}]{} Optiva-Framework
  {}[{}19{}]{} TMScanner
  {}[{}20{}]{} OWScan
  {}[{}21{}]{} XAttacker
  {}[{}22{}]{} XSSniper
  {}[{}23{}]{} Striker
  {}[{}24{}]{} Rang3r
  {}[{}25{}]{} Heardbleed Scanner
  {}[{}26{}]{} Wpscan
  {}[{}27{}]{} Wascan
  {}[{}28{}]{} Zarp
  {}[{}29{}]{} Angry Fuzzer
  {}[{}30{}]{} CMSmap
  {}[{}31{}]{} Wpseku
  {}[{}32{}]{} CMSeel Suit
  {}[{}33{}]{} Knockpy
  {}[{}34{}]{} A2SV-ssl-vul-Scan
  {}[{}35{}]{} Easymap
  {}[{}36{}]{} Gasmask
  {}[{}37{}]{} NoSql
  {}[{}38{}]{} CheckUrl
  {}[{}39{}]{} Killshot
  {}[{}40{}]{} Astronmap
  {}[{}41{}]{} SkipFish
  {}[{}42{}]{} SmbScanner
  {}[{}43{}]{} Shodan-Eye
  {}[{}44{}]{} Search Sploit
  {}[{}45{}]{} Webkiller
  {}[{}46{}]{} Raccoon
  {}[{}47{}]{} phpVulnhunter
  {}[{}48{}]{} Sandmap
  {}[{}49{}]{} jackhammer
  {}[{}50{}]{} Dr0p1t-Framework
  {}[{}51{}]{} watchdog
  {}[{}52{}]{} crlfuzz
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      vuln = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if vuln == "1" or vuln == "01":
       system("clear")
       Slowrosis()
       print (" Installed Succesfully ")
    elif vuln == "2" or vuln == "02":
       system("clear")
       nicto()
       print (" Installed Succesfully ")
    elif vuln == "3" or vuln == "03":
       system("clear")
       nmap()
       print (" Installed Succesfully ")
    elif vuln == "4" or vuln == "04":
       system("clear")
       Sqlmap()
       print (" Installed Succesfully ")
    elif vuln == "5" or vuln == "05":
       system("clear")
       SQliv()
       print (" Installed Succesfully ")
    elif vuln == "6" or vuln == "06":
       system("clear")
       viSQL()
       print (" Installed Succesfully ")
    elif vuln == "7" or vuln == "07":
       system("clear")
       sqlmate()
       print (" Installed Succesfully ")
    elif vuln == "8" or vuln == "08":
       system("clear")
       Clickjacking()
       print (" Installed Succesfully ")
    elif vuln == "9" or vuln == "09":
       system("clear")
       psqlipro()
       print (" Installed Succesfully ")
    elif vuln == "10":
       system("clear")
       wppluginscanner()
       print (" Installed Succesfully ")
    elif vuln == "11":
       system("clear")
       Reconng()
       print (" Installed Succesfully ")
    elif vuln == "12":
       system("clear")
       Nscan()
       print (" Installed Succesfully ")
    elif vuln == "13":
       system("clear")
       RedHawk()
       print (" Installed  Succesfully ")
    elif vuln == "14":
       system("clear")
       CyberScan()
       print (" Installed Succesfully ")
    elif vuln == "15":
       system("clear")
       ReconDog()
       print (" Installed Succesfully ")
    elif vuln == "16":
       system("clear")
       reconspider()
       print (" Installed Succesfully ")
    elif vuln == "17":
       system("clear")
       wordpresscan()
       print (" Installed Succesfully ")
    elif vuln == "18":
       system("clear")
       optivaframework()
       print (" Installed Succesfully ")
    elif vuln == "19":
       system("clear")
       Tmscanner()
       print (" Installed Succesfully ")
    elif vuln == "20":
       system("clear")
       OWScan()
       print (" Installed Succesfully ")
    elif vuln == "21":
       system("clear")
       XAttacker()
       print (" Installed Succesfully ")
    elif vuln == "22":
       system("clear")
       xsssniper()
       print (" Installed Succesfully ")
    elif vuln == "23":
       system("clear")
       Striker()
       print (" Installed Succesfully ")
    elif vuln == "24":
       system("clear")
       rang3r()
       print (" Installed Succesfully ")
    elif vuln == "25":
       system("clear")
       heartbleed()
       print (" Installed Succesfully ")
    elif vuln == "26":
       system("clear")
       wpscan()
       print (" Installed Succesfully ")
    elif vuln == "27":
       system("clear")
       wascan()
       print (" Installed Succesfully ")
    elif vuln == "28":
       system("clear")
       Zarp()
       print (" Installed Succesfully ")
    elif vuln == "29":
       system("clear")
       angryFuzzer()
       print (" Installed Succesfully ")
    elif vuln == "30":
       system("clear")
       CMsmap()
       print (" Installed Succesfully ")
    elif vuln == "31":
       system("clear")
       wpseku()
       print (" Installed Succesfully ")
    elif vuln == "32":
       system("clear")
       CMSeek()
       print (" Installed Succesfully ")
    elif vuln == "33":
       system("clear")
       knockpy()
       print ("  Installed Succesfully ")
    elif vuln == "34":
       system("clear")
       a2sv()
       print (" Installed Succesfully ")
    elif vuln == "35":
       system("clear")
       Easymap()
       print (" Installed Succesfully ")
    elif vuln == "36":
       system("clear")
       gasmask()
       print ("installed Succesfully ")
    elif vuln == "37":
       system("clear")
       nosql()
       print (" Installed Succesfully ")
    elif vuln == "38":
       system("clear")
       CheckUrl()
       print (" Installed Succesfully ")
    elif vuln == "39":
       system("clear")
       killshot()
       print (" Installed Succesfully ")
    elif vuln == "40":
       system("clear")
       Astronmap()
       print (" Installed Succesfully ")
    if vuln == "41":
       system("clear")
       skipfish()
       print (" Installed Succesfully ")
    elif vuln == "42":
       system("clear")
       smbscanner()
       print (" Installed Succesfully ")
    elif vuln == "43":
       system("clear")
       shodaneye()
       print (" Installed Succesfully ")
    elif vuln == "44":
       system("clear")
       searchsploit()
       print (" Installed Succesfully ")
    elif vuln == "45":
       system("clear")
       webkiller()
       print (" Installed Succesfully ")
    elif vuln == "46":
       system("clear")
       raccoon()
       print (" Installed Succesfully ")
    elif vuln == "47":
       system("clear")
       phpvulnhunter()
       print (" Installed Succesfully ")
    elif vuln == "48":
       system("clear")
       sandmap()
       print (" Installed Succesfully ")
    elif vuln == "49":
       system("clear")
       jackhammer()
       print (" Installed Succesfully ")
    elif vuln == "50":
       system("clear")
       Dr0p1tframework()
       print (" Installed Succesfully ")
    elif vuln == "51":
       system("clear")
       watchdog()
       print (" Installed Succesfully ")
    elif vuln == "52":
       system("clear")
       crlfuzz()
       print (" Installed Succesfully ")
    elif vuln == "99":
       BackToMenu()
    elif vuln == "0" or vuln == "00":
       print(O)
       exit()

def Info():
    print ("""  {}[{}1{}]{} Nmap
  {}[{}2{}]{} TheHarvester
  {}[{}3{}]{} LittleBrother
  {}[{}4{}]{} Infoga
  {}[{}5{}]{} TrackSploit
  {}[{}6{}]{} Recon-ng
  {}[{}7{}]{} ReconDog
  {}[{}8{}]{} UserRecon
  {}[{}9{}]{} Th3inspector
  {}[{}10{}]{} PureBlood
  {}[{}11{}]{} Angry Fuzzer
  {}[{}12{}]{} Exif Tool
  {}[{}13{}]{} Gasmask
  {}[{}14{}]{} Nscan
  {}[{}15{}]{} PhoneInfoga
  {}[{}16{}]{} URLDecoder
  {}[{}17{}]{} ReconCobra
  {}[{}18{}]{} Creepy
  {}[{}19{}]{} Devploit
  {}[{}20{}]{} InfoSploit
  {}[{}21{}]{} BruteForce_new
  {}[{}22{}]{} NameCHK
  {}[{}23{}]{} ASU
  {}[{}24{}]{} Sherlock
  {}[{}25{}]{} Mac-Lookup
  {}[{}26{}]{} GINF
  {}[{}27{}]{} Credmap
  {}[{}28{}]{} ChoiceBot
  {}[{}29{}]{} Breacher
  {}[{}30{}]{} KnockMail
  {}[{}31{}]{} Telegram-Scraper
  {}[{}32{}]{} Social-analyzer
  {}[{}33{}]{} ctfr
  {}[{}34{}]{} Osintgram
  {}[{}35{}]{} snitch
  {}[{}36{}]{} Anubis
  {}[{}37{}]{} Infoga-1
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      info = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if info == "1" or info == "01":
       system("clear")
       nmap()
       print (" Installed Succesfully ")
    elif info == "2" or info == "02":
       system("clear")
       TheHarvester()
       print (" Installed Succesfully ")
    elif info == "3" or info == "03":
       system("clear")
       Littlebrother()
       print (" Installed Succesfully ")
    elif info == "4" or info == "04":
       system("clear")
       Infoga()
       print (" Installed Succesfully ")
    elif info == "5" or info == "05":
       system("clear")
       tracksploit()
       print (" Installed Succesfully ")
    elif info == "6" or info == "06":
       system("clear")
       Reconng()
       print (" Installed Succesfully ")
    elif info == "7" or info == "07":
       system("clear")
       ReconDog()
       print (" Installed Succesfully ")
    elif info == "8" or info == "08":
       system("clear")
       Userrecon()
       print (" Installed Succesfully ")
    elif info == "9" or info == "09":
       system("clear")
       Theinspector()
       print (" Installed Succesfully ")
    elif info == "10":
       system("clear")
       pureblood()
       print (" Installed Succesfully ")
    elif info == "11":
       system("clear")
       AngryFuzzer()
       print (" Installed Succesfully ")
    elif info == "12":
       system("clear")
       Exiftool()
       print (" Installed Succesfully ")
    elif info == "13":
       system("clear")
       gasmask()
       print (" Installed Succesfully ")
    elif info == "14":
       system("clear")
       Nscan()
       print (" Installed Succesfully ")
    elif info == "15":
       system("clear")
       Phoneinfoga()
       print (" Installed Succesfully ")
    elif info == "16":
       system("clear")
       URLDecoder()
       print (" Installed Succesfully ")
    elif info == "17":
       system("clear")
       reconcobra()
       print (" Installed Succesfully ")
    elif info == "18":
       system("clear")
       creepy()
       print (" Installed Succesfully ")
    elif info == "19":
       system("clear")
       Devploit()
       print (" Installed Succesfully ")
    elif info == "20":
       system("clear")
       InfoSploit()
       print (" Installed Succesfully ")
    elif info == "21":
       system("clear")
       BRUTEFORCERnew()
       print (" Installed Succesfully ")
    elif info == "22":
       system("clear")
       Namechk()
       print (" Installed Succesfully ")
    elif info == "23":
       system("clear")
       ASU()
       print (" Installed Succesfully ")
    elif info == "24":
       system("clear")
       Sherlock()
       print (" Installed Succesfully ")
    elif info == "25":
       system("clear")
       Maclookup()
       print (" Installed Succesfully ")
    elif info == "26":
       system("clear")
       GINF()
       print (" Installed Succesfully ")
    elif info == "27":
       system("clear")
       Credmap()
       print (" Installed Succesfully ")
    elif info == "28":
       system("clear")
       Choicebot()
       print (" Installed Succesfully ")
    elif info == "29":
       system("clear")
       Breacher()
       print (" Installed Succesfully ")
    elif info == "30":
       system("clear")
       Knockmail()
       print (" Installed Succesfully ")
    elif info == "31":
       system("clear")
       telegramscraper()
       print (" Installed Succesfully ")
    elif info == "32":
       system("clear")
       socialanalyser()
       print (" Installed Succesfully ")
    elif info == "33":
       system("clear")
       ctfr()
       print (" Installed Succesfully ")
    elif info == "34":
       system("clear")
       osintgram()
       print (" Installed Succesfully ")
    elif info == "35":
       system("clear")
       snitch()
       print (" Installed Succesfully ")
    elif info == "36":
       system("clear")
       anubis()
       print (" Installed Succesfully ")
    elif info == "37":
       system("clear")
       infoga1()
       print (" Installed Succesfully ")
    elif info == "99":
       BackToMenu()
    elif info == "0" or info == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Wifi():
    print ("""  {}[{}1{}]{} Wifite
  {}[{}2{}]{} Wifite2
  {}[{}3{}]{} RouterSploit
  {}[{}4{}]{} WifiPhisher
  {}[{}5{}]{} Aircrack-ng
  {}[{}6{}]{} Wifi-Bruteforcer
  {}[{}7{}]{} Autopixie.py
  {}[{}8{}]{} Ehtools
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      wifi = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if wifi == "1" or wifi == "01":
       system("clear")
       Wifite()
       print (" Installed Succesfully ")
    elif wifi == "2" or wifi == "02":
       system("clear")
       Wifite2()
       print (" Installed Succesfully ")
    elif wifi == "3" or wifi == "03" :
       system("clear")
       Routersploit()
       print (" Installed Succesfully ")
    elif wifi == "4" or wifi == "04":
       system("clear")
       wifiphisher()
       print (" Installed Succesfully ")
    elif wifi == "5" or wifi == "05":
       system("clear")
       aircrackng()
       print (" Installed Succesfully ")
    elif wifi == "6" or wifi == "06":
       system("clear")
       wifibruteforcer()
       print (" Installed Succesfully ")
    elif wifi == "7" or wifi == "07":
       system("clear")
       Autopixie()
       print (" Installed Succesfully ")
    elif wifi == "8" or wifi == "08":
       system("clear")
       Ehtools()
       print (" Installed Succesfully ")
    elif wifi == "99":
       BackToMenu()
    elif wifi == "0" or wifi == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Trac():
    print("""  {}[{}1{}]{} Trape
  {}[{}2{}]{} Trity
  {}[{}3{}]{} Nmap
  {}[{}4{}]{} PhoneInfoga
  {}[{}5{}]{} IP-Geolocation
  {}[{}6{}]{} Crips
  {}[{}7{}]{} IP-Tracer
  {}[{}8{}]{} IP-Attack
  {}[{}9{}]{} IP-Tracker
  {}[{}10{}]{} AngryFuzzer
  {}[{}11{}]{} IP-FY
  {}[{}12{}]{} Seeker
  {}[{}13{}]{} Locator
  {}[{}14{}]{} Saycheese
  {}[{}15{}]{} Grabcam
  {}[{}16{}]{} Camphish
  {}[{}17{}]{} WishFish
  {}[{}18{}]{} SayHellow
  {}[{}19{}]{} HackLock
  {}[{}20{}]{} FireFly
  {}[{}21{}]{} IPCS
  {}[{}22{}]{} Cam-Hackers
  {}[{}23{}]{} CCTV
  {}[{}24{}]{} Geo-recon
  {}[{}25{}]{} Trackout
  {}[{}26{}]{} m-wiz
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""

  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      trac = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if trac == "1" or trac == "01":
       system("clear")
       Trape()
       print (" Installed Succesfully ")
    elif trac == "2" or trac == "02":
       system("clear")
       Trity()
       print (" Installed Succesfully ")
    elif trac == "3" or trac == "03":
       system("clear")
       nmap()
       print (" Installed Succesfully ")
    elif trac == "4" or trac == "04":
       system("clear")
       Phoneinfoga()
       print (" Installed Succesfully ")
    elif trac == "5" or trac == "05":
       system("clear")
       IpGeolocation()
       print (" Installed Succesfully ")
    elif trac == "6" or trac == "06":
       system("clear")
       crips()
       print (" Installed Succesfully ")
    elif trac == "7" or trac == "07":
       system("clear")
       Iptracer()
       print (" Installed Succesfully ")
    elif trac == "8" or trac == "08":
       system("clear")
       Ipattack()
       print (" Installed Succesfully ")
    elif trac == "9" or trac == "09":
       system("clear")
       Iptracker()
       print (" Installed Succesfully ")
    elif trac == "10":
       system("clear")
       AngryFuzzer()
       print (" Installed Succesfully ")
    elif trac == "11":
       system("clear")
       ipfy()
       print (" Installed Succesfully ")
    elif trac == "12":
       system("clear")
       seeker()
       print (" Installed Succesfully ")
    elif trac == "13":
       system("clear")
       locator()
       print (" Installed Succesfully ")
    elif trac == "14":
       system("clear")
       saycheese()
       print (" Installed Succesfully ")
    elif trac == "15":
       system("clear")
       grabcam()
       print (" Installed Succesfully ")
    elif trac == "16":
       system("clear")
       camphish()
       print (" Installed Succesfully ")
    elif trac == "17":
       system("clear")
       Wishfish()
       print (" Installed Succesfully ")
    elif trac == "18":
       system("clear")
       Sayhellow()
       print (" Installed Succesfully ")
    elif trac == "19":
       system("clear")
       Hacklock()
       print (" Installed Succesfully ")
    elif trac == "20":
       system("clear")
       Firefly()
       print (" Installed Succesfully ")
    elif trac == "21":
       system("clear")
       IPCS()
       print (" Installed Succesfully ")
    elif trac == "22":
       system("clear")
       camhackers()
       print (" Installed Succesfully ")
    elif trac == "23":
       system("clear")
       cctv()
       print (" Installed Succesfully ")
    elif trac == "24":
       system("clear")
       georecon()
       print (" Installed Succesfully ")
    elif trac == "25":
       system("clear")
       trackout()
       print (" Installed Succesfully ")
    elif trac == "26":
       system("clear")
       mwiz()
    elif trac == "99":
       BackToMenu()
    elif trac == "0" or trac == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Exp():
    print("""  {}[{}1{}]{} Metasploit
  {}[{}2{}]{} Beef
  {}[{}3{}]{} SQLmap
  {}[{}4{}]{} Phonesploit
  {}[{}5{}]{} Websploit
  {}[{}6{}]{} A-Rat
  {}[{}7{}]{} The FatRat
  {}[{}8{}]{} Veil-Evasion
  {}[{}9{}]{} Evil-Droid
  {}[{}10{}]{} TMVenom
  {}[{}11{}]{} Duck-Droid
  {}[{}12{}]{} Ghost Framework
  {}[{}13{}]{} Commix
  {}[{}14{}]{} Parat
  {}[{}15{}]{} Msf-Pg
  {}[{}16{}]{} Spade
  {}[{}17{}]{} Brutal
  {}[{}18{}]{} AndroBugs-Framework
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      exp = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if exp == "1" or exp == "01":
       system("clear")
       metasploit()
       print (" Installed Succesfully ")
    elif exp == "2" or exp == "02":
       system("clear")
       Beef()
       print (" Installed Succesfully ")
    elif exp == "3" or exp == "03":
       system("clear")
       system("clear")
       Sqlmap()
       print (" Installed Succesfully ")
    elif exp == "4" or exp == "04":
       system("clear")
       Phonesploit()
       print (" Installed Succesfully ")
    elif exp == "5" or exp == "05":
       system("clear")
       websploit()
       print (" Installed Succesfully ")
    elif exp == "6" or exp == "06":
       system("clear")
       ARat()
       print (" Installed Succesfully ")
    elif exp == "7" or exp == "07":
       system("clear")
       Thefatrat()
       print (" Installed Succesfully ")
    elif exp == "8" or exp == "08":
       system("clear")
       vielEvasion()
       print (" Installed Succesfully ")
    elif exp == "9" or exp == "09":
       system("clear")
       Evildroid()
       print (" Installed Succesfully ")
    elif exp == "10":
       system("clear")
       TMvenom()
       print (" Installed Succesfully ")
    elif exp == "11":
       system("clear")
       Duckdroid()
       print (" Installed Succesfully ")
    elif exp == "12":
       system("clear")
       Ghostframework()
       print (" Installed Succesfully ")
    elif exp == "13":
       system("clear")
       commix()
       print (" Installed Succesfully ")
    elif exp == "14":
       system("clear")
       parat()
       print (" Installed Succesfully ")
    elif exp == "15":
       system("clear")
       MSFpg()
       print (" Installed Succesfully ")
    elif exp == "16":
       system("clear")
       spade()
       print (" Installed Succesfully ")
    elif exp == "17":
       system("clear")
       brutal()
       print (" Installed Succesfully ")
    elif exp == "18":
       system("clear")
       AndroBugs_Framework()
       print (" Installed Succesfully ")
    elif exp == "99":
       BackToMenu()
    elif exp == "0" or exp == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Pass():
    print("""  {}[{}1{}]{} john the ripper
  {}[{}2{}]{} Hashcat
  {}[{}3{}]{} Hydra
  {}[{}4{}]{} Hasher
  {}[{}5{}]{} Hash-Cracker
  {}[{}6{}]{} Hash-Buster
  {}[{}7{}]{} Hash-Generator
  {}[{}8{}]{} Hasherdoit
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      Pass = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if Pass == "1" or Pass == "01":
       system("clear")
       johntheripper()
       print (" Installed Succesfully ")
    elif Pass == "2" or Pass == "02":
       system("clear")
       Hashcat()
       print (" Installed Succesfully ")
    elif Pass == "3" or Pass == "03":
       system("clear")
       Hydra()
       print (" Installed Succesfully ")
    elif Pass == "4" or Pass == "04":
       system("clear")
       Hasher()
       print (" Installed Succesfully ")
    elif Pass == "5" or Pass == "05":
       system("clear")
       Hashcracker()
       print (" Installed Succesfully ")
    elif Pass == "6" or Pass == "06":
       system("clear")
       Hashbuster()
       print (" Installed Succesfully ")
    elif Pass == "7" or Pass == "07":
       system("clear")
       Hashgenerator()
       print (" Installed Succesfully ")
    elif Pass == "8" or Pass == "08":
       system("clear")
       Hasherdoit()
       print (" Installed Succesfully ")
    elif Pass == "99":
       BackToMenu()
    elif Pass == "0" or Pass == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Mal():
    print("""  {}[{}1{}]{} The Zoo
  {}[{}2{}]{} BeeLogger
  {}[{}3{}]{} Vbug
  {}[{}4{}]{} Malicious
  {}[{}5{}]{} Infect
  {}[{}6{}]{} HatKey
  {}[{}7{}]{} PapaViruz
  {}[{}8{}]{} Vanish
  {}[{}9{}]{} Spammer-Grab
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      mal = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if mal == "1" or mal == "01":
       system("clear")
       Thezoo()
       print (" Installed Succesfully ")
    elif mal == "2" or mal == "02":
       system("clear")
       Beelogger()
       print (" Installed Succesfully ")
    elif mal == "3" or mal == "03":
       system("clear")
       Vbug()
       print (" Installed Succesfully ")
    elif mal == "4" or mal == "04":
       system("clear")
       Malicious()
       print (" Installed Succesfully ")
    elif mal == "5" or mal == "05":
       system("clear")
       infect()
       print (" Installed Succesfully ")
    elif mal == "6" or mal == "06":
       system("clear")
       Hatkey()
       print (" Installed Succesfully ")
    elif mal == "7" or mal == "07":
       system("clear")
       papaviruz()
       print (" Installed Succesfully ")
    elif mal == "8" or mal == "08":
       system("clear")
       vanish()
       print (" Installed Succesfully ")
    elif mal == "9" or mal == "09":
       system("clear")
       Spammergrab()
       print (" Installed Succesfully ")
    elif mal == "99":
       BackToMenu()
    elif mal == "0" or mal == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def Bom():
    print("""  {}[{}1{}]{} TBomb
  {}[{}2{}]{} SMS FUCKER 2.0
  {}[{}3{}]{} SMS-Bomb
  {}[{}4{}]{} Quack
  {}[{}5{}]{} HBomb
  {}[{}6{}]{} Bombers
  {}[{}7{}]{} SMS Bombers 300
  {}[{}8{}]{} Email-Bomber
  {}[{}9{}]{} E-Bomber
  {}[{}10{}]{} G-BOMBER-2.0
  {}[{}11{}]{} AvarSpam
  {}[{}12{}]{} SpamWa
  {}[{}13{}]{} LiteOTP
  {}[{}14{}]{} Spazsms
  {}[{}15{}]{} TelegramScraper
  {}[{}16{}]{} ispammer
  {}[{}17{}]{} BomberThon
  {}[{}18{}]{} call
  {}[{}19{}]{} spamX
  {}[{}20{}]{} MBomb
  {}[{}21{}]{} whataBomb
  {}[{}22{}]{} fast-mail-bomber
  {}[{}23{}]{} Email-Hack
  {}[{}24{}]{} Hpomb
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      bom = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if bom == "1" or bom == "01":
       system("clear")
       Tbomb()
       print (" Installed Succesfully ")
    elif bom == "2" or bom == "02":
       system("clear")
       smsfucker ()
       print (" Installed Succesfully ")
    elif bom == "3" or bom == "03":
       system("clear")
       smsbomb()
       print (" Installed Succesfully ")
    elif bom == "4" or bom == "04":
       system("clear")
       Quack()
       print (" Installed Succesfully ")
    elif bom == "5" or bom == "05":
       system("clear")
       Hbomb()
       print (" Installed Succesfully ")
    elif bom == "6" or bom == "06":
       system("clear")
       bombers()
       print (" Installed Succesfully ")
    elif bom == "7" or bom == "07":
       system("clear")
       smsbomber300()
    elif bom == "8" or bom == "08":
       system("clear")
       Emailbomber()
       print (" Installed Succesfully ")
    elif bom == "9" or bom == "09":
       system("clear")
       EBomber()
       print (" Installed Succesfully ")
    elif bom == "10":
       system("clear")
       EMBomber()
       print (" Installed Succesfully ")
    elif bom == "11":
       system("clear")
       Avarspam()
       print (" Installed Succesfully ")
    elif bom == "12":
       system("clear")
       Spamwa()
       print (" Installed Succesfully ")
    elif bom == "13":
       system("clear")
       Liteotp()
       print (" Installed Succesfully ")
    elif bom == "14":
       system("clear")
       SpazSms()
       print (" Installed Succesfully ")
    elif bom == "15":
       system("clear")
       telegramscraper()
       print (" Installed Succesfully ")
    elif bom == "16":
       system("clear")
       ispammer()
       print (" Installed Succesfully ")
    elif bom == "17":
       system("clear")
       bomberthon()
       print (" Installed Succesfully ")
    elif bom == "18":
       system("clear")
       call()
       print (" Installed Succesfully ")
    elif bom == "19":
       system("clear")
       spamx()
       print (" Installed Succesfully ")
    elif bom == "20":
       system("clear")
       mbomb()
       print (" Installed Succesfully ")
    elif bom == "21":
       system("clear")
       whatabomb()
       print (" Installed Succesfully ")
    elif bom == "22":
       system("clear")
       fastmailbomber()
       print (" Installed Succesfully ")
    elif bom == "23":
       system("clear")
       emailhack()
       print (" Installed Succesfully ")
    elif bom == "24":
       system("clear")
       hpomb()
       print (" Installed Succesfully ")
    elif bom == "99":
       BackToMenu()
    elif bom == "0" or bom == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

def DDOS():
    print("""  {}[{}1{}]{} Slowrosis
  {}[{}2{}]{} Hulk
  {}[{}3{}]{} DDOS-Attack
  {}[{}4{}]{} Hunner
  {}[{}5{}]{} Xerxes
  {}[{}6{}]{} PlanetWork-DDOS
  {}[{}7{}]{} LiteDDOS
  {}[{}8{}]{} Hammer
  {}[{}9{}]{} DDOS-Ripper
  {}[{}10{}]{} X-Attack
  {}[{}11{}]{} Torjan
  {}[{}12{}]{} fastnetmon
  {}[{}13{}]{} MCIDDOS
  {}[{}14{}]{} ddos-dos-tools
  {}[{}15{}]{} Saddam
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))
    try:
      ddos = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if ddos == "1" or ddos == "01":
       system("clear")
       Slowrosis()
       print (" Installed Succesfully ")
    elif ddos == "2" or ddos == "02":
       system("clear")
       Hulk()
       print (" Installed Succesfully ")
    elif ddos == "3" or ddos == "03":
       system("clear")
       DdosAttack()
       print (" Installed Succesfully ")
    elif ddos == "4" or ddos == "04":
       system("clear")
       Hunner()
       print (" Installed Succesfully ")
    elif ddos == "5" or ddos == "05":
       system("clear")
       xerxes()
       print (" Installed Succesfully ")
    elif ddos == "6" or ddos == "06":
       system("clear")
       PlanetworkDDOS()
       print (" Installed Succesfully ")
    elif ddos == "7" or ddos == "07":
       system("clear")
       liteddos()
       print (" Installed Succesfully ")
    elif ddos == "8" or ddos == "08":
       system("clear")
       hammer()
       print (" Installed Succesfully ")
    elif ddos == "9" or ddos == "09":
       system("clear")
       ddosripper()
       print (" Installed Succesfully ")
    elif ddos == "10":
       system("clear")
       xattack()
       print (" Installed Succesfully ")
    elif ddos == "11":
       system("clear")
       torjan()
       print (" Installed Succesfully ")
    elif ddos == "12":
       system("clear")
       fastnetmon()
       print (" Installed Succesfully ")
    elif ddos == "13":
       system("clear")
       mciddos()
       print (" Installed Succesfully ")
    elif ddos == "14":
       system("clear")
       ddosdostools()
       print (" Installed Succesfully ")
    elif ddos == "15":
       system("clear")
       saddam()
       print (" Installed Succesfully ")
    elif ddos == "99":
       BackToMenu()
    elif ddos == "0" or ddos == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()


def Special():
    print("""  {}[{}1{}]{} Split Termux Terminals
  {}[{}2{}]{} Chat Room in Termux
  {}[{}3{}]{} Browsing in Termux
  {}[{}4{}]{} Getting System Info
  {}[{}5{}]{} Hollywood Effect
  {}[{}6{}]{} Cmatrix
  {}[{}7{}]{} Fire in Termux
  {}[{}8{}]{} Banners
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      spec = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if spec == "1" or spec == "01":
       system("clear")
       Split()
       print (" Installed Succesfully ")
    elif spec == "2" or spec == "02":
       system("clear")
       Chat()
       print (" Installed Succesfully ")
    elif spec == "3" or spec == "03":
       system("clear")
       Browse()
       print (" Installed Succesfully ")
    elif spec == "4" or spec == "04":
       system("clear")
       Sysinfo()
       print (" Installed Succesfully ")
    elif spec == "5" or spec == "05":
       system("clear")
       Hollywood()
       print (" Installed Succesfully ")
    elif spec == "6" or spec == "06":
       system("clear")
       Cmatrix()
       print (" Installed Succesfully ")
    elif spec == "7" or spec == "07":
       system("clear")
       Fire()
       print (" Installed Succesfully ")
    elif spec == "8" or spec == "08":
       system("clear")
       toilet()
       print (" Installed Succesfully ")
    elif spec == "99":
       BackToMenu()
    elif spec == "0" or spec == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()


def Ano():
    print("""  {}[{}1{}]{} Tool-X
    {}[{}2{}]{} Web Hunter
  {}[{}3{}]{} Dark-Fly
  {}[{}4{}]{} Easy-Hack
  {}[{}5{}]{} Lazymux
  {}[{}6{}]{} Fsociety
  {}[{}7{}]{} lscript
  {}[{}8{}]{} Lazyscript
  {}[{}9{}]{} AK47
  {}[{}10{}]{} TheChoice
  {}[{}11{}]{} Th3inspector
  {}[{}12{}]{} Txtool
  {}[{}13{}]{} HackerPro
  {}[{}14{}]{} Facebook-Toolkit
  {}[{}15{}]{} GoldenEye
  {}[{}16{}]{} Hacktronian
  {}[{}17{}]{} Tool-N
  {}[{}18{}]{} HackingTool
  {}[{}19{}]{} D-Tect
  {}[{}20{}]{} King-Hacking
  {}[{}21{}]{} Host
  {}[{}22{}]{} OXIDTools
  {}[{}23{}]{} tstyle
  {}[{}24{}]{} bash2mp4
  {}[{}25{}]{} shorturl
  {}[{}26{}]{} PROXY-FINDER
  {}[{}27{}]{} PENTESTING-BIBLE
  {}[{}28{}]{} pureblood
  {}[{}29{}]{} DarkSploit
  {}[{}30{}]{} hakkuframework
  {}[{}31{}]{} Optiva-Framework
  {}[{}32{}]{} Gloom-Framework
  {}[{}99{}]{} Return To Menu
  {}[{}00{}]{} Exit\n"""
  .format(A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G,A,W,A,G))

    try:
      ano = input(" {}[{}*{}] Select Option : {}".format(W,A,W,A))
    except KeyboardInterrupt:
      print(O)
      exit()
    print(G)
    sleep(0.5)
    if ano == "1" or ano == "01":
       system("clear")
       ToolX()
       print (" Installed Succesfully ")
    elif ano == "2" or ano == "02":
       system("clear")
       darkhunter ()
       print (" Installed Succesfully ")
    elif ano == "3" or ano == "03":
       system("clear")
       Darkfly()
       print (" Installed Succesfully ")
    elif ano == "4" or ano == "04":
       system("clear")
       Eayhack()
       print (" Installed Succesfully ")
    elif ano == "5" or ano == "05":
       system("clear")
       Lazymux()
       print (" Installed Succesfully ")
    elif ano == "6" or ano == "06":
       system("clear")
       Fsociety()
       print (" Installed Succesfully ")
    elif ano == "7" or ano == "07":
       system("clear")
       Lazy()
       print (" Installed Succesfully ")
    elif ano == "8" or ano == "08":
       system("clear")
       Lazyscript()
       print (" Installed Succesfully ")
    elif ano == "9" or ano == "09":
       system("clear")
       AK47()
       print (" Installed Succesfully ")
    elif ano == "10":
       system("clear")
       Thechoice()
       print (" Installed Succesfully ")
    elif ano == "11":
       system("clear")
       Theinspector()
       print (" Installed Succesfully ")
    elif ano == "12":
       system("clear")
       txtool()
       print (" Installed Succesfully ")
    elif ano == "13":
       system("clear")
       Hackerpro()
       print (" Installed Succesfully ")
    elif ano == "14":
       system("clear")
       Facebooktoolkit()
       print (" Installed Succesfully ")
    elif ano == "15":
       system("clear")
       GoldenEye()
       print (" Installed Succesfully ")
    elif ano == "16":
       system("clear")
       Hacktronian()
       print (" Installed Succesfully ")
    elif ano == "17":
       system("clear")
       ToolN()
       print (" Installed Succesfully ")
    elif ano == "18":
       system("clear")
       Hackingtool()
       print (" Installed Succesfully ")
    elif ano == "19":
       system("clear")
       Dtect()
       print (" Installed Succesfully ")
    elif ano == "20":
       system("clear")
       kingHacking()
       print (" Installed Succesfully ")
    elif ano == "21":
       system("clear")
       host()
       print (" Installed Succesfully ")
    elif ano == "22":
       system("clear")
       oxidtools()
       print (" Installed Succesfully ")
    elif ano == "23":
       system("clear")
       tstyle()
       print (" Installed Succesfully ")
    elif ano == "24":
       system("clear")
       bash2mp4()
       print (" Installed Succesfully ")
    elif ano == "25":
       system("clear")
       shorturl()
       print (" Installed Succesfully ")
    elif ano == "26":
       system("clear")
       proxyfinder()
       print (" Installed Succesfully ")
    elif ano == "27":
       system("clear")
       pentestingbible()
       print (" Installed Succesfully ")
    elif ano == "28":
       system("clear")
       pureblood()
       print (" Installed Succesfully ")
    elif ano == "29":
       system("clear")
       darksploit()
       print (" Installed Succesfully ")
    elif ano == "30":
       system("clear")
       hakkuframework()
       print (" Installed Succesfully ")
    elif ano == "31":
       system("clear")
       optivaframework()
       print (" Installed Succesfully ")
    elif ano == "32":
       system("clear")
       gloomframework()
       print (" Installed Succesfully ")
    elif ano == "99":
       BackToMenu()
    elif ano == "0" or ano == "00":
       print(O)
       exit()
    else:
       print(O)
       exit()

# Phishing tools
# Evilginx:
def Evilginx():
    print (system("cd $HOME && git clone https://github.com/kgretzky/evilginx"))
# PhishX:
def Phishx():
    print (system("cd $HOME && git clone https://github.com/kucuksemsiyelicocuk/WeebSec-PhishX"))
# HiddenEye:
def HiddenEye():
    print (system("cd $HOME && git clone https://github.com/DarkSecDevelopers/HiddenEye.git"))
# Shellphish:
def Shellphish():
    print (system("cd $HOME && git clone https://github.com/jaykali/shellphish"))
# SocialFish:
def SocialFish():
    print (system("cd $HOME && git clone https://github.com/UndeadSec/SocialFish.git"))
# weeman:
def weeman():
    print (system("cd $HOME && git clone https://github.com/samyoyo/weeman.git"))
# BlackEye:
def BlackEye():
    print (system("cd $HOME && git clone https://github.com/An0nUD4Y/blackeye"))
# Zphisher:
def Zphisher():
    print (system("cd $HOME && git clone git://github.com/htr-tech/zphisher.git"))
# Tphish:
def Tphish():
    print (system("cd $HOME && git clone https://github.com/Stephin-Franklin/T-Phish"))
# ADV phishing:
def ADVphishing():
    print (system("cd $HOME && git clone https://github.com/Ignitetch/AdvPhishing.git"))
# Nexphisher:
def Nexphisher():
    print (system("cd $HOME && git clone https://github.com/htr-tech/nexphisher"))
# Recreator Phishing:
def RecreatorPhishing():
    print (system("cd $HOME && git clone https://github.com/AngelSecurityTeam/Recreator-Phishing"))
# Evil Url:
def EvilUrl():
    print (system("cd $HOME && git clone https://github.com/darkhunter141/URL-MASTER"))
# lowbait:
def lawbait():
    print (system("cd $HOME && git clone https://github.com/ridwanirawan/lowbait"))
# FotoSploit:
def FotoSploit():
    print (system("cd $HOME && git clone https://github.com/Cesar-Hack-Gray/FotoSploit"))
# Gophish:
def gophish():
    print (system("cd $HOME && git clone https://github.com/gophish/gophish"))
# Mrphish:
def mrphish():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/mrphish"))
# Shark:
def shark():
    print (system("cd $HOME && git clone https://github.com/Bhaviktutorials/shark"))
# Phisher:
def phisher():
    print (system("cd $HOME && git clone https://github.com/yezz123/Phisher"))
# Lordphih:
def lordphish():
    print (system("cd $HOME && git clone https://github.com/Black-Hell-Team/LordPhish.git"))
# Masphish:
def maskphish():
    print (system("cd $HOME && git clone https://github.com/jaykali/maskphish"))

# brute forcing:
# Hydra:
def Hydra():
    print (system("cd $HOME && pkg install hydra"))
# Black Hydra:
def BlackHydra():
    print (system("cd $HOME && git clone https://github.com/Gameye98/Black-Hydra"))
# BruteX:
def Brutex():
    print (system("cd $HOME && git clone https://github.com/1N3/BruteX"))
# facebook-cracker:
def facebookcracker():
    print (system("cd $HOME && git clone https://github.com/Ha3MrX/facebook-cracker"))
# Facebookbruteforce:
def facebookbruteforce():
    print (system("cd $HOME && git clone https://github.com/IAmBlackHacker/Facebook-BruteForce"))
# Firecrack:
def Firecrack():
    print (system("cd $HOME && git clone https://github.com/Ranginang67/Firecrack"))
# FBbrute:
def FBbrute():
    print (system("cd $HOME && git clone https://github.com/Gameye98/FBBrute"))
# fbb:
def fbb():
    print (system("cd $HOME && git clone https://github.com/Cabdulahi/fbb"))
# FB-cracker:
def FBcracker():
    print (system("cd $HOME && git clone https://github.com/kaitolegion/FB-Cracker"))
# Bruteforcernew:
def BRUTEFORCERnew():
    print (system("cd $HOME && git clone https://github.com/FR13ND8/BRUTEFORCEnew"))
# Instahack:
def Instahack():
    print (system("cd $HOME && git clone https://github.com/fuck3erboy/instahack"))
# Instabrute:
def Instabrute():
    print (system("cd $HOME && git clone https://github.com/Ha3MrX/InstaBrute"))
# Instainsane:
def Instainsane():
    print (system("cd $HOME && git clone https://github.com/umeshshinde19/instainsane"))
# Instax:
def Instax():
    print (system("cd $HOME && git clone https://github.com/dhasirar/instax.git"))
# Instashell:
def Instashell():
    print (system("cd $HOME && git clone https://github.com/F33Z/instashell.git"))
# Brutespray:
def Brutespray():
    print (system("cd $HOME && git clone https://github.com/x90skysn3k/brutespray"))
# cupp:
def cupp():
    print (system("cd $HOME && git clone https://github.com/Mebus/cupp"))
# Lazybee:
def Lazybee():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/lazybee"))
# Wordlister:
def Wordlister():
    print (system("cd $HOME && git clone https://github.com/4n4nk3/Wordlister"))
# GoblinWordGenerator:
def GoblinWordGenerator():
    print (system("cd $HOME && git clone https://github.com/UndeadSec/GoblinWordGenerator.git"))
# Passgen:
def Passgen():
    print (system("cd $HOME && git clone https://github.com/Broham/PassGen"))
# crunch:
def crunch():
    print (system("cd $HOME && git clone https://github.com/crunchsec/crunch"))
# Indonation wordlist:
def Indonationwordlist():
    print (system("cd $HOME && git clone https://github.com/geovedi/indonesian-wordlist"))
# Socialbox-termux:
def socialbox():
    print (system("cd $HOME && git clone https://github.com/samsesh/SocialBox-Termux"))
# Intar:
def intar():
    print (system("cd $HOME && git clone https://github.com/dhasirar/instax"))
# Blueforce-FB:
def blueforce():
    print (system("cd $HOME && git clone https://github.com/AngelSecurityTeam/BluForce-FB"))
# P-gen:
def pgen():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/p-gen"))
# Plutus:
def plutus():
    print (system("cd $HOME && git clone https://github.com/Isaacdelly/Plutus"))
# XBruteForcer:
def xbruteforcer():
    print (system("cd $HOME && git clone https://github.com/Moham3dRiahi/XBruteForcer"))
# password-list:
def passwordlist():
    print (system("cd $HOME && git clone https://github.com/Scipag/password-list"))
# Bruter19:
def bruter19():
    print (system("cd $HOME && git clone https://github.com/AzizKpln/Bruter19"))
# P-Gen:
def pgen():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/p-gen"))

# cloning tools
# OSIF:
def OSIF():
    print (system("cd $HOME && git clone https://github.com/ciku370/OSIF"))
# FBI:
def FBI():
    print (system("cd $HOME && git clone https://github.com/xHak9x/fbi.git"))
# Dark-FB:
def Darkfb():
    print (system("pip2 install requests"))
    print (system("pip2 install mechanize"))
    print (system("cd $HOME && git clone https://github.com/V4N654T/dark-fb"))
# Exif-Tool:
def Exiftool():
    print (system("cd $HOME && git clone https://github.com/exiftool/exiftool"))
# ASU:
def ASU():
    print (system("cd $HOME && git clone https://github.com/LOoLzeC/ASU"))
# BlackMafia:
def blackmafia():
    print (system("cd $HOME && git clone https://github.com/lovehacker404/BlackMafia"))
# instahack:
def instahack():
    print (system("cd $HOME && git clone https://github.com/evildevill/instahack"))
# Bad-Robo:
def badrobo():
    print (system("cd $HOME && git clone https://github.com/jaleelx98/Bad-Robo"))
# without:
def without():
    print (system("cd $HOME && git clone https://github.com/BlackTiger-Error404/without"))
# Fast-Clone:
def fastclone():
    print (system("cd $HOME && git clone https://github.com/Mohammadjan1122/Fast_clone"))
# bxi:
def bxi():
    print (system("cd $HOME && git clone https://github.com/Binyamin-binni/bxi"))
# Sensei:
def sensei():
    print (system("cd $HOME && git clone https://github.com/BOT-033/Sensei"))
# autoig:
def autoig():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/autoig"))
# osi.ig:
def osiig():
    print (system("cd $HOME && git clone https://github.com/th3unkn0n/osi.ig"))
# Lucifer:
def lucifer():
    print (system("cd $HOME && git clone https://github.com/rixon-cochi/Lucifer"))
# afgcrack:
def afgcrack():
    print (system("cd $HOME && git clone https://github.com/htr-tech/afgcrack"))
# insfollow:
def insfollow():
    print (system("cd $HOME && git clone https://github.com/termuxprofessor/insfollow"))
# toolsig:
def toolsig():
    print (system("cd $HOME && git clone https://github.com/officialputuid/toolsig"))
# Inshackle:
def Inshackle():
    print (system("cd $HOME && git clone https://github.com/xd20111/inshackle"))


# Vulnerability tools
# nmap:
def nmap():
    print (system("apt install nmap"))
    print ("Type nmap your nmap will be started")
# Nicto:
def nicto():
    print (system("cd $HOME && git clone https://github.com/sullo/nikto"))
# Recon ng:
def Reconng():
    print (system("cd $HOME && git clone https://github.com/lanmaster53/recon-ng"))
# Nscan:
def Nscan():
    print (system("cd $HOME && git clone https://github.com/Anon-Divyanth/Nscan"))
# red hawk:
def RedHawk():
    print (system("cd $HOME && git clone https://github.com/Tuhinshubhra/RED_HAWK"))
# Sqlmap:
def Sqlmap():
    print (system("cd $HOME && git clone https://github.com/sqlmapproject/sqlmap.git"))
# Cyberscan:
def CyberScan():
    print (system("cd $HOME && git clone https://github.com/medbenali/CyberScan.git"))
# Tmscanner:
def Tmscanner():
    print (system("cd $HOME && git clone https://github.com/TechnicalMujeeb/TM-scanner.git"))
# OWScan:
def OWScan():
    print (system("cd $HOME && git clone https://github.com/Gameye98/OWScan"))
# XAttacker:
def XAttacker():
    print (system("cd $HOME && git clone https://github.com/Moham3dRiahi/XAttacker.git"))
# xsssniper:
def xsssniper():
    print (system("cd $HOME && git clone https://github.com/gbrindisi/xsssniper"))
# ReconDog:
def ReconDog():
    print (system("cd $HOME && git clone https://github.com/s0md3v/ReconDog"))
# Striker:
def Striker():
    print (system("cd $HOME && git clone https://github.com/s0md3v/Striker"))
# Skipfish:
def skipfish():
    print (system("cd $HOME && git clone https://github.com/spinkham/skipfish"))
# rang3r:
def rang3r():
    print (system("cd $HOME && git clone https://github.com/floriankunushevci/rang3r"))
# sublis3r:
def sublis3r():
    print (system("cd $HOME && git clone https://github.com/aboul3la/Sublist3r.git"))
# reconspider:
def reconspider():
    print (system("cd $HOME && git clone https://github.com/bhavsec/reconspider.git"))
# wpscan:
def wpscan():
    print (system("gem install bundler"))
    print (system("bundle install"))
    print (system("cd $HOME && git clone https://github.com/wpscanteam/wpscan.git"))
# Wascan:
def wascan():
    print (system("cd $HOME && git clone https://github.com/m4ll0k/WAScan.git"))
# Zarp:
def Zarp():
    print (system("cd $HOME && git clone https://github.com/hatRiot/zarp.git"))
# Heartbleed:
def heartbleed():
    print (system("cd $HOME && git clone https://github.com/TechnicalMujeeb/HeartBleed"))
# angryFuzzer:
def angryFuzzer():
    print (system("cd $HOME && git clone https://github.com/ihebski/angryFuzzer.git"))
# CMsmap:
def CMsmap():
    print (system("cd $HOME && git clone https://github.com/Dionach/CMSmap"))
# wpseku:
def wpseku():
    print (system("cd $HOME && git clone https://github.com/m4ll0k/WPSeku.git"))
# CMSeek:
def CMSeek():
    print (system("cd $HOME && git clone https://github.com/Tuhinshubhra/CMSeeK"))
# CheckUrl:
def CheckUrl():
    print (system("cd $HOME && git clone https://github.com/UndeadSec/checkURL.git"))
# Knockpy:
def knockpy():
    print (system("cd $HOME && git clone https://github.com/guelfoweb/knock.git"))
# a2sv:
def a2sv():
    print (system("cd $HOME && git clone https://github.com/hahwul/a2sv.git"))
# smbscanner:
def smbscanner():
    print (system("cd $HOME && git clone https://github.com/TechnicalMujeeb/smb-scanner"))
# viSQL:
def viSQL():
    print (system("cd $HOME && git clone https://github.com/Marcel0Sousa/script-viSQL"))
# wordpresscan:
def wordpresscan():
    print (system("cd $HOME && git clone https://github.com/swisskyrepo/Wordpresscan.git"))
# SQliv:
def SQliv():
    print (system("cd $HOME && git clone https://github.com/the-robot/sqliv.git"))
# sqlmate:
def sqlmate():
    print (system("cd $HOME && git clone https://github.com/UltimateHackers/sqlmate"))
# Easymap:
def Easymap():
    print (system("cd $HOME && git clone https://github.com/Cvar1984/Easymap"))
# gasmask:
def gasmask():
    print (system("cd $HOME && git clone https://github.com/twelvesec/gasmask"))
# Killshot:
def killshot():
    print (system("cd $HOME && git clone https://github.com/bahaabdelwahed/killshot"))
# Astronmap:
def Astronmap():
    print (system("cd $HOME && git clone https://github.com/Gameye98/AstraNmap"))
# nosql:
def nosql():
    print (system("cd $HOME && git clone https://github.com/codingo/NoSQLMap"))
# Click-jacking:
def Clickjacking():
    print (system("cd $HOME && git clone https://github.com/D4Vinci/Clickjacking-Tester"))
# Maxsubdofinder:
def Maxsubdofinder():
    print (system("cd $HOME && git clone https://github.com/maxteroit/MaxSubdoFinder"))
# Sandmap:
def sandmap():
    print (system("cd $HOME && git clone https://github.com/trimstray/sandmap"))
# jackhammer:
def jackhammer():
    print (system("cd $HOME && git clone https://github.com/olacabs/jackhammer"))
# Dr0p1t-Framework:
def dr0p1tframework():
    print (system("cd $HOME && git clone https://github.com/D4Vinci/Dr0p1t-Framework"))
# watchdog:
def watchdog():
    print (system("cd $HOME && git clone https://github.com/flipkart-incubator/watchdog"))
# crlfuzz:
def crlfuzz():
    print (system("cd $HOME && git clone https://github.com/dwisiswant0/crlfuzz"))
# Psqli-pro:
def psqlipro():
    print (system("cd $HOME && git clone https://github.com/Agressiv1njector/psqli-pro"))
# wp-plugin-scanner:
def wppluginscanner():
    print (system("cd $HOME && git clone https://github.com/pywget/wp-plugin-scanner"))
# Optiva-framework:
def optivaframework():
    print (system("cd $HOME && git clone https://github.com/joker25000/Optiva-Framework"))
# shodan-eye:
def shodaneye():
    print (system("cd $HOME && git clone https://github.com/BullsEye0/shodan-eye"))
# SearchSploit:
def searchsploit():
    print (system("cd $HOME && git clone https://github.com/andreafioraldi/cve_searchsploit"))
# webkiller:
def webkiller():
    print (system("cd $HOME && git clone https://github.com/ultrasecurity/webkiller"))
# Raccoon:
def raccoon():
    print (system("cd $HOME && git clone https://github.com/evyatarmeged/Raccoon"))
# phpvulnhunter:
def phpvulnhunter():
    print (system("cd $HOME && git clone https://github.com/OneSourceCat/phpvulhunter"))
# jackhammer:
def jackhammer():
    print (system("cd $HOME && git clone https://github.com/olacabs/jackhammer"))
# Dr0p1t-Framework:
def Dr0p1tframework():
    print (system("cd $HOME && git clone https://github.com/D4Vinci/Dr0p1t-Framework"))
# watchdog:
def watchdog():
    print (system("cd $HOME && git clone https://github.com/flipkart-incubator/watchdog"))
# crlfuzz:
def crlfuzz():
    print (system("cd $HOME && git clone https://github.com/dwisiswant0/crlfuzz"))



# Information Gathering:
# Phoneinfoga:
def Phoneinfoga():
    print (system("cd $HOME && git clone https://github.com/abhinavkavuri/PhoneInfoga"))
# LittleBrother:
def Littlebrother():
    print (system("cd $HOME && git clone https://github.com/Lulz3xploit/LittleBrother"))
# TheHarvester:
def TheHarvester():
    print (system("cd $HOME && git https://github.com/laramies/theHarvester"))
# Infoga:
def Infoga():
    print (system("cd $HOME && git clone https://github.com/m4ll0k/Infoga.git"))
# Userrecon:
def Userrecon():
    print (system("cd $HOME && git clone https://github.com/issamelferkh/userrecon"))
# Report:
def Report():
    print (system("cd $HOME && git clone https://github.com/IlayTamvan/Report"))
# Trity:
def Trity():
    print (system("cd $HOME && git clone https://github.com/darkhunter141/smsfucker-2.0"))
# Inshackle:
def Inshackle():
    print (system("cd $HOME && git clone https://github.com/xd20111/inshackle"))
# Devploit:
def Devploit():
    print (system("cd $HOME && git clone https://github.com/joker25000/Devploit"))
# Infosploit:
def InfoSploit():
    print (system("cd $HOME && git clone https://github.com/CybernetiX-S3C/InfoSploit"))
# Namechk:
def Namechk():
    print (system("cd $HOME &&git clone https://github.com/HA71/Namechk"))
# Sherlock:
def Sherlock():
    print (system("cd $HOME && git clone https://github.com/sherlock-project/sherlock.git"))
# Mac-lookup:
def Maclookup():
    print (system("cd $HOME && git clone https://github.com/T4P4N/Mac-Lookup"))
# GINF:
def GINF():
    print (system("cd $HOME && git clone https://github.com/Gameye98/GINF"))
# Credmap:
def Credmap():
    print (system("cd $HOME && git clone https://github.com/lightos/credmap.git"))
# Choice Bot:
def Choicebot():
    print (system("cd $HOME && git clone https://github.com/sreeram1211/choicebot"))
# Breacher:
def Breacher():
    print (system("cd $HOME && git clone https://github.com/s0md3v/Breacher"))
# Knock Mail:
def Knockmail():
    print (system("cd $HOME && git clone https://github.com/4w4k3/KnockMail.git"))
# Telegram-scraper:
def telegramscraper():
    print (system("cd $HOME && git clone https://github.com/th3unkn0n/TeleGram-Scraper"))
# Socialanalyser:
def socialanalyser():
    print (system("cd $HOME && git clone https://github.com/qeeqbox/social-analyzer"))
# ctfr:
def ctfr():
    print (system("cd $HOME && git clone https://github.com/UnaPibaGeek/ctfr"))
# Osintgram:
def osintgram():
    print (system("cd $HOME && git clone https://github.com/Datalux/Osintgram"))
# snitch:
def snitch():
    print (system("cd $HOME && git clone https://github.com/Smaash/snitch"))
# Infoga-1:
def infoga1():
    print (system("cd $HOME && git clone https://github.com/securitywarrior/Infoga-1"))
# URLDecoder:
def urldecoder():
    print (system("cd $HOME && git clone https://github.com/Anon-Divyanth/URLDecoder"))
# reconcobra:
def reconcobra():
    print (system("cd $HOME && git clone https://github.com/Agent00049/ReconCobra"))
# creepy:
def creepy():
    print (system("cd $HOME && git clone https://github.com/ilektrojohn/creepy"))

# Wifi Hacking
# Wifite:
def Wifite():
    print (system("cd $HOME && wget https://raw.github.com/derv82/wifite/master/wifite.py"))
# Wifite2:
def Wifite2():
    print (system("cd $HOME && git clone https://github.com/derv82/wifite2.git"))
# Routersploit:
def Routersploit():
    print (system("cd $HOME && git clone https://github.com/threat9/routersploit"))
# wifiphisher:
def wifiphisher():
    print (system("cd $HOME && git clone https://github.com/wifiphisher/wifiphisher.git"))
# aircrack-ng:
def aircrackng():
    print (system("apt install root-repo"))
    print (system("apt install aircrack-ng"))
    print ("Then Type sudo airmon-ng")
# wifi-bruteforcer:
def wifibruteforcer():
    print (system("cd $HOME && git clone https://github.com/faizann24/wifi-bruteforcer-fsecurify"))
# Autopixie:
def Autopixie():
    print (system("cd $HOME && git clone https://github.com/nxxxu/AutoPixieWps"))
# ehtools:
def Ehtools():
    print (system("cd $HOME && git clone https://github.com/entynetproject/ehtools"))
# anubis:
def anubis():
    print (system("cd $HOME && git clone https://github.com/jonluca/Anubis"))

# Tracing and tracking
# Trape:
def Trape():
    print (system("cd $HOME && git clone https://github.com/jofpin/trape.git"))
# seeker:
def seeker():
    print (system("cd $HOME && git clone https://github.com/thewhiteh4t/seeker.git"))
# Locator:
def locator():
    print (system("cd $HOME && git clone https://github.com/thelinuxchoice/locator"))
# Firefly:
def Firefly():
    print (system("cd $HOME && git clone https://github.com/M3-SEC/firefly.git"))
# Saycheese:
def saycheese():
    print (system("cd $HOME && git clone https://github.com/Anonymous3-SIT/saycheese"))
# Grabcam:
def grabcam():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/grabcam"))
# camphish:
def camphish():
    print (system("cd $HOME && git clone https://github.com/techchipnet/CamPhish"))
# WishFish:
def Wishfish():
    print (system("cd $HOME && git clone https://github.com/kinghacker0/WishFish"))
# IPCS:
def IPCS():
    print (system("cd $HOME && git clone https://github.com/kancotdiq/ipcs"))
# Sayhellow:
def Sayhellow():
    print (system("cd $HOME && git clone https://github.com/d093w1z/sayhello"))
# lockphish:
def lockphish():
    print (system("cd $HOME && git clone https://github.com/JasonJerry/lockphish"))
# Hacklock:
def Hacklock():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/hacklock"))
# cam-Hackers:
def camhackers():
    print (system("cd $HOME && git clone https://github.com/AngelSecurityTeam/Cam-Hackers"))
# CCTV:
def cctv():
    print (system("cd $HOME && git clone https://github.com/GUNAWAN18ID/cctv"))
# IP-Geolocation:
def IpGeolocation():
    print (system("cd $HOME && git clone https://github.com/maldevel/IPGeoLocation"))
# crips:
def crips():
    print (system("cd $HOME && git clone https://github.com/Manisso/Crips.git"))
# Angry Fuzzer:
def AngryFuzzer():
    print (system("cd $HOME && git clone https://github.com/ihebski/angryFuzzer.git"))
# IP-Tracer:
def Iptracer():
    print (system("cd $HOME && git clone https://github.com/rajkumardusad/IP-Tracer.git"))
# IP-Attack:
def Ipattack():
    print (system("cd $HOME && git clone https://github.com/Bhai4You/Ip-Attack"))
# IP-Tracker:
def Iptracker():
    print (system("cd $HOME && git clone git://github.com/htr-tech/track-ip.git"))
# IP-FY:
def ipfy():
    print (system("cd $HOME && git clone https://github.com/T4P4N/IP-FY"))
# geo-recon:
def georecon():
    print (system("cd $HOME && git clone https://github.com/radioactivetobi/geo-recon"))
# Trackout:
def trackout():
    print (system("cd $HOME && git clone https://github.com/abaykan/TrackOut"))
# m-wiz:
def mwiz():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/m-wiz"))

# Exploitation Tools
# Metasploit:
def metasploit():
    print (" NOTE: It takes over 30 Minutes for installation ")
    x = input(" If U want to install metasploit [y/n] : ")
    if x == "y" or x == "Y":
       print (system("pkg install curl wget"))
       print (system("cd $HOME && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh"))
       print (system("chmod 777 metasploit.sh && ./metasploit.sh"))
       print (system("msfconsole"))
    else:
       exit()
# Beef:
def Beef():
    print (system("cd $HOME && git clone https://github.com/beefproject/beef"))
# Phonesploit:
def Phonesploit():
    print (system("cd $HOME && git clone https://github.com/Zucccs/PhoneSploit"))
# websploit:
def websploit():
    print (system("cd $HOME && git clone https://github.com/websploit/websploit.git"))
# A-Rat:
def ARat():
    print (system("cd $HOME && git clone https://github.com/Xi4u7/A-Rat"))
# The FatRat:
def Thefatrat():
    print (system("cd $HOME && git clone https://github.com/Screetsec/TheFatRat.git"))
# viel-Evasion:
def vielEvasion():
    print (system("cd $HOME && git clone https://github.com/Veil-Framework/Veil-Evasion.git"))
# Evil-Droid:
def Evildroid():
    print (system("cd $HOME && git clone https://github.com/M4sc3r4n0/Evil-Droid.git"))
# TMvenom:
def TMvenom():
    print (system("cd $HOME && git clone https://github.com/TechnicalMujeeb/tmvenom.git"))
# Duck-Droid:
def Duckdroid():
    print (system("cd $HOME && git clone https://github.com/T4Termux/Duck_Droid.git"))
# Ghost-Framework:
def Ghostframework():
    print (system("cd $HOME && git clone https://github.com/entynetproject/ghost"))
# Commix:
def commix():
    print (system("cd $HOME && git clone https://github.com/commixproject/commix.git"))
# Parat:
def parat():
    print (system("cd $HOME && git clone https://github.com/micle-fm/Parat"))
# MSF-Pg:
def MSFpg():
    print (system("cd $HOME && git clone https://github.com/haxzsadik/MSF-Pg"))
# AndroBugs_Framework:
def AndroBugs_Framework():
    print (system("cd $HOME && git clone https://github.com/AndroBugs/AndroBugs_Framework"))
# Weevely:
def Weevely():
    print (system("cd $HOME && git clone https://github.com/sunge/Weevely"))
# spade:
def spade():
    print (system("cd $HOME && git clone https://github.com/NVlabs/SPADE"))
# brutal:
def brutal():
    print (system("cd $HOME && git clone https://github.com/Screetsec/Brutal"))

# password Attacking
# John the ripper:
def johntheripper():
    print (system("cd $HOME && git clone https://github.com/magnumripper/JohnTheRipper.git"))
# Hashcat:
def Hashcat():
    print (system("apt install unstable-repo"))
    print (system("apt install hashcat"))
    print ("Type \" hashcat \" to Start ")
# hasher:
def Hasher():
    print (system("cd $HOME && git clone https://github.com/CiKu370/hasher"))
# Hash-Cracker:
def Hashcracker():
    print (system("cd $HOME && git clone https://github.com/jclebreton/hash-cracker"))
# Hash-Buster:
def Hashbuster():
    print (system("cd $HOME && git clone https://github.com/s0md3v/Hash-Buster"))
# Hash-Generator:
def Hashgenerator():
    print (system("cd $HOME && git clone https://github.com/CiKu370/hash-generator"))
# Hasherdoit:
def Hasherdoit():
    print (system("cd $HOME && git clone https://github.com/galauerscrew/hasherdotid"))

# Malicious tools
# Thezoo:
def Thezoo():
    print (system("cd $HOME && git clone https://www.github.com/ytisf/theZoo"))
# Beelogger:
def Beelogger():
    print (system("cd $HOME && git clone https://github.com/4w4k3/BeeLogger.git"))
# Hatkey:
def Hatkey():
    print (system("cd $HOME && git clone https://github.com/Naayouu/Hatkey"))
# Vbug:
def Vbug():
    print (system("cd $HOME && git clone https://github.com/Junior60/vbug"))
# Malicious:
def Malicious():
    print (system("cd $HOME && git clone https://github.com/Hider5/Malicious"))
# Infect:
def infect():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/Infect"))
# Spammer-Grab:
def Spammergrab():
    print (system("cd $HOME && git clone https://github.com/p4kl0nc4t/Spammer-Grab"))
# papaviruz:
def papaviruz():
    print (system("cd $HOME && git clone https://github.com/Hacking-pch/papaviruz"))
# vanish:
def vanish():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/vanish"))

# Bombing Tools
# Tbomb:
def Tbomb():
    print (system("cd $HOME && git clone https://github.com/TheSpeedX/TBomb.git"))
# Quack:
def Quack():
    print (system("cd $HOME && git clone https://github.com/entynetproject/quack"))
# Hbomb:
def Hbomb():
    print (system("cd $HOME && git clone https://github.com/HoneyPots0/HBomb"))
# Email-Bomber:
def Emailbomber():
    print (system("cd $HOME && git clone https://github.com/mohinparamasivam/Email_Bomber.git"))
# E-Bomber:
def EBomber():
    print (system("cd $HOME && git clone https://github.com/darkhunter141/G-Bomber-141-2.0"))
# EMBomber:
def EMBomber():
    print (system("cd $HOME && git clone https://github.com/darkhunter141/G-Bomber-141-2.0"))
# Avarspam:
def Avarspam():
    print (system("cd $HOME && git clone https://github.com/ALX-04/AVARspam"))
# Spamwa:
def Spamwa():
    print (system("cd $HOME && git clone https://github.com/krypton-byte/SpamWa"))
# LiteOTP:
def Liteotp():
    print (system("apt install php wget"))
    print (system("cd $HOME && wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite"))
    print (" Type \" lite \" to start")
# SpazSms:
def SpazSms():
    print (system("cd $HOME && git clone https://github.com/Gameye98/SpazSMS"))
# Bombers:
def bombers():
    print (system("cd $HOME && git clone https://github.com/bhattsameer/Bombers"))
# Telegram:
def telegram():
    print (system("cd $HOME && git clone https://github.com/th3unkn0n/TeleGram-Scraper"))
# ispammer:
def ispammer():
    print (system("cd $HOME && git clone https://github.com/MrSp4rX/iSpammer"))
# Sms-BomB
def smsbomb():
    print (system("cd $HOME && git clone https://github.com/Bhai4You/SmS-BomB"))
# SMSBomber300:
def smsbomber300():
    print (system("cd $HOME && git clone https://github.com/Ivan-Hacker-700/SMSBomber300"))
# bomberthon:
def bomberthon():
    print (system("cd $HOME && git clone https://github.com/b31ngD3v/bomberthon"))
# Mbomb:
def mbomb():
    print (system("cd $HOME && git clone https://github.com/palahsu/MBomb"))
# WhataBomb:
def whatabomb():
    print (system("cd $HOME && git clone https://github.com/tbhaxor/whatabomb"))
# fast-mail-bomber:
def fastmailbomber():
    print (system("cd $HOME && git clone https://github.com/juzeon/fast-mail-bomber"))
# email-hack:
def emailhack():
    print (system("cd $HOME && git clone https://github.com/Macr0phag3/email_hack"))
# Hpomb:
def hpomb():
    print (system("cd $HOME && git clone https://github.com/xd20111/HBomb"))
# spamx:
def spamx():
    print (system("cd $HOME && git clone https://github.com/noob-hackers/spamx"))
# call:
def call():
    print (system("cd $HOME && git clone https://github.com/S4NZ-ID/Call"))

# ddos tools
# Hammer:
def hammer():
    print (system("cd $HOME && git clone https://github.com/cyweb/hammer"))
# Torjan:
def torjan():
    print (system("cd $HOME && git clone https://github.com/ZK1Hacker/TORJAN"))
# X-Attack:
def xattack():
    print (system("cd $HOME && git clone https://github.com/CharlieTheHack1/X-Attack"))
# MCIDDOS:
def mciddos():
    print (system("cd $HOME && git clone https://github.com/MrTamfanX/MCIDDOS"))
# ddos-dos-tools:
def ddosdostools():
    print (system("cd $HOME && git clone https://github.com/wenfengshi/ddos-dos-tools"))
# Saddam:
def saddam():
    print (system("cd $HOME && git clone https://github.com/OffensivePython/Saddam"))
# fastnetmon:
def fastnetmon():
    print (system("cd $HOME && git clone https://github.com/pavel-odintsov/fastnetmon"))
# Liteddos:
def liteddos():
    print (system("cd $HOME && git clone https://github.com/4L13199/LITEDDOS"))
# ddos-ripper:
def ddosripper():
    print (system("cd $HOME && git clone https://github.com/palahsu/DDoS-Ripper"))

# Special Pakages
# Splitting terminals:
def Split():
    print (system("cd $HOME && pkg install tmux"))
    intro = "\033[1;34m This pakage is helps for splitting terminals into many types\n Type \n \t\t \033[1;32m tmux \033[1;34m \n After type.. \n\t\t \033[1;32m ctrl % b \033[0m \n\n"
    sleep(0.5)
    for t in intro:
      sys.stdout.write (t)
      sys.stdout.flush()
      sleep(0.1)



# Chatting:
def Chat():
    print (system("cd $HOME && pkg install irssi"))
    irss = "\033[1;34m This pakage 'irssi' is an Internet relay chat client since 1999. you can chat with a group of people by joining a channel at number of available servers.You can create your own channel(Group) on irssi which is completely free and your friends can join the same channel to chat with you \033[0m \ntype\n\t\t\033[1;32m irssi\n\033[0mAfter type\n\t\t\033[1;32m \help\033[0m\n"
    sleep(0.5)
    for i in irss:
     sys.stdout.write(i)
     sys.stdout.flush()
     sleep(0.1)

# Browse:
def Browse():
    print (system("cd $HOME && pkg install w3m"))
    brow = "\033[1;34m This Pakage is for Browsing internet through termux app\n\033[0m Type\n\t\t \033[1;32m w3m www.google.com\n\033[0m"
    sleep(0.5)
    for b in brow:
     sys.stdout.write(b)
     sys.stdout.flush()
     sleep(0.1)


# System info:
def Sysinfo():
    print (system("cd $HOME && pkg install screenfetch"))
    info = "\033[1;34m This pakage is a System Information Tool. It helps to find our system internal core informatio\033[0m\nType\033[1;32m\n\t\t screenfetch\033[0m\n"
    sleep(0.5)
    for i in info:
     sys.stdout.write(i)
     sys.stdout.flush()
     sleep(0.1)

# Hollywood:
def Hollywood():
    print (system("cd $HOME && pkg install hollywood"))
    print ("\033[1;34m\nType\n\t\t\033[1;32m hollywood\033[0m\n")
# Cmatrix:
def Cmatrix():
    print (system("cd $HOME && pkg install cmatrix"))
    print ("\033[1;34m\nType\n\t\t\033[1;32m cmatrix\033[0m\n")
# Fire:
def Fire():
    print (system("cd $HOME && pkg install libcaca"))
    print ("\033[1;34m\nType\n\t\t\033[1;32m libcaca\033[0m\n")
# Toilet:
def toilet():
    print (system("cd $HOME && pkg install toilet"))
    print ("\033[1;34m\nType\n\t\t\033[1;32m toilet -f mono12 -F gay 'your text'\033[0m")

# Another Hacking Tools
# Tool-X:
def ToolX():
    print (system("cd $HOME && git clone https://github.com/rajkumardusad/Tool-X.git"))
# :
def darkhunter():
    print (system("cd $HOME && git clone https://github.com/darkhunter141/Web-Hunter "))
# Dark-fly:
def Darkfly():
    print (system("cd $HOME && git clone https://github.com/Ranginang67/DarkFly-Tool"))
# Easy-Hack:
def Eayhack():
    print (system("cd $HOME && git clone https://github.com/sabri-zaki/EasY_HaCk"))
# Lazymux:
def Lazymux():
    print (system("cd $HOME && git clone https://github.com/Gameye98/Lazymux"))
# Fsociety:
def Fsociety():
    print (system("cd $HOME && git clone https://github.com/Manisso/fsociety"))
# lazy:
def Lazy():
    print (system("cd $HOME && git clone https://github.com/arismelachroinos/lscript.git"))
# Lazyscript:
def Lazyscript():
    print (system("cd $HOME && git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git"))
# AK47:
def AK47():
    print (system("cd $HOME && git clone https://github.com/nasirxo/AK47"))
# Thechoice:
def Thechoice():
    print (system("cd $HOME && git clone https://github.com/thelinuxchoice/thechoice"))
# Theinspector:
def Theinspector():
    print (system("cd $HOME && git clone https://github.com/Moham3dRiahi/Th3inspector.git"))
# txtool:
def txtool():
    print (system("cd $HOME && git clone https://github.com/kuburan/txtool.git"))
# Hackerpro:
def Hackerpro():
    print (system("cd $HOME && git clone https://github.com/technicaldada/hackerpro.git"))
# Facebook-Toolkit:
def Facebooktoolkit():
    print (system("cd $HOME && git clone https://github.com/warifp/FacebookToolkit"))
# GoldenEye:
def GoldenEye():
    print (system("cd $HOME && git clone https://github.com/jseidl/GoldenEye"))
# Hacktronian:
def Hacktronian():
    print (system("cd $HOME && git clone https://github.com/thehackingsage/hacktronian.git"))
# Tool-N:
def ToolN():
    print (system("cd $HOME && git clone https://github.com/novalattasya/Tool-N"))
# Hackingtool:
def Hackingtool():
    print (system("cd $HOME && git clone https://github.com/Z4nzu/hackingtool.git"))
# D-tect:
def Dtect():
    print (system("cd $HOME && git clone https://github.com/shawarkhanethicalhacker/D-TECT-1"))
# King-Hacking:
def kingHacking():
    print (system("cd $HOME && git clone https://github.com/king-hacking/King-Hacking.git"))
# Slowrosis:
def Slowrosis():
    print (system("cd $HOME && git clone https://github.com/gkbrk/slowloris.git"))
# Hulk:
def Hulk():
    print (system("cd $HOME && git clone https://github.com/grafov/hulk"))
# Ddos-Attack:
def DdosAttack():
    print (system("cd $HOME && git clone https://github.com/Ha3MrX/DDos-Attack"))
# Hunner:
def Hunner():
    print (system("cd $HOME && git clone https://github.com/b3-v3r/Hunner"))
# xerxes:
def xerxes():
    print (system("cd $HOME && git clone https://github.com/XCHADXFAQ77X/XERXES"))
# Planetwork-DDOS:
def PlanetworkDDOS():
    print (system("cd $HOME && git clone h-ttps://github.com/Hydra7/Planetwork-DDOS"))
# pureblood:
def pureblood():
    print (system("cd $HOME && git clone https://github.com/cr4shcod3/pureblood"))
# Darksploit:
def Darksploit():
    print (system("cd $HOME && git clone https://github.com/LOoLzeC/DarkSploit"))
# hakkuframework:
def hakkuframework():
    print (system("cd $HOME && git clone https://github.com/4shadoww/hakkuframework"))
# Optiva-framework:
def Optivaframework():
    print (system("cd $HOME && git clone https://github.com/joker25000/Optiva-Framework"))
# Gloom-Framework:
def Gloomframework():
    print (system("cd $HOME && git clone https://github.com/joshDelta/Gloom-Framework.git"))
# Host:
def host():
    print (system("cd $HOME && git clone https://github.com/htr-tech/host"))
# oxidtools:
def oxidtools():
    print (system("cd $HOME && git clone https://github.com/risspect/OXIDTools"))
# tstyle:
def tstyle():
    print (system("cd $HOME && git clone https://github.com/htr-tech/tstyle"))
# bash2mp4:
def bash2mp4():
    print (system("cd $HOME && git clone https://github.com/htr-tech/bash2mp4"))
# shorturl:
def shorturl():
    print (system("cd $HOME && git clone https://github.com/htr-tech/shorturl"))
# proxy-finder:
def proxyfinder():
    print (system("cd $HOME && git clone https://github.com/sabri-zaki/PROXY_FINDER"))
# Pentesting-Bible:
def pentestingbible():
    print (system("cd $HOME && git clone https://github.com/blaCCkHatHacEEkr/PENTESTING-BIBLE"))
# pureblood:
def pureblood():
    print (system("cd $HOME && git clone https://github.com/johnjohnsp1/pureblood"))
# Darksploit:
def darksploit():
    print (system("cd $HOME && git clone https://github.com/anthrax3/DarkSploit"))
# hakkuframework:
def hakkuframework():
    print (system("cd $HOME && git clone https://github.com/4shadoww/hakkuframework"))
# optiva-framework:
def optivaframework():
    print (system("cd $HOME && git clone https://github.com/joker25000/Optiva-Framework"))
# Gloom-Framework:
def gloomframework():
    print (system("cd $HOME && git clone https://github.com/StreetSec/Gloom-Framework"))



# BackToMenu:
def BackToMenu():
   python = sys.executable
   os.execl(python,python,* sys.argv)
   curdir = os.getcwd()
# Restart:
def Restart():
     try:
       x = input(" {}[{}*{}]{} Return to menu [Y/N] : {}".format(R,W,R,W,G))
     except KeyboardInterrupt:
       print(O)
       exit()
     if x == "y" or x == "Y":
       sleep(0.5)
       BackToMenu()
     else:
       print(O)
       exit()
