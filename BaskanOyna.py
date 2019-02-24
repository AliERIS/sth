import database
import BaskanMenu
import BSonrakiHafta
def Oynat():
    secim111=int(input("""
1-)Sonraki Hafta
2-)Oyuncuları Öv
3-)Oyuncuları Yer
4-)Oyunculara Doping yaptır
5-)Transfer Yap
6-)Menajeri Öv
7-)Menajeri Yer
8-)Menajeri Kov
9-)Menajere Baskı Yap
10-)Yeni Menajer
11-)Hakemleri Yer
12-)Hakemleri Öv
13-)Bildiri İmzala
14-)Sponsor Bul
15-)Medyada Agresif Tavır takın
16-)Medyada sakin tavır takın
17-)Şike Yap
18-)Istifa Et"""))
    if(secim111==1): # SONRAKİ HAFTA
        BSonrakiHafta.SonrakiHafta()
        
    elif(secim111==2): #  Oyuncuları ÖV
        for q in range (0,len(BaskanMenu.playerlist)):
            BaskanMenu.playerlist[q].morale+=database.bosses.listofbosses[secim11-1].charisma/10
            if(BaskanMenu.playerlist[q].intel>50):
                BaskanMenu.playerlist[q].form+=1
            else:
                BaskanMenu.playerlist[q].form-=1
    elif(secim111==3): #Oyuncuları Yer
        for q in range (0,len(BaskanMenu.playerlist)):
            BaskanMenu.playerlist[q].morale-=database.bosses.listofbosses[secim11-1].charisma/20
            if(BaskanMenu.playerlist[q].intel>80):
                BaskanMenu.playerlist[q].form+=2
            else:
                BaskanMenu.playerlist[q].form-=1

    elif(secim111==4): #Oyunculara doping yaptır
    elif(secim111==5): #Transfer yap
    elif(secim111==6):#menajeri öv
    elif(secim111==7):#menajeri Yer
    elif(secim111==8):#menajeri Kov
    elif(secim111==9):#menajere baskı yap
    elif(secim111==10):#Yeni menajer
    elif(secim111==11):#Hakemleri yer
    elif(secim111==12):#hakemleri öv
    elif(secim111==13):#bildiri İmzala
    elif(secim111==14):#Sponsor Bul
    elif(secim111==15):#Medyaya Agresif
    elif(secim111==16):#Medyaya sakin
    elif(secim111==17):#şike yap
    elif(secim111==18):#istifa et
