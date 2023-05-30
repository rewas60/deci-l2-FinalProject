import time
from time import sleep
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
points = 0
#point indictour function
def point_indictor(added_points):
    global points
    points += added_points 
    print(f"your pints is {points}")
Pl_Name = input("Enter your name : ")
intro_text = f"""Hello {Pl_Name} in Chronicles of the Galactic Undead: Year 3020
In this game, you are the only human on Earth and you have been attacked
by a bunch of eveil robots. Your goal is to achieve 300 Points
to buy a spaceship from the lab and reunite with your family on the Revenia planet.
You can buy weapons and your points start at zero."""
type_text(intro_text)
your_points=f"your points is {points}"
type_text(your_points)
introx = "you are at your home and you need to make a step to forword to buy the space ship " 
sc1 = "A)go and find resources to make weapons to beat the robos"
sc2 = "B)go and find resources to make spaceship"
sc3 = "C)stay at home and the robots won't find you"
sc4 = "D)find some friends or some people and collobrate to buy spaceship"
type_text(introx)
print()
time.sleep(2)
type_text(sc1)
print()
time.sleep(1)
type_text(sc2)
print()
time.sleep(1)
type_text(sc3)
print()
time.sleep(1)
type_text(sc4)
print()
time.sleep(3)
des_1 = input("your choice is : ")
time.sleep(2)
choices_check4(des_1)
sc1_ch1 = "A)go to forest and find some resources"
sc1_ch2 = "B)go to down town and search for weapons"
sc1_ch3 = "C)search in your home"

sc1_ch1_ch1 = "pick up some sticks"
sc1_ch1_ch2 = "ignore the sticks"
sc1_ch1_ch3 = "climb the tree and pick up some leaves"
print()
if des_1 in ["a","A"]:
    print(sc1)
    type_text(sc1_ch1)
    print()
    time.sleep(1)
    type_text(sc1_ch2)
    print()
    time.sleep(1)
    type_text(sc1_ch3)
    print()
    time.sleep(1)
    print()
    sc1_des1 = input("choose your next step : ")
    choices_check3(sc1_des1)
    if sc1_des1 in ["a","A"]:
        print("your choice is go to forest and find some resources")
        print()
        type_text(sc1_ch1_ch1)
        print()
        time.sleep(1)
        type_text(sc1_ch1_ch2)
        print()
        time.sleep(1)
        type_text(sc1_ch1_ch3)
        print()
        time.sleep(1)
        print()
        sc1_ch1_des1 = input("what is your next step : ")
        choices_check3(sc1_ch1_des1)
        if sc1_ch1_des1 in ["a","A"]:
            print("your choice is pick up some sticks")
            point_indictor(10)
        elif sc1_ch1_des1 in ["b","B"]:
            print("your choice is  to ignore the sticks ")
            point_indictor(0)
        elif sc1_ch1_des1 in ["c","C"]:
            print("your choice is climb the tree and pick up some leaves")
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