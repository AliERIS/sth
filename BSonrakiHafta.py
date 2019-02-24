import database
import BaskanMenu
import BaskanMatch
import BaskanRandomEvent
def SonrakiHafta():
    BaskanMenu.hafta=BaskanMenu.hafta+1
    BaskanMatch.match()
    BaskanRandomEvent.randomevent()
