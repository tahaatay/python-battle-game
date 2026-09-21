import random
from colorama import Fore
import time

hile_sayar=0
p_can=100
p_hasar=10
x_can=150
x_hasar=15

guc_iksiri=1
can_iksiri=1
iksir_etkisi=False

def saldiri():
    global x_can, iksir_etkisi
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

    if iksir_etkisi==True:
        p_hasar+=15
        iksir_etkisi=False

    x_can-=p_hasar
    print(f"canavarın canı {x_can} ")
def savunma():

    global x_hasar, p_can
    Savunmaa=["0","1","2","3","0"]
    Savunma=random.choice(Savunmaa)
    if Savunma=="0":
        print("Normal hasar yedin kral.(-15)")
        x_hasar=15

    elif Savunma=="1":
        print("Hasarın çoğunu somurdun. (-5)")
        x_hasar=5

    elif Savunma=="2":
        print("Hasar bile almadan mükemmel akrabosi ile kaçtın (0)")
        x_hasar=0

    elif Savunma=="3":
        print("Kendi kılıcın senin yüzüne geldi ve düşmanda sana vurdu(-25)")
        x_hasar=25

    p_can-=x_hasar
    print(f"canın {p_can} ")
def iksir():
    global guc_iksiri, can_iksiri, iksir_etkisi, p_can

    print("2 seçeneğin var...")
    time.sleep(0.6)
    print(Fore.RED+"Güç iksiri yada Can iksiri...")
    print("2 sindende 1 er adet vardır")
    iksir=input("Can iksiri için can Güç iksiri için güç").lower()
    if iksir=="güç" and guc_iksiri>0:
        guc_iksiri-=1
        iksir_etkisi=True
    elif iksir=="can" and can_iksiri>0:
        can_iksiri-=1
        p_can+=21
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

def menu():
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
          +"-"*30)

while p_can>0 and x_can>0:
    menu()
    sec=input("Hangisini seçeceksiniz? {1-2-3-4}")

    if sec=="1":
        saldiri()
        print("Eğer bu seçeneği 2 kere aynı anda kullanırsan oyuncu kendini infaz eder!!!")
        print("İntihar etmemesi için savunma yapman gerekicek!")
        hile_sayar+=1
        if x_can<=0:
            print("CANAVAR ÖLDÜ")
            break

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

    else:
        print("Kral 1 2 3 4 e basıcaksın o kadar!")