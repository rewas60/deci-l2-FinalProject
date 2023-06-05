import sys
import random
import time
from time import sleep
import colored

#\033[94m blue
#\033[92m green
#\033[93m yellow
#\033[91m red

#function to change th color of the text
def coloric(sentence, the_word, color_code):
    colored_sentence = sentence.replace(the_word, f"{color_code}{the_word}\033[0m")
    return colored_sentence

#delay function
def type_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

#choice checker function
def choices_check4(des):
    choices = ["a", "A", "b", "B", "c", "C", "d", "D"]
    if des not in choices:
        print(f"Please choose a valid answer. {des} is not valid.")
        des_1 = input("Enter a valid choice: ")
        print(f"Your choice is {des}")

#check 3 choices
def choices_check3(des):
    choices = ["a", "A", "b", "B", "c", "C"]
    if des not in choices:
        print(f"Please choose a valid answer. {des} is not valid.")
        des_1 = input("Enter a valid choice: ")
    print(f"Your choice is {des}")

def choices_check2(des):
    choices = ["a", "A", "b", "B"]
    if des not in choices:
        print(f"Please choose a valid answer. {des} is not valid.")
        des_1 = input("Enter a valid choice: ")
    print(f"Your choice is {des}")

points = 0

#point indictour function
def point_indictor(added_points):
    global points
    points += added_points 
    print(f"your points is {points}")

#a compination of type text and coloric
def text_coloric(text_N1=None, text_N2=None, text_N3=None, text_N4=None, text_c="\033[92m"):
    colored_text_N1 = coloric(text_N1, text_N1, text_c) if text_N1 else None
    colored_text_N2 = coloric(text_N2, text_N2, text_c) if text_N2 else None
    colored_text_N3 = coloric(text_N3, text_N3, text_c) if text_N3 else None
    colored_text_N4 = coloric(text_N4, text_N4, text_c) if text_N4 else None

    if colored_text_N1:
        type_text(colored_text_N1)
        print()
    if colored_text_N2:
        type_text(colored_text_N2)
        print()
    if colored_text_N3:
        type_text(colored_text_N3)
        print()
    if colored_text_N4:
        type_text(colored_text_N4)
        print()


#repeat function
def repeat(par1=None, par2=None, par3=None, par4=None,repeats_time=1):
    if par2 is None and par3 is None and par4 is None:
        for i in range(repeats_time):
            type_text(par1)
            print()
    elif par3 is None and par4 is None:
        type_text(par1)
        print()
        time.sleep(1)
        type_text(par2)
        print()
    elif par4 is None:
        type_text(par1)
        print()
        time.sleep(1)
        type_text(par2)
        print()
        time.sleep(1)
        type_text(par3)
        print()
    else:
        type_text(par1)
        print()
        time.sleep(1)
        type_text(par2)
        print()
        time.sleep(1)
        type_text(par3)
        print()
        time.sleep(1)
        type_text(par4)
        print()

Pl_Name = input("Enter your name : ")
Pl_Nameic = coloric(Pl_Name,Pl_Name,"\033[92m")
intro_text = f"""Hello {Pl_Nameic} in Chronicles of the Galactic Undead: Year 3020
In this game, you are the only human on Earth and you have been attacked
by a bunch of eveil robots. Your goal is to achieve 300 Points
to buy a spaceship from the lab and reunite with your family on the Revenia planet.
You can buy weapons and your points start at zero."""

type_text(intro_text)

your_points=f"your points is {points}"

type_text(your_points)

introx = "you are at your home and you need to make a step to forword to buy the space ship " 
sc1 = coloric("A)go and find resources to make weapons to beat the robos","A)go and find resources to make weapons to beat the robos","\033[92m")
sc2 = coloric("B)go and find resources to make spaceship","B)go and find resources to make spaceship","\033[92m")
sc3 = coloric("C)stay at home and the robots won't find you","C)stay at home and the robots won't find you","\033[92m")
sc4 = coloric("D)find some friends or some people and collobrate to buy spaceship","D)find some friends or some people and collobrate to buy spaceship","\033[92m")
type_text(introx)
print()
text_coloric(sc1,sc2,sc3,sc4)
print()

time.sleep(3)
des_1 = input("your choice is : ")
time.sleep(2)
choices_check4(des_1)

print()

if des_1 in ["a","A"]:
    type_text("now you have to make step and move forwaord to get back to your family again make a good decion that may help you")
    print()
    text_coloric("A)go to forest and find some resources","B)go to down town and search for weapons","C)climb the tree and pick up some leaves")
    print()
    sc1_des1 = input("choose your next step : ")
    choices_check3(sc1_des1)
    if sc1_des1 in ["a","A"]:
        print("your choice is go to forest and find some resources")
        print()
        text_coloric("A)pick up some sticks","B)ignore the sticks","C)climb the tree and pick up some leaves")
        print()
        sc1_ch1_des1 = input("what is your next step : ")
        choices_check3(sc1_ch1_des1)
        if sc1_ch1_des1 in ["a","A"]:
            print("your choice is pick up some sticks")
            point_indictor(10)
            print()
            print()
            repeat("A)pick up a rock from floor and make pickaxe","B)ignore this rock","C)return home")
            print()
            sc1_ch1_des1_ch1 = input("what is your next dection : ")
            if sc1_ch1_des1_ch1 in ["a","A"]:
                print("you chose to pick up a rock from floor and make pickaxe")
                point_indictor(10)
                print()
                print()
                type_text("now it is raining heavy so you have many choices and thing to do during the rain")
                print()
                print()
                text_coloric("A)return home","B)go to cave and mine it searching for resources until it stop raining")
                sc1_ch1_des1_ch1_des = input("make a step forward : ")
                print()
                choices_check2(sc1_ch1_des1_ch1_des)
                print()
                if sc1_ch1_des1_ch1_des in ["A","a"]:
                    type_text("your descion is to return home")
                    print()
                    type_text("while you are rturning to your home you found some robots")
                    print()
                    print()
                    text_coloric("A)walk like a robot so they wont hurt you","B)try to ignore the and hide from them","C)try to know if they an eveil robots or good ","D)fight them")
                    print()
                    sc1_ch1_des1_ch1_des_des = input("be strong and choose with withem : ")
                    choices_check4(sc1_ch1_des1_ch1_des_des)
                    print()
                    if sc1_ch1_des1_ch1_des_des in ["a","A"]:
                        type_text("your choice is walking like a robot so they wont hurt you")
                        print()
                        text_coloric("unfortunetly they found you and you loosed",text_c="\033[91m")
                        sys.exit
                    elif sc1_ch1_des1_ch1_des_des in ["b","B"]:
                        print()
                        type_text("your choice is try to ignore the and hide from them")
                        print()
                        next_scenario1 = random.choice(["you crossed safely","they detected you "])
                        print()
                        if next_scenario1 == "they detected you ":
                            type_text(next_scenario1)
                            print()
                            text_coloric("unfortunetly they found you and you loosed",text_c="\033[91m")
                            sys.exit
                        elif next_scenario1 == "you crossed safely":
                            print()
                            text_coloric(next_scenario1)
                            print()
                    elif sc1_ch1_des1_ch1_des_des in ["c","C"]:
                        print()
                        type_text("your choice is trying to know if they an eveil robots or good")
                        print()
                    elif sc1_ch1_des1_ch1_des_des in ["d","D"]:
                        print()
                        type_text(coloric("your choice is fightin them but surley the stronger  than you and they killed you","they killed you","\033[91m"))
                        print()
                        sys.exit
                elif sc1_ch1_des1_ch1_des in ["B","b"]:
                    type_text("your choice is going to cave and mine it searching for resources until it stop raining")
            elif sc1_ch1_des1_ch1 in ["b","B"]:
                print("you chose to ignore this rock")
                point_indictor(0)
                print()
                print("now it is raining heavy you must make a important to choice about raining")
                print()
                print()
                text_coloric("A) go to the cave until the morning or the rain finishes","B) continue your trip and water won't do any thing to you","C) see a tree and waint behind it until the rain finishes")
            elif sc1_ch1_des1_ch1 in ["c","C"]:
                print("you chose to return home")
                point_indictor(-5)
        elif sc1_ch1_des1 in ["b","B"]:
            print("your choice is  to ignore the sticks ")
            point_indictor(0)
            print()
            text_coloric("A)pick up a rock from floor it may help you","B)ignore this rock","C)return home")
            print()
            sc1_ch1_des1_ch2 = input("your next step is important so take care when you choose it : ")
            choices_check3(sc1_ch1_des1_ch2)
        elif sc1_ch1_des1 in ["c","C"]:
            type_text("your choice is climb the tree and pick up some leaves")
            print()
            next_scenario= random.choice(["you unfortunetly fall and dead","you sucessed and to climb and bring the leaves"])
            if next_scenario == "you unfortunetly fall and dead":
                type_text(next_scenario)
                type_text("you unfortunetly fall and dead")
                print()
                type_text("game finished , you lossed")
                print()
                sys.exit
            elif next_scenario == "you sucessed and to climb and bring the leaves":
                type_text(next_scenario)
                print()
            point_indictor(5)
    elif sc1_des1 in ["b","B"]:
        print("your choice is go to down town and search for weapons")
    elif sc1_des1 in ["C","c"]:
        print("your choice is search in your home")
elif des_1 in ["b","B"]:
    print(sc2)
elif des_1 in ["c","C"]:
    print(sc3)
elif des_1 in ["d","D"]:
    print(sc4)
