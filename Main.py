import random
from colorama import Fore
import time
from matplotlib import pyplot as plt

isim=input("Ismin ne yabancı?")


hile_sayar=0

p_altin=0
p_can=100
p_hasar=10
p_kalkan=0
p_kilic=0
p_puan=0

if isim=="ahmetmustafamehmet":
    p_puan=10000

else:
    pass

guc_iksiri=1
can_iksiri=1
iksir_etkisi=False

x_can=0
x_hasar=0
x_altin=0
x_puan=0
hasar=0
dusmanlar= {
    "Fare" : {"can":60,"hasar":7,"altın":10,"puan":5},

    "Kangal":{"can":95,"hasar":16,"altın":25,"puan":12},

    "Goblin":{"can":125,"hasar":21,"altın":30,"puan":15},

    "Ork":{"can":150,"hasar":25,"altın":40,"puan":20},

    "Ejderha":{"can":275,"hasar":30,"altın":1000,"puan":50}
}

def saldiri():
    global x_can, iksir_etkisi, p_hasar
    krit=["0","0","0","1","2"]
    krit_sans=random.choice(krit)

    if krit_sans=="0":
        print(Fore.LIGHTBLUE_EX+"Normal hasar vurdun (-10)")
        p_hasar=10

    elif krit_sans=="1":
        print(Fore.LIGHTGREEN_EX+"KRİTİK hasar vurdun (-25)")
        p_hasar=25

    elif krit_sans=="2":
        print(Fore.RED+"Kaçırdın dostum...(0)")
        p_hasar=0

    if iksir_etkisi:
        p_hasar+=15
        iksir_etkisi=False

    if p_kilic==1:
        p_hasar+=10

    elif p_kilic==2:
        p_hasar+=15

    elif p_kilic==3:
        p_hasar+=25

    else:
        pass

    x_can-=p_hasar
    print(f"canavarın bu kadar canı kaldı [{x_can}] ")
def savunma():

    global x_hasar, p_can, hasar
    hasar=x_hasar
    Savunmaa=["0","1","2","3","0"]
    Savunma=random.choice(Savunmaa)

    if Savunma=="0":
        print("Normal hasar yedin kral.")
        hasar+=0

    elif Savunma=="1":
        print("Hasarın çoğunu somurdun.")
        hasar-=6

    elif Savunma=="2":
        print("Hasar bile almadan mükemmel akrabosi ile kaçtın")
        hasar-=15

    elif Savunma=="3":
        print("Kendi kılıcın senin yüzüne geldi ve düşmanda sana vurdu")
        hasar+=10

    if p_kalkan==1:
        hasar-=8
        print(f"Rakibin sana aslında {hasar+8} kadar vuracaktı ama şimdi {hasar} vuruyor!")

    elif p_kalkan==2:
        hasar-=14
        print(f"Rakibinin 14 hasarını engelledin tebrikler!")

    elif p_kalkan==3:
        hasar-=22

    if hasar>0:
      p_can-=hasar

    elif hasar<0:
     print("Rakibin kalkanın yüzünden sana saldıramadı!")

    print(f"canın {p_can} ")
def iksir():
    global guc_iksiri, can_iksiri, iksir_etkisi, p_can

    print("2 seçeneğin var...")
    time.sleep(0.6)

    print(Fore.RED+"Güç iksiri yada Can iksiri...")
    print("2 sindende 1 er adet vardır")

    ik=input("Can iksiri için can Güç iksiri için güç").lower()

    if ik=="güç" and guc_iksiri>0:
        guc_iksiri-=1
        iksir_etkisi=True

    elif ik=="can" and can_iksiri>0:
        can_iksiri-=1
        p_can+=21

        if p_can>100:
            p_can=100
            print(Fore.GREEN+"Canın şuan tam dolu")
        else:
            print(f"Canın şuan {p_can} seviyesinde")
            pass
def olum_zarlari():
    global x_can, p_can,iksir_etkisi
    print("Hayatının en büyük kaosuna hazırmısın?")
    time.sleep(0.6)
    x=input("evet yada hayır").lower()
    if x=="evet":
        if x_can>p_can:

            if 50<p_can<100:
                x_can-=25

            elif 25<p_can<50:
                x_can-=35
                iksir_etkisi=True
                print(Fore.RED + "İKSİR ETKİSİ VERİLDİ!!!")

        elif p_can>x_can:

            if 50<p_can<=100:
                p_can-=30
                iksir_etkisi=True
                print(Fore.RED + "İKSİR ETKİSİ VERİLDİ!!!")

            elif 20<p_can<=50:
                p_can-=40

            elif p_can<=20:
                iksir_etkisi=True
                print(Fore.RED+"İKSİR ETKİSİ VERİLDİ!!!")

        elif p_can==x_can:
            x_can-=25
            p_can-=30
            iksir_etkisi=True
            print(Fore.RED + "İKSİR ETKİSİ VERİLDİ!!!")

    elif x=="hayır":
        pass
def macera_fin():

    global p_puan

    isimler_list = []
    puanlar_list = []

    if p_kilic==3:
        p_puan+=25
    if p_kalkan==3:
        p_puan+=30
    if p_kalkan==3 and p_kilic==3:
        p_puan+=40


    ppp=str(p_puan)
    with open ("skor.txt","a",encoding="utf-8") as k:
        k.write(f"{isim},{ppp}\n")

    try:
     with open("skor.txt","r",encoding="utf-8") as file:
        for p in file:
            p=p.strip()
            if p:
               parca=p.split(",")
               if len(parca)==2:
                  isimler_list.append(parca[0])
                  puanlar_list.append(int(parca[1]))
    except FileNotFoundError:
     pass
    liste=list(zip(isimler_list,puanlar_list))
    liste.sort(key=lambda x: x[1],reverse=True)
    print(liste)
    x=isimler_list
    y=puanlar_list
    plt.xlabel("isimler")
    plt.ylabel("puanlar")
    plt.title("Skoarboard")
    plt.bar(x,y)
    plt.show()
def kayip_ekle():
    toplam_kayip = 0
    # Mevcut kayıp sayısını dosyadan oku
    try:
        with open("kayiplar.txt", "r", encoding="utf-8") as f:
            icerik = f.read().strip()
            if icerik:
                toplam_kayip = int(icerik)
    except FileNotFoundError:
        toplam_kayip = 0

    # Kayıp sayısını 1 artır ve kaydet
    toplam_kayip += 1
    with open("kayiplar.txt", "w", encoding="utf-8") as f:
        f.write(str(toplam_kayip))

    # Atmosferik ölüm ekranı
    print(Fore.RED + "\n" + "="*45)
    print(Fore.RED + f"Bu macerada kaybolan maceracı sayısı: {toplam_kayip}")
    print(Fore.RED + "Hikâyen zindanların karanlığında çürümeye terk edildi...")
    print(Fore.RED + "="*45 + "\n")
def market():
    global p_kalkan, p_kilic, can_iksiri, guc_iksiri, p_altin

    print(Fore.GREEN+"*"*30+
          "\n*** "+Fore.BLUE+"Kılıç geliştirmesi için 1 "+Fore.GREEN+"***\n"
          +"*"*30+
          "\n*** "+Fore.BLUE+"Kalkan geliştrimesi için 2 "+Fore.GREEN+"***\n"
          +"*"*30+
          "\n*** "+Fore.RED+"İksir almak için 3 "+Fore.GREEN+"***\n"
          +"*"*30)

    print(Fore.RED+"Kral ilk kılıç geliştirmesi 10 altındır ilk kalkan ise 8 altındır")

    if p_kilic==3 and p_kalkan==3 and can_iksiri>2 and guc_iksiri>2:
        print("Herşeyin tamam alınabilecek bişey kalmadı!")

    elif p_kilic!=3 or p_kalkan!=3 or can_iksiri!=3 or guc_iksiri!=3:
     try:
      Gelistirme=int(input("1,2 veya 3 ü seçiniz"))
     except ValueError:
        print("Geçersiz giriş!")
        return

     if Gelistirme==1:

        if p_kilic<1 and p_altin>=10:
            p_kilic+=1
            p_altin-=10
            print(Fore.LIGHTMAGENTA_EX+"KILICIN SEVİYE YÜKSELDİ 10 HASAR ARTIŞI")

        elif 0<p_kilic<2 and p_altin>=16:
            p_kilic+=1
            p_altin-=16
            print(Fore.MAGENTA + "KILICIN SEVİYE YÜKSELDİ 5 HASAR ARTIŞI")

        elif 1<p_kilic<3 and p_altin>=22:
            p_kilic+=1
            p_altin-=22
            print(Fore.LIGHTBLUE_EX + "KILICIN SEVİYE YÜKSELDİ 10 HASAR ARTIŞI")

        elif p_kilic==3:
            print(Fore.RED+"Kılıcın maks seviyede!")

        else:
            print("paran yetersiz")

     elif Gelistirme==2:

        if p_kalkan<1 and p_altin>=8:
            p_kalkan+=1
            p_altin-=8
            print(Fore.YELLOW+"Kalkanın seviye yükseldi 8 hasar azaltımı!")

        elif 0<p_kalkan<2 and p_altin>=18:
            p_kalkan+=1
            p_altin-=18
            print(Fore.LIGHTYELLOW_EX+"Kalkanın seviye yükseldi 6 hasar azaltımı!")

        elif 1<p_kalkan<3 and p_altin>=26:
            p_kalkan+=1
            p_altin-=26
            print(Fore.CYAN+"Kalkanın seviye yükseldi 8 hazar azaltımı!")

        elif p_kalkan==3:
            print(Fore.RED+"Kalkanın maks seviyede!")

        else:
            print("paran yetersiz")

     elif Gelistirme==3:
          print(Fore.LIGHTRED_EX+"Güç iksiri için tanesine 7 altın\n"+
                Fore.RED+"Can iksiri içinse tanesine 5 altın\n"+
                Fore.LIGHTRED_EX+"Güç iksiri için 1///Can iksiri için 2")
          print("İptal için '0' yazın")
          try:
           secenek=int(input("Seçiminizi yapın: "))
          except ValueError:
              print("Geçersiz giriş!")
              return

          if secenek==1 and p_altin>=7:
              guc_iksiri+=1
              p_altin-=7
              print(Fore.GREEN+"Güç iksiriniz alındı!")

          elif secenek==1 and p_altin<7:
              print("Güç iksirine verecek paran bulunmamakta!")

          elif secenek==2 and p_altin<5:
              print(Fore.RED+"Can iksirini alacak paran yok!")

          elif secenek==2 and p_altin>=5:
              can_iksiri+=1
              p_altin-=5
              print(Fore.GREEN+"Can iksiriniz alındı!")

          elif secenek==0:
                pass
def menu():
    print(Fore.RED+f"Düşmanın canı:{x_can}")
    print(Fore.LIGHTGREEN_EX+f"Senin canın {p_can}")
    print(Fore.RED+"-"*30+
          "\n-------"+Fore.CYAN+" MENÜÜÜÜ "+Fore.RED+"--------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 1*Saldırı "+Fore.RED+"------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 2*İksir içme "+Fore.RED+"---------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 3*Ölüm zarları "+Fore.RED+"-------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 4*Market "+Fore.RED+"-------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 5*Macerayı bitir. "+Fore.RED+"----\n"
          +"-"*30)
while True:

    if x_can<=0:
        p_altin+=x_altin
        p_puan+=x_puan
        print("1 - Fare")
        print("2 - Kangal")
        print("3 - Goblin")
        print("4 - Ork")
        print("5 - Ejderha")
        dusman_seciyor = input("Düşman seç: ")

        if dusman_seciyor=="1":
            dusman="Fare"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
            x_puan = dusmanlar[dusman]["puan"]

        elif dusman_seciyor=="2":
            dusman="Kangal"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
            x_puan = dusmanlar[dusman]["puan"]

        elif dusman_seciyor=="3":
            dusman="Goblin"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
            x_puan = dusmanlar[dusman]["puan"]

        elif dusman_seciyor=="4":
            dusman="Ork"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
            x_puan = dusmanlar[dusman]["puan"]
        elif dusman_seciyor=="5":
            dusman="Ejderha"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
            x_puan = dusmanlar[dusman]["puan"]

    menu()
    sec=input("Hangisini seçeceksiniz? {1-2-3-4-5}")

    if sec=="1":
        saldiri()
        print(f"Saldırdın verdiğin hasar:{p_hasar}")
        savunma()
        print(f"Düşman sana saldırdı ve verdiği hasar {hasar}")
        if p_can<=0:
            kayip_ekle()
            break

    elif sec=="2":
        iksir()
        print("iksir içildi!")
        print(f"canın {p_can} ")

    elif sec=="3":
        print(Fore.RED+"olum zarlari!")
        olum_zarlari()
        if p_can<=0:
            print(Fore.RED+"Ruhun, zarların yarattığı kaosa yenik düştü."
                  " Artık ne bir puanın var ne de geri dönebilecek bir bedenin...")
            kayip_ekle()
            break


    elif sec=="4":
        market()

    elif sec=="5":
        macera_fin()
        break

    else:
        print("Kral 1 2 3 4 5 ya basıcaksın o kadar!")