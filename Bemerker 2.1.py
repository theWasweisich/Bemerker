import time
import win10toast
from win10toast import ToastNotifier
import pyautogui
import random

toaster = ToastNotifier()
liste = []
fertige_liste = []
einstellungen = []
title = ("")
datei = open('bemerkungen.txt','r')

try:
    for zeile in datei:
        liste.append(zeile)
    datei.close()
except TypeError:
    print("    <<Fehler>> Bitte Bemerkungsdatei überprüfen!")
for element in liste:
    fertige_liste.append(element.strip())

try:
    with open('Einstellungen.txt', "r") as einst:
        for zeile in einst:
            einstellungen.append(zeile)
        einst.close()
except TypeError:
    print("     <<Fehler>> Bitte Überprüfe Einstellungen.txt!")
title = str(einstellungen[6].strip())

print("\nAchtung! Fenster nicht schließen, sondern minimieren. Ansonsten wird das Programm gestoppt.\n")
zeit = str(einstellungen[3].strip())
print('Einstellungen: \nZeit: ' + zeit + '\nTitel: ' + title)
time.sleep(3)

print('\n\nAber nun: viel Spaß!')


time.sleep(0.5)

bemerkung = ""

while True:
    bemerkung = random.choice(fertige_liste)
    print(type(bemerkung))
    print('\n\n>    verschicke Bemerkung: "' + bemerkung + '" ...')
    toaster.show_toast(title, bemerkung, icon_path="icon.ico")
    bemerkung = ""
    zeit = int(einstellungen[3])
    print('>    ' + str(zeit) + ' Sekunden, bis zur nächsten Bemerkung...')
    while zeit != 0:
        zeit = zeit - 1
        time.sleep(1)
