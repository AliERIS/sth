import database
import BaskanMenu
import random

def event1():
    c=random.randrange(0,100)
    d=random.randrange(0,34)
    print("Oyuncunuz",BaskanMenu.playerlist[c%len(BaskanMenu.playerlist)].name,"antremanda sakatlandı",d," hafta sahalardan uzak kalacak")
def event2():
    print("event2")
def event3():
    print("event3")
def event4():
    print("event4")
def event5():
    print("event5")
def event6():
    print("event6")
def event7():
    print("event7")
def event8():
    print("event8")
def event9():
    print("event9")
def event10():
    print("event10")
def event11():
    print("event11")
def event12():
    print("event12")
def event13():
    print("event13")
def event14():
    print("event14")
def event15():
    print("event15")
def event16():
    print("event16")
def event17():
    print("event17")
def event18():
    print("event18")
def event19():
    print("event19")
def event20():
    print("event20")

def randomevent():
    a=random.randrange(0,100)
    if(a>80):
        b=random.randrange(0,20)
        if(b==0):
            event1()
        elif(b==1):
            event2()
        elif(b==2):
            event3()
        elif(b==3):
            event4()
        elif(b==4):
            event5()
        elif(b==5):
            event6()
        elif(b==6):
            event7()
        elif(b==7):
            event8()
        elif(b==8):
            event9()
        elif(b==9):
            event10()
        elif(b==10):
            event11()
        elif(b==11):
            event12()
        elif(b==12):
            event13()
        elif(b==13):
            event14()
        elif(b==14):
            event15()
        elif(b==15):
            event16()
        elif(b==16):
            event17()
        elif(b==17):
            event18():
        elif(b==18):
            event19():
        elif(b==19):
            event20():
        else:
            print("event error")
