import sys
import random
import time
from time import sleep
import colored

# \033[94m blue
# \033[92m green
# \033[93m yellow
# \033[91m red
# function section
#####################################################################################################################
# To color the text
def coloric(sentence, the_word, color_code):
    """
    Returns a colored version of the sentence by replacing the specified word with the given color code.

    Args:
        sentence (str): The input sentence.
        the_word (str): The word to be colored.
        color_code (str): The color code to be applied.

    Returns:
        str: The colored sentence.
    """
    colored_sentence = sentence.replace(the_word, f"{color_code}{the_word}\033[0m")
    return colored_sentence
#typing effect
def type_text(text, delay=0.05):
    """
    Prints the text character by character with a specified delay between each character.

    Args:
        text (str): The text to be printed.
        delay (float): The delay between each character (default: 0.05).
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
#valdiate functions
def choices_check3(des):
    """
    Validates the user's choice from a list of options (a, A, b, B, c, C).

    Args:
        des (str): The user's choice.

    Returns:
        str: The validated choice.
    """
    choices = ["a", "A", "b", "B", "c", "C"]
    while True:
        if des not in choices:
            print(f"Please choose a valid answer. {des} is not valid.")
            des = input("Enter a valid choice: ")
        else:
            print(f"Your choice is {des}")
            return des
def choices_check2(des):
    """
    Validates the user's choice from a list of options (a, A, b, B).

    Args:
        des (str): The user's choice.

    Returns:
        str: The validated choice.
    """
    choices = ["a", "A", "b", "B"]
    while True:
        if des not in choices:
            print(f"Please choose a valid answer. {des} is not valid.")
            des = input("Enter a valid choice: ")
        else:
            print(f"Your choice is {des}")
            return des
def name_checker():
    """
    Asks the user to enter their name and checks if it is valid (no numbers).

    Returns:
        str: The valid name entered by the user.
    """
    while True:
        name = input("Enter your name: ")
        if any(char.isdigit() for char in name):
            print("Invalid name. Name cannot contain numbers.")
        else:
            return name
#poinst inqury
points = 0
def point_indictor(added_points):
    """
    Updates the points variable and prints the updated points indicator.

    Args:
        added_points (int): The points to be added to the current total.

    Global Variables:
        points (int): The total points.
    """
    global points
    points += added_points
    print("=================================================")
    print()
    text_coloric(f"Your points is {points}", text_c="\033[94m")
    print()
    print("=================================================")
#effect with typing effect
def text_coloric(
    text_N1=None, text_N2=None, text_N3=None, text_N4=None, text_c="\033[92m"
):
    """
    Prints colored text using the coloric and type_text functions.

    Args:
        text_N1 (str): The first line of text.
        text_N2 (str): The second line of text.
        text_N3 (str): The third line of text.
        text_N4 (str): The fourth line of text.
        text_c (str): The color code to be applied (default: "\033[92m").
    """
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
#colors gradiant
def text_choices(text_a, text_b, text_c, text_d="", text_e="", text_f=""):
    """
    Prints the text choices with different colors.

    Args:
        text_a (str): Text for choice A.
        text_b (str): Text for choice B.
        text_c (str): Text for choice C.
        text_d (str): Text for choice D (default: "").
        text_e (str): Text for choice E (default: "").
        text_f (str): Text for choice F (default: "").
    """
    print(colored.fg("cyan"), end="")
    print(text_a)
    print(colored.fg("blue"), end="")
    print(text_b)
    print(colored.fg("magenta"), end="")
    print(text_c)
    if text_d:
        print(colored.fg("yellow"), end="")
        print(text_d)
    if text_e:
        print(colored.fg("green"), end="")
        print(text_e)
    if text_f:
        print(colored.fg("red"), end="")
        print(text_f)
    print(colored.attr("reset"), end="")
#play again
def play_again():
    """
    Asks the user if they want to play again and handles their choice.
    """
    lol = input("Do you want to play again (Y/N): ")
    choicesx = ["y", "Y", "n", "N"]
    if lol not in choicesx:
        print(f"Please choose a valid answer. {lol} is not valid.")
        play_again()
    else:
        if lol in ["n", "N"]:
            text_coloric("See you later", text_c="\033[91m")
            sys.exit()
        elif lol in ["Y", "y"]:
            play_game()
#Intro function
def IntroFunction():
    """
    Displays the introductory message and gets the user's name.
    """
    text_coloric("Welcome to Legends of Avaloria", text_c="\033[92m")
    print()
    time.sleep(2)
    name = name_checker()
    print()
    time.sleep(2)
    Intro = f"""Hello {name}! In this game, you are stuck in a mysterious world
and your goal is to find your way back home. Gain more points
and get in the lead in the leaderboard. Your starting points is zero.
Take care and choose the choices wisely.
"""
    type_text(Intro)
    point_indictor(0)
#####################################################################################################################

# The Game Function

#####################################################################################################################


def play_game():
    IntroFunction()
    print()
    print()
    type_text(
        "As you wake up, you find yourself in a dark "
        + "forest with no memory of how you got there."
    )
    print()
    sleep(1)
    type_text("You see three paths in front of you.")
    print()
    sleep(1)

    text_coloric(
        "A) Take the path on the left",
        "B) Take the path in the middle",
        "C) Take the path on the right",
    )
    print()
    sleep(1)

    des_1 = input("Choose your path: ")
    desl_des1 = choices_check3(des_1)

    if desl_des1 in ["a", "A"]:
        type_text("You chose the path on the left.")
        print()
        type_text("As you walk along the path, you come across a river.")
        print()
        sleep(1)
        point_indictor(random.randint(1, 25))

        text_coloric(
            "A) Try to swim across the river",
            "B) Look for a bridge",
            "C) Follow the river to find another way around",
        )
        print()
        sleep(1)

        des_2 = input("What do you want to do next? ")
        desl_des2 = choices_check3(des_2)

        if desl_des2 in ["a", "A"]:
            type_text("You decided to swim across the river.")
            print()
            type_text(
                "Unfortunately, the current was too strong and you got swept away."
            )
            print()
            text_coloric("Game Over!", text_c="\033[91m")
            print()
            play_again()

        elif desl_des2 in ["b", "B"]:
            type_text("You decided to look for a bridge.")
            print()
            point_indictor(random.randint(1, 25))
            type_text(
                "After searching for a while, you find a sturdy "
                + "bridge and cross the river safely."
            )
            print()
            point_indictor(10)
            print()
            text_choices(
                "A) Continue along the path",
                "B) Rest and recover your energy",
                "C) Look for signs of civilization",
            )
            print()
            sc1_des2 = input("What do you want to do next? ")
            desl_sc1_des2 = choices_check3(sc1_des2)
            print()
            if desl_sc1_des2 in ["a", "A"]:
                type_text("You chose to continue along the path.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After walking for a while, you stumble upon a small village."
                )
                print()
                sleep(1)
                text_coloric(
                    "A) Explore the village",
                    "B) Ask the villagers for help",
                    "C) Find a place to rest",
                )
                print()
                sleep(1)

                sc1_ch1_des2 = input("What is your next step: ")
                desl_sc1_ch1_des2 = choices_check3(sc1_ch1_des2)

                if desl_sc1_ch1_des2 in ["a", "A"]:
                    type_text("You decided to explore the village.")
                    print()

                    type_text("As you explore, you discover a hidden treasure chest.")
                    print()
                    sleep(1)
                    point_indictor(20)
                    print()
                    type_text(
                        "Congratulations! You found a treasure chest and gained 20 points!"
                    )
                    print()
                    type_text("Feeling accomplished, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Rest and recover your energy",
                        "C) Ask the villagers for directions",
                    )
                    print()
                    sc1_ch1_des2_ch1 = input("What is your next decision: ")
                    desl_sc1_ch1_des2_ch1 = choices_check3(sc1_ch1_des2_ch1)
                    print()

                    if desl_sc1_ch1_des2_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_sc1_ch1_des2_ch1 in ["b", "B"]:
                        type_text("You decided to rest and recover your energy.")
                        point_indictor(random.randint(1, 25))
                        print()
                        type_text(
                            "After a good night's sleep, you wake up refreshed and ready to continue your journey."
                        )
                        print()
                        text_choices(
                            "A) Follow the road out of the village",
                            "B) Ask the villagers for directions",
                            "",
                        )
                        print()
                        sc1_ch1_des2_ch1_ch1 = input("What is your next decision: ")
                        desl_sc1_ch1_des2_ch1_ch1 = choices_check2(sc1_ch1_des2_ch1_ch1)
                        print()

                        if desl_sc1_ch1_des2_ch1_ch1 in ["a", "A"]:
                            type_text(
                                "You chose to follow the road out of the village."
                            )
                            point_indictor(random.randint(1, 25))
                            print()
                            type_text(
                                "After walking for a while, you see a familiar landmark."
                            )
                            print()
                            type_text("You have found your way back home!")
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                        elif desl_sc1_ch1_des2_ch1_ch1 in ["b", "B"]:
                            type_text(
                                "You decided to ask the villagers for directions."
                            )
                            point_indictor(random.randint(1, 25))
                            print()
                            type_text(
                                "The villagers give you detailed instructions on how to get back home."
                            )
                            print()
                            type_text(
                                "Following their directions, you find your way back home!"
                            )
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()
                elif desl_sc1_ch1_des2 in ["b", "B"]:
                    type_text("You decided to ask the villagers for help.")

                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "The villagers offer their assistance and guide you back home."
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()
                elif desl_sc1_ch1_des2 in ["c", "C"]:
                    type_text("You decided to find a place to rest.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After a good night's sleep, you wake up refreshed and ready to continue your journey."
                    )
                    print()
                    text_choices(
                        "A) Explore the village", "B) Ask the villagers for help", ""
                    )
                    print()
                    sc1_ch1_des2_ch1 = input("What is your next decision: ")
                    desl_sc1_ch1_des2_ch1 = choices_check2(sc1_ch1_des2_ch1)
                    print()
                    if desl_sc1_ch1_des2_ch1 in ["a", "A"]:
                        type_text("You chose to explore the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "As you explore, you discover a hidden treasure chest."
                        )
                        print()
                        sleep(1)
                        point_indictor(20)
                        print()
                        type_text(
                            "Congratulations! You found a treasure chest and gained 20 points!"
                        )
                        print()
                        type_text("Feeling accomplished, you continue your journey.")
                        print()
                        sleep(1)

                        text_choices(
                            "A) Follow the road out of the village",
                            "B) Ask the villagers for directions",
                            ".",
                        )
                        print()
                        sc1_ch1_des2_ch1_ch1 = input("What is your next decision: ")
                        desl_sc1_ch1_des2_ch1_ch1 = choices_check2(sc1_ch1_des2_ch1_ch1)
                        print()

                        if desl_sc1_ch1_des2_ch1_ch1 in ["a", "A"]:
                            type_text(
                                "You chose to follow the road out of the village."
                            )
                            point_indictor(random.randint(1, 25))
                            print()
                            type_text(
                                "After walking for a while, you see a familiar landmark."
                            )
                            print()
                            type_text("You have found your way back home!")
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                        elif desl_sc1_ch1_des2_ch1_ch1 in ["b", "B"]:
                            type_text(
                                "You decided to ask the villagers for directions."
                            )
                            point_indictor(random.randint(1, 25))
                            print()
                            type_text(
                                "The villagers give you detailed instructions on how to get back home."
                            )
                            print()
                            type_text(
                                "Following their directions, you find your way back home!"
                            )
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                    elif sc1_ch1_des2_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for help.")
                        point_indictor(random.randint(1, 25))
                        print()
                        type_text(
                            "The villagers offer their assistance and guide you back home."
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )

                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

            elif desl_sc1_des2 in ["b", "B"]:
                type_text("You decided to rest and recover your energy.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After a good night's sleep, you wake up refreshed and ready to continue your journey."
                )
                print()
                text_choices(
                    "A) Explore the village", "B) Ask the villagers for help", ""
                )
                print()
                sc1_des2_ch1 = input("What is your next decision: ")
                desl_sc1_des2_ch1 = choices_check2(sc1_des2_ch1)
                print()

                if desl_sc1_des2_ch1 in ["a", "A"]:
                    type_text("You chose to explore the village.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("As you explore, you discover a hidden treasure chest.")
                    print()
                    sleep(1)
                    point_indictor(20)
                    print()
                    type_text(
                        "Congratulations! You found a treasure chest and gained 20 points!"
                    )
                    print()
                    type_text("Feeling accomplished, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Ask the villagers for directions",
                        "",
                    )
                    print()
                    sc1_des2_ch1_ch1 = input("What is your next decision: ")
                    desl_sc1_des2_ch1_ch1 = choices_check3(sc1_des2_ch1_ch1)
                    print()

                    if desl_sc1_des2_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_sc1_des2_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for directions.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers give you detailed instructions on how to get back home."
                        )
                        print()
                        type_text(
                            "Following their directions, you find your way back home!"
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                elif desl_sc1_des2_ch1 in ["b", "B"]:
                    type_text("You decided to ask the villagers for help.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "The villagers offer their assistance and guide you back home."
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()

        elif desl_des2 in ["c", "C"]:
            type_text("You decided to follow the river to find another way around.")
            print()
            point_indictor(random.randint(1, 25))
            type_text(
                "As you follow the river, you come across a hidden path "
                + "that leads you out of the forest."
            )
            print()
            point_indictor(10)
            print()
            type_text(
                "Congratulations! You found a way out of the forest and gained 10 points!"
            )
            print()
            sleep(1)

            text_choices(
                "A) Continue your journey",
                "B) Rest and recover your energy",
                "C) Look for signs of civilization",
            )
            print()
            des_2_ch1 = input("What do you want to do next? ")
            desl_des_2_ch1 = choices_check3(des_2_ch1)
            print()

            if desl_des_2_ch1 in ["a", "A"]:
                type_text("You chose to continue your journey.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After walking for a while, you stumble upon a small village."
                )
                print()
                sleep(1)

                text_coloric(
                    "A) Explore the village",
                    "B) Ask the villagers for help",
                    "C) Find a place to rest",
                )
                print()
                sleep(1)

                des_2_ch1_ch1 = input("What is your next step: ")
                desl_des_2_ch1_ch1 = choices_check3(des_2_ch1_ch1)

                if desl_des_2_ch1_ch1 in ["a", "A"]:
                    type_text("You decided to explore the village.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("As you explore, you discover a hidden treasure chest.")
                    print()
                    sleep(1)
                    point_indictor(20)
                    print()
                    type_text(
                        "Congratulations! You found a treasure chest and gained 20 points!"
                    )
                    print()
                    type_text("Feeling accomplished, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Rest and recover your energy",
                        "C) Ask the villagers for directions",
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1_ch1 = choices_check3(des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to rest and recover your energy.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After a good night's sleep, you wake up refreshed and ready "
                            + " to continue your journey."
                        )
                        print()
                        text_choices(
                            "A) Follow the road out of the village",
                            "B) Ask the villagers for directions",
                        )
                        print()
                        des_2_ch1_ch1_ch1_ch1 = input("What is your next decision: ")
                        desl_des_2_ch1_ch1_ch1_ch1 = choices_check2(
                            des_2_ch1_ch1_ch1_ch1
                        )
                        print()

                        if desl_des_2_ch1_ch1_ch1_ch1 in ["a", "A"]:
                            type_text(
                                "You chose to follow the road out of the village."
                            )
                            print()
                            point_indictor(random.randint(1, 25))
                            type_text(
                                "After walking for a while, you see a familiar landmark."
                            )
                            print()
                            type_text("You have found your way back home!")
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                        elif desl_des_2_ch1_ch1_ch1_ch1 in ["b", "B"]:
                            type_text(
                                "You decided to ask the villagers for directions."
                            )
                            print()
                            point_indictor(random.randint(1, 25))
                            type_text(
                                "The villagers give you detailed instructions on how to get back home."
                            )
                            print()
                            type_text(
                                "Following their directions, you find your way back home!"
                            )
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                elif desl_des_2_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to ask the villagers for help.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "The villagers offer their assistance and guide you back home."
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()

                elif desl_des_2_ch1_ch1 in ["c", "C"]:
                    type_text("You decided to find a place to rest.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After a good night's sleep, you wake up refreshed and ready to continue your journey."
                    )
                    print()
                    text_choices(
                        "A) Explore the village", "B) Ask the villagers for help", ""
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1 = choices_check2(des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to explore the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "As you explore, you discover a hidden treasure chest."
                        )
                        print()
                        sleep(1)
                        point_indictor(20)
                        print()
                        type_text(
                            "Congratulations! You found a treasure chest and gained 20 points!"
                        )
                        print()
                        type_text("Feeling accomplished, you continue your journey.")
                        print()
                        sleep(1)

                        text_choices(
                            "A) Follow the road out of the village",
                            "B) Ask the villagers for directions",
                            "",
                        )
                        print()
                        des_2_ch1_ch1_ch1_ch1 = input("What is your next decision: ")
                        desl_des_2_ch1_ch1_ch1_ch1 = choices_check2(
                            des_2_ch1_ch1_ch1_ch1
                        )
                        print()

                        if desl_des_2_ch1_ch1_ch1_ch1 in ["a", "A"]:
                            type_text(
                                "You chose to follow the road out of the village."
                            )
                            print()
                            point_indictor(random.randint(1, 25))
                            type_text(
                                "After walking for a while, you see a familiar landmark."
                            )
                            print()
                            type_text("You have found your way back home!")
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                        elif desl_des_2_ch1_ch1_ch1_ch1 in ["b", "B"]:
                            type_text(
                                "You decided to ask the villagers for directions."
                            )
                            print()
                            point_indictor(random.randint(1, 25))
                            type_text(
                                "The villagers give you detailed instructions on how to get back home."
                            )
                            print()
                            type_text(
                                "Following their directions, you find your way back home!"
                            )
                            print()
                            type_text(
                                "Congratulations! You have successfully completed the game."
                            )
                            print()
                            sleep(1)
                            text_coloric("Game Over!", text_c="\033[92m")
                            print()
                            play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for help.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers offer their assistance and guide you back home."
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

            elif desl_des_2_ch1 in ["b", "B"]:
                type_text("You decided to rest and recover your energy.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After a good night's sleep, you wake up refreshed"
                    + " and ready to continue your journey."
                )
                print()
                text_choices(
                    "A) Explore the village", "B) Ask the villagers for help", ""
                )
                print()
                des_2_ch1_ch1 = input("What is your next decision: ")
                desl_des_2_ch1_ch1 = choices_check2()
                print()

                if desl_des_2_ch1_ch1 in ["a", "A"]:
                    type_text("You chose to explore the village.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("As you explore, you discover a hidden treasure chest.")
                    print()
                    sleep(1)
                    point_indictor(20)
                    print()
                    type_text(
                        "Congratulations! You found a treasure chest and gained 20 points!"
                    )
                    print()
                    type_text("Feeling accomplished, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Ask the villagers for directions",
                        "",
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1_ch1 = choices_check2(desl_des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for directions.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers give you detailed instructions on how to get back home."
                        )
                        print()
                        type_text(
                            "Following their directions, you find your way back home!"
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                elif desl_des_2_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to ask the villagers for help.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "The villagers offer their assistance and guide you back home."
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()
            elif desl_sc1_des2 in ["c", "C"]:
                type_text("You decided to look for signs of civilization.")
                print()
                point_indictor(random.randint(1, 25))
                type_text("As you explore, you come across a small village.")
                print()
                sleep(1)
            text_choices(
                "A) Explore the village",
                "B) Ask the villagers for help",
                "C) Find a place to rest",
            )
            print()
            des_2_ch1 = input("What do you want to do next? ")
            desl_des_2_ch1 = choices_check3(des_2_ch1)
            print()
            if desl_des_2_ch1 in ["a", "A"]:
                type_text("You decided to explore the village.")
                print()
                point_indictor(random.randint(1, 25))
                type_text("As you explore, you discover a hidden treasure chest.")
                print()
                sleep(1)
                point_indictor(20)
                print()
                type_text(
                    "Congratulations! You found a treasure chest and gained 20 points!"
                )
                print()
                type_text("Feeling accomplished, you continue your journey.")
                print()
                sleep(1)

                text_choices(
                    "A) Follow the road out of the village",
                    "B) Rest and recover your energy",
                    "C) Ask the villagers for directions",
                )
                print()
                des_2_ch1_ch1 = input("What is your next decision: ")
                desl_des_2_ch1_ch1 = choices_check3(des_2_ch1_ch1)
                print()

                if desl_des_2_ch1_ch1 in ["a", "A"]:
                    type_text("You chose to follow the road out of the village.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("After walking for a while, you see a familiar landmark.")
                    print()
                    type_text("You have found your way back home!")
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()

                elif desl_des_2_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to rest and recover your energy.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After a good night's sleep, you wake up refreshed and ready "
                        + "to continue your journey."
                    )
                    print()
                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Ask the villagers for directions",
                        "",
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1_ch1 = choices_check2(des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for directions.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers give you detailed instructions on how to get back home."
                        )
                        print()
                        type_text(
                            "Following their directions, you find your way back home!"
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                elif desl_des_2_ch1_ch1 in ["c", "C"]:
                    type_text("You decided to find a place to rest.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After a good night's sleep, you wake up refreshed and ready "
                        + "to continue your journey."
                    )
                    print()
                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Ask the villagers for directions",
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1_ch1 = choices_check2(des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for directions.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers give you detailed instructions on how to get back home."
                        )
                        print()
                        type_text(
                            "Following their directions, you find your way back home!"
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

            elif desl_des_2_ch1 in ["b", "B"]:
                type_text("You decided to ask the villagers for help.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "The villagers offer their assistance and guide you back home."
                )
                print()
                type_text("Congratulations! You have successfully completed the game.")
                print()
                sleep(1)
                text_coloric("Game Over!", text_c="\033[92m")
                print()
                play_again()

            elif desl_des_2_ch1 in ["c", "C"]:
                type_text("You decided to find a place to rest.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After a good night's sleep, you wake up refreshed and ready to continue your journey."
                )
                print()
                text_choices(
                    "A) Explore the village", "B) Ask the villagers for help", ""
                )
                print()
                des_2_ch1_ch1 = input("What is your next decision: ")
                desl_des_2_ch1_ch1 = choices_check2(des_2_ch1_ch1)
                print()

                if desl_des_2_ch1_ch1 in ["a", "A"]:
                    type_text("You chose to explore the village.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("As you explore, you discover a hidden treasure chest.")
                    print()
                    sleep(1)
                    point_indictor(20)
                    print()
                    type_text(
                        "Congratulations! You found a treasure chest and gained 20 points!"
                    )
                    print()
                    type_text("Feeling accomplished, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Follow the road out of the village",
                        "B) Ask the villagers for directions",
                        "",
                    )
                    print()
                    des_2_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_2_ch1_ch1_ch1 = choices_check2(des_2_ch1_ch1_ch1)
                    print()

                    if desl_des_2_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to follow the road out of the village.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After walking for a while, you see a familiar landmark."
                        )
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_2_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to ask the villagers for directions.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "The villagers give you detailed instructions on how to get back home."
                        )
                        print()
                        type_text(
                            "Following their directions, you find your way back home!"
                        )
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()
                elif desl_des_2_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to ask the villagers for help.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "The villagers offer their assistance and guide you back home."
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()

    elif desl_des1 in ["b", "B"]:
        type_text("You decided to take the left path.")
        print()
        point_indictor(random.randint(1, 25))
        type_text(
            "As you continue on the left path, you come across a river blocking your way."
        )
        print()
        text_choices(
            "A) Try to find a way to cross the river",
            "B) Turn back and take the right path",
            "",
        )
        print()
        des_1_ch1 = input("What is your next decision: ")
        desl_des_1_ch1 = choices_check2(des_1_ch1)
        print()

        if desl_des_1_ch1 in ["a", "A"]:
            type_text("You decided to try to find a way to cross the river.")
            print()
            point_indictor(random.randint(1, 25))
            type_text("After searching for a while, you find a sturdy log.")
            print()
            sleep(1)

            text_choices(
                "A) Attempt to cross the river using the log",
                "B) Give up and turn back to take the right path",
                "",
            )
            print()
            des_1_ch1_ch1 = input("What is your next decision: ")
            desl_des_1_ch1_ch1 = choices_check2(des_1_ch1_ch1)
            print()

            if desl_des_1_ch1_ch1 in ["a", "A"]:
                type_text("You chose to attempt to cross the river using the log.")
                print()
                point_indictor(random.randint(1, 25))
                type_text("With careful balance, you manage to cross the river safely.")
                print()
                type_text("Continuing on, you encounter a dense forest.")
                print()
                sleep(1)

                text_choices(
                    "A) Explore the forest", "B) Look for a way out of the forest", ""
                )
                print()
                des_1_ch1_ch1_ch1 = input("What is your next decision: ")
                desl_des_1_ch1_ch1_ch1 = choices_check2(des_1_ch1_ch1_ch1)
                print()

                if desl_des_1_ch1_ch1_ch1 in ["a", "A"]:
                    type_text("You chose to explore the forest.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("As you explore, you stumble upon a hidden treasure.")
                    print()
                    sleep(1)
                    point_indictor(30)
                    print()
                    type_text(
                        "Congratulations! You found a hidden treasure and gained 30 points!"
                    )
                    print()
                    type_text("Feeling excited, you continue your journey.")
                    print()
                    sleep(1)

                    text_choices(
                        "A) Continue through the forest",
                        "B) Look for a way out of the forest",
                        "",
                    )
                    print()
                    des_1_ch1_ch1_ch1_ch1 = input("What is your next decision: ")
                    desl_des_1_ch1_ch1_ch1_ch1 = choices_check2(des_1_ch1_ch1_ch1_ch1)
                    print()

                    if desl_des_1_ch1_ch1_ch1_ch1 in ["a", "A"]:
                        type_text("You chose to continue through the forest.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text("After a while, you see a familiar landmark.")
                        print()
                        type_text("You have found your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                    elif desl_des_1_ch1_ch1_ch1_ch1 in ["b", "B"]:
                        type_text("You decided to look for a way out of the forest.")
                        print()
                        point_indictor(random.randint(1, 25))
                        type_text(
                            "After some time, you find a path that leads you out of the forest."
                        )
                        print()
                        type_text("Following the path, you find your way back home!")
                        print()
                        type_text(
                            "Congratulations! You have successfully completed the game."
                        )
                        print()
                        sleep(1)
                        text_coloric("Game Over!", text_c="\033[92m")
                        print()
                        play_again()

                elif desl_des_1_ch1_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to look for a way out of the forest.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After some time, you find a path that leads you out of the forest."
                    )
                    print()
                    type_text("Following the path, you find your way back home!")
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()

            elif desl_des_1_ch1_ch1 in ["b", "B"]:
                type_text(
                    "You decided to give up and turn back to take the right path."
                )
                print()
                point_indictor(random.randint(1, 25))
                type_text("As you backtrack, you come across a hidden path.")
                print()
                type_text(
                    "Curiosity gets the better of you, and you decide to explore it."
                )
                print()
                sleep(1)

                type_text("You encounter various challenges along the hidden path.")
                print()
                type_text(
                    "With determination and quick thinking, you overcome each obstacle."
                )
                print()
                type_text("Finally, you reach the end of the hidden path.")
                print()
                type_text("To your surprise, it leads you back home!")
                print()
                type_text("Congratulations! You have successfully completed the game.")
                print()
                sleep(1)
                text_coloric("Game Over!", text_c="\033[92m")
                print()
                play_again()

        elif desl_des_1_ch1 in ["b", "B"]:
            type_text("You decided to turn back and take the right path.")
            print()
            point_indictor(random.randint(1, 25))
            type_text(
                "As you walk along the right path, you notice a glimmering object in the distance."
            )
            print()
            type_text("Curiosity piques your interest, and you decide to investigate.")
            print()
            sleep(1)

            type_text("You find a hidden cave filled with treasures.")
            print()
            type_text("You collect the treasures and gain valuable points.")
            print()
            sleep(1)
            point_indictor(50)
            print()
            type_text("Congratulations! You found a hidden cave and gained 50 points!")
            print()
            type_text("Feeling triumphant, you continue your journey.")
            print()
            sleep(1)

            text_choices(
                "A) Continue on the path", "B) Rest and recover your energy", ""
            )
            print()
            des_1_ch1_ch1 = input("What is your next decision: ")
            desl_des_1_ch1_ch1 = choices_check2(des_1_ch1_ch1)
            print()

            if desl_des_1_ch1_ch1 in ["a", "A"]:
                type_text("You chose to continue on the path.")
                print()
                point_indictor(random.randint(1, 25))
                type_text("After a while, you see a familiar landmark.")
                print()
                type_text("You have found your way back home!")
                print()
                type_text("Congratulations! You have successfully completed the game.")
                print()
                sleep(1)
                text_coloric("Game Over!", text_c="\033[92m")
                print()
                play_again()

            elif desl_des_1_ch1_ch1 in ["b", "B"]:
                type_text("You decided to rest and recover your energy.")
                print()
                point_indictor(random.randint(1, 25))
                type_text(
                    "After a good night's sleep, you wake up refreshed and ready "
                    + "to continue your journey."
                )
                print()
                text_choices(
                    "A) Continue on the path", "B) Look for a shortcut back home", ""
                )
                print()
                des_1_ch1_ch1_ch1 = input("What is your next decision: ")
                desl_des_1_ch1_ch1_ch1 = choices_check2(des_1_ch1_ch1_ch1)
                print()

                if desl_des_1_ch1_ch1_ch1 in ["a", "A"]:
                    type_text("You chose to continue on the path.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text("After a while, you see a familiar landmark.")
                    print()
                    type_text("You have found your way back home!")
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()
                elif desl_des_1_ch1_ch1_ch1 in ["b", "B"]:
                    type_text("You decided to look for a shortcut back home.")
                    print()
                    point_indictor(random.randint(1, 25))
                    type_text(
                        "After exploring for a while, you discover a hidden path."
                    )
                    print()
                    type_text(
                        "Taking the hidden path, you find a quicker route back home!"
                    )
                    print()
                    type_text(
                        "Congratulations! You have successfully completed the game."
                    )
                    print()
                    sleep(1)
                    text_coloric("Game Over!", text_c="\033[92m")
                    print()
                    play_again()
    elif desl_des1 in ["c", "C"]:
        print()
        text_coloric(
            "i am very sorry to say that this part is under developmnt",
            text_c="\033[91m",
        )
        print()
        play_again()


play_game()
