from time import *
import random
import os as system
import webbrowser as web

class dane():
    losowanie = ["Speed up", "Slow down"]
    przywitania = ["Hi", "Hello",]
    nazwa = ["user", "User", "Player"]
    user = random.choice(nazwa)
    przywitanie = random.choice(przywitania)

wirus = 1

def start():
    system.system("color f1")
    print(f"Hi {dane.user}, you have to choice what do u want use:")
    print("------------------------------------------")
    print("[1]  Speed up PC")
    print("[2]  Slow down PC")
    print("[3]  I don't know")
    print("-------------------------------------------")
    wybor = int(input("Write here 1, 2 or 3---->       "))
    if wybor == 1:
        print("Give me 2 seconds for loading")
        sleep(2)
        option1()
    if wybor == 2:
        print("Give me 2 seconds for loading")
        sleep(2)
        option2()
    if wybor == 3:
        print("You don't know what's use? No problem! I will choice")
        print("|||||||||||||||||||||||||||||||")
        los = random.choice(dane.losowanie)
        print(los)
        print("|||||||||||||||||||||||||||||||")
        print("   ")
        sleep(2)
        start()


def option1():
    print("Okej i in your browser loading some page...")
    print("What's processor do u have ?")
    print("[1] Amd")
    print("[2] Intel")
    procesor = int(input("Write here --->   "))
    if procesor == 1:
        web.open("https://www.amd.com/en/technologies/ryzen-master")
        web.open("https://www.razer.com/cortex")
        web.open("https://www.msi.com/Landing/afterburner/graphics-cards")
        print("What's graphic cart do you have ?")
        print("[1] Nvidia")
        print("[2] Amd")
        graphic = int(input("Write here --->     "))
        if graphic == 1:
            web.open("https://www.nvidia.com/pl-pl/geforce/geforce-experience/")
            print("In this aplication you need to download drivers update.")
            print("You have to download this files to speed up ur pc. Be careful, i am not responsible for any damage")
            sleep(10)
        if graphic == 2:
            web.open("https://www.amd.com/en/technologies/radeon-software")
            print("In this aplication you need to download drivers update.")
            print("You have to download this files to speed up ur pc. Be careful, i am not responsible for any damage")
            sleep(10)
    if procesor == 2:
        web.open("https://www.razer.com/cortex")
        web.open("https://www.intel.pl/content/www/pl/pl/gaming/overclocking-intel-processors.html")
        web.open("https://www.msi.com/Landing/afterburner/graphics-cards")
        print("What's graphic cart do you have ?")
        print("[1] Nvidia")
        print("[2] Amd")
        graphic = int(input("Write here --->     "))
        if graphic == 1:
            web.open("https://www.nvidia.com/pl-pl/geforce/geforce-experience/")
            print("In this aplication you need to download drivers update.")
            print("You have to download this files to speed up ur pc. Be careful, i am not responsible for any damage")
            sleep(10)
        if graphic == 2:
            web.open("https://www.amd.com/en/technologies/radeon-software")
            print("In this aplication you need to download drivers update.")
            print("You have to download this files to speed up ur pc. Be careful, i am not responsible for any damage")
            sleep(10)


def option2():
    print("You, want to slow down your Pc? No problem! Give me some time")
    sleep(0.1)
    kot = open("SLow.dll", "w")
    for wirus in range(1, 500000):
        if wirus < 499999:
            kot.write("Pc is now slowed.,,.,.,.,.,.,.,.,.,")
            wirus = wirus + 1
        else:
            print("Okey, this file will slow down your pc, but don't close me i writing importany file")
            web.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            slowdown()


def slowdown():
    slow = open("Run This.bat", "w")
    slow.write("@echo off   ")
    slow.write("\n")
    slow.write(":start")
    slow.write("\n")
    slow.write("start cmd.exe")
    slow.write("\n")
    slow.write("start notepad.exe")
    slow.write("\n")
    slow.write("start notepad.exe")
    slow.write("\n")
    slow.write("start calculator.exe")
    slow.write("\n")
    slow.write("goto :start")
    slow.close()


start()


