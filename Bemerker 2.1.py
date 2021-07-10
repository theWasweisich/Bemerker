import time #Für den Countdown
import win10toast #Das Modul für Windows Toasts
from win10toast import ToastNotifier #Die Toasts von dem Modul für Windows Toasts
import random #Für die randomisierung

# Vorbereitungen
toaster = ToastNotifier()
liste = []
fertige_liste = []
einstellungen = []
title = ("")
datei = open('bemerkungen.txt','r')

# Auslesen und conventieren der Bemerkungen
for zeile in datei:
    liste.append(zeile)
datei.close()

for element in liste:
    fertige_liste.append(element.strip())

# Einlesen und Auswerten der Einstellungen
with open('Einstellungen.txt', "r") as einst:
    for zeile in einst:
        einstellungen.append(zeile)
    einst.close()
title = str(einstellungen[6].strip())

print("\nAchtung! Fenster nicht schließen, sondern minimieren. Ansonsten wird das Programm gestoppt.\n")
zeit = str(einstellungen[3].strip())
print('Einstellungen: \nZeit: ' + zeit + '\nTitel: ' + title)
time.sleep(3)

print('\n\nAber nun: viel Spaß!')


time.sleep(0.5)

bemerkung = ""

# Eigendliche Schleife
while True:
    bemerkung = random.choice(fertige_liste)
    print('\n\n>    sending Notification: "' + bemerkung + '" ...')
    toaster.show_toast(title, bemerkung, icon_path="icon.ico")
    bemerkung = ""
    zeit = int(einstellungen[3])
    print('>    ' + str(zeit) + ' seconds till next notificatoion...')
    while zeit != 0:
        zeit = zeit - 1
        time.sleep(1)
