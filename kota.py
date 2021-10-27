import os as system
from time import *

class menu():
    
    def men():
        print("Witaj w moim notatniku!")
        print("[1] Zapisać")
        print("[2] Odczytać")
        odpowiedz = input("Napisz tutaj --->    ")
        zapisywanie

        
    
class kot():
def zapisywanie():
    if menu.odpowiedz == "zapisać":
        print("Okej teraz napisz poniżej co chcesz zapisać i naciśniej później ENTER")
        notatka = input("Napisz tu ---->     ")
        print("Teraz napisz na dole jaką chcesz nazwe pliku")
        nazwa = input("Napisz tutaj ---->   ")
        plik = open(f"{nazwa}.txt", "w")
        plik.write(notatka)
        print("twój plik powinien być zapisany w lokalizacji aplikacji")
        sleep(5)

def odczytywanie():
    if menu.odpowiedz == "odczytać":
        print("Okej potrzebuje kilku danych do tej operacji...")
        print("[1] lokalizacja pliku ")
        lokalizacja = input("Napisz tu --->   ")
        print("[2] Nazwa pliku z rozszerzeniem")
        ppnazwa = input("Napisz tutaj nie użając spacji --->   ")
        kot = open(lokalizacja + ppnazwa, "a")
        with open(lokalizacja + ppnazwa) as f:
            lines = f.readlines()
            print(lines)
            sleep(5)
            print("Chcesaz edytować tą notatke ?")
            edytowanie = input("Napisz tutaj ----> ")
            if edytowanie == "Tak":
                print("Chcesz usunąć całą treść tego pliku?")
                usunięcie = input("Napisz tutaj --->   ")
                if usunięcie == "Tak":
                    koto = open(lokalizacja + ppnazwa, "w")
                    print("Napisz poniżej co chcesz zapisać")
                    zmiana = input("Napisz tutaj --->   ")
                    sleep(2)
                    kot.write(" " + zmiana)
                    print("Plik został zapisany")
                    sleep(10)
                if usunięcie == "Nie":
                    print("Napisz poniżej co chcesz zapisać")
                    zmiana = input("Napisz tutaj --->   ")
                    kot.write(" " + zmiana)
                    print("Plik został zapisany")
                    sleep(10)
            if edytowanie == "Nie":
                print("Okej to teraz podaj mi za ile sekund mam się sam wyłączyć")
                czas = input("Napisz tutaj --->   ")
                print("OK")
                sleep(czas)








