import database
import BaskanOyna
def Oyna():
    secim11=int(input("""
1-)Ali Koç
2-)Fikret Orman
3-)Mustafa Cengiz"""))
    playerlist=[]
    for i in range(0,3):
        if(database.bosses.listofbosses[secim11-1]==database.teams.listofteams[i].boss):
            key=i
    for b in range(0,len(database.players.listofplayers)):
        if(database.teams.listofteams[key]==database.players.listofplayers[b].team ):
            playerlist.insert(0,database.players.listofplayers[b])
    hafta=0
    ligsıra=1
    for i in range(0,len(playerlist)):
        print(playerlist[i].name)
    print("Hoş geldiniz sayın ",database.bosses.listofbosses[secim11-1].name," takımınız ", database.teams.listofteams[key].name)
    print("Hafta=",hafta)
    print("Butce= ",database.bosses.listofbosses[secim11-1].money)
    print("Lig Sıralaması= ",ligsıra)
    BaskanOyna.Oynat()
