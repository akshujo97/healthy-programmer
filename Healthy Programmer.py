import datetime
import time

from pygame import mixer
import pygame
s = "C:/Users/Akshay/PycharmProjects/PythonTuts/ss.mp3"

l = 3500

print(min)

def mymix(inp2,s2):
    mixer.init()
    mixer.music.load('ss.mp3')
    mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        inp2 = input("Press S to stop: ")
        if (inp2 == s2):
            mixer.music.stop()

            break
        else:
            continue

def fileopen(str,time_of_schedule):
    with open(n, "a+") as f:
        f.seek(0)
        data = f.read()
        if len(data) >= 0:
            f.write("\n")
            f.write(f"{str} {time_of_schedule}")
            f.close()

if __name__ == '__main__':
    localtime = datetime.datetime.now()
    n = input("Welcome to healthy programmer, please enter your name here: ")
    print(f"Please sit back and relax {n}, we will notify you shortly. Your entry: {localtime}")
    name = f"{n}.txt"
    min = localtime.minute
    init_time = 9
    fin_time = 17
    water_timer = min + 30
    eye_timer = min + 35
    phy_timer = min + 45

    while True:
        localtime = datetime.datetime.now()
        min = localtime.minute
        sec = localtime.second
        hour = localtime.hour

        if localtime.hour>=init_time and localtime.hour<=fin_time:

            """For water"""
            if l == 0:
                print(f"Yayy you fulfilled your goal of 3.5L so congrats!!")
            else:
                if water_timer > 60:
                    water_timer = water_timer - 60
                elif water_timer <= 60:
                    water_timer = water_timer

                if min == water_timer and sec == 0:
                    waterdr = "Drank water on "
                    l -= 218.5
                    print(f"Drink Water: {l} liters left")
                    fileopen(waterdr, localtime)
                    inp1 = "S"
                    mymix(inp1, "S")
                    time.sleep(2)
                    min = localtime.minute
                    water_timer = min + 30

            """For eyes"""
            if eye_timer > 60:
                eye_timer = eye_timer - 60
            elif eye_timer <= 60:
                eye_timer = eye_timer

            if min == eye_timer and sec == 0:
                eyeex = f"Eye exercise on "
                print("Eye Exercise")
                fileopen(eyeex,localtime)
                inp1 = "S"
                mymix(inp1, "S")
                min = localtime.minute
                eye_timer = min + 35

            """For physical"""
            if phy_timer > 60:
                phy_timer = phy_timer - 60
            elif phy_timer <= 60:
                phy_timer = phy_timer

            if min == phy_timer and sec == 0:
                phyex = "Did Physical exercise on "
                print("Physical Exercise")
                fileopen(phyex, localtime)
                inp1 = "S"
                mymix(inp1, "S")
                min = localtime.minute
                phy_timer = min + 45

            """Collision"""
            if water_timer == eye_timer:
                water_eyes = "Drank water and did eye exercise on "
                print("First drink water then do eye exercises.")

                inp1 = "S"
                mymix(inp1, "S")
                fileopen(water_eyes, localtime)
                water_timer = min + 30
                eye_timer = min + 35
            elif eye_timer == phy_timer:
                eye_physical = "Did eye and phycal exercise on "
                print("Please do eye and physical exercise")
                fileopen(eye_physical, localtime)
                inp1 = "S"
                mymix(inp1, "S")
                phy_timer = min + 45
                eye_timer = min + 35
            elif water_timer == phy_timer:
                water_physical = "Drank water and did physical exercise on "
                print("Please drink water and do physical exercise")
                fileopen(water_physical, localtime)
                inp1 = "S"
                mymix(inp1, "S")
                water_timer = min + 30
                phy_timer = min + 45
            else:
                pass

        else:
            continue







