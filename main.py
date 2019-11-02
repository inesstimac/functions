from functions import *

print("Welcome to Guess The Secret Number.")

while True:
    start = input("A) Play new game, B) See top scores or C) Quit? ")

    if start == "A":
        level = input("Choose a level (easy or hard): ")
        play_game(level=level)

    if start == "B":
        for score_dict in get_top_scores():
            print(score_dict["name"] + " with " + str(score_dict["attempts"]) + " attempt(s)")

    if start == "C":
        break
