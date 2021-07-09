import time
import win10toast
import pyautogui
import random


from win10toast import ToastNotifier

toaster = ToastNotifier()
liste = []
fertige_liste = []
einstellungen = []
datei = open('bemerkungen.txt','r')

for zeile in datei:
    liste.append(zeile)

datei.close()

with open('Einstellungen.txt', "r") as einst:
    for zeile in einst:
        einstellungen.append(zeile)
    einst.close()


for element in liste:
    fertige_liste.append(element.strip())

print("Achtung! Fenster nicht schließen, sondern minimieren. Ansonsten wird das Programm gestoppt.")

time.sleep(3)

print('\n\nAber nun: viel Spaß!')

print(fertige_liste)

time.sleep(0.5)

bemerkung = ""

while True:
    bemerkung = random.choice(fertige_liste)
    print('\n\n>    sending Notification: "' + bemerkung + '" ...')
    toaster.show_toast("Bemerkung", bemerkung, icon_path="icon.ico")
    bemerkung = ""
    zeit = int(einstellungen[3])
    print('>    starting timer...')
    while zeit != 0:
        zeit = zeit - 1
        time.sleep(1)
