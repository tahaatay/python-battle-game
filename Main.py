import random
from colorama import Fore
import time

hile_sayar=0

p_altin=0
p_can=100

p_hasar=10

p_kalkan=0
p_kilic=0

guc_iksiri=1
can_iksiri=1
iksir_etkisi=False

x_can=0
x_hasar=0
hasar=0
x_altin=0
dusmanlar= {
    "Fare" : {
        "can":60,
        "hasar":7,
        "altın":10
    },
    "Kangal":{
        "can":95,
        "hasar":16,
        "altın":25,
    },
    "Goblin":{"can":125,"hasar":21,"altın":30},

    "Ork":{"can":150,"hasar":25,"altın":40},

    "Ejderha":{"can":275,"hasar":30,"altın":1000
    }
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
        hasar+=5

    elif Savunma=="1":
        print("Hasarın çoğunu somurdun.")
        hasar+=5

    elif Savunma=="2":
        print("Hasar bile almadan mükemmel akrabosi ile kaçtın")
        hasar+=0

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

    if x_hasar>0:
      p_can-=x_hasar

    elif x_hasar<0:
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
      Gelistirme=int(input("1,2 veya 3 ü seçiniz"))

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
          print("İptal için '000' yazın")
          secenek=int(input("Seçiminizi yapın: "))
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
          elif secenek==000:
                pass
def menu():
    print(Fore.RED+f"Düşmanın canı:{x_can}")
    print(Fore.LIGHTGREEN_EX+f"Senin canın {p_can}")
    print(Fore.RED+"-"*30+
          "\n-------"+Fore.CYAN+" MENÜÜÜÜ "+Fore.RED+"--------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 1*Saldırı "+Fore.RED+"------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 2*Savunma "+Fore.RED+"------------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 3*İksir içme "+Fore.RED+"---------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 4*Ölüm zarları "+Fore.RED+"-------\n"
          +"-"*30+
          "\n-------"+Fore.BLUE+" 5*Market "+Fore.RED+"-------------\n"
          +"-"*30)
while p_can>0:

    if x_can<=0:
        p_altin+=x_altin

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
        elif dusman_seciyor=="2":
            dusman="Kangal"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
        elif dusman_seciyor=="3":
            dusman="Goblin"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
        elif dusman_seciyor=="4":
            dusman="Ork"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]
        elif dusman_seciyor=="5":
            dusman="Ejderha"
            x_can = dusmanlar[dusman]["can"]
            x_hasar = dusmanlar[dusman]["hasar"]
            x_altin = dusmanlar[dusman]["altın"]

    menu()
    sec=input("Hangisini seçeceksiniz? {1-2-3-4}")

    if sec=="1":
        saldiri()
        print("Eğer bu seçeneği 2 kere aynı anda kullanırsan oyuncu kendini infaz eder!!!")
        print("İntihar etmemesi için savunma yapman gerekicek!")
        hile_sayar+=1


        if hile_sayar==2:
            p_can=0
            print("Oyuncu kendini infaz etti hileci!!!")
            break

    elif sec=="2":
        savunma()
        hile_sayar-=1
        if p_can<=0:
            break

    elif sec=="3":
        iksir()
        print("iksir içildi!")
        print(f"canın {p_can} ")

    elif sec=="4":
        print(Fore.RED+"olum zarlari!")
        olum_zarlari()
        if x_can<=0:
            print("Canavar öldü...")
            break
        elif p_can<=0:
            print("Ölümün zarları senin ruhunu içti ve öldün...")
            break
    elif sec=="5":
        market()

    else:
        print("Kral 1 2 3 4 5 e basıcaksın o kadar!")
