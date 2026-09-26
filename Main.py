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

