import datetime
import json
import random


def play_game(level):
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()
    wrong_guesses = []
    name = input("Enter your name: ")

    while True:
        guess = int(input("Guess the secret number between 1 and 30: "))
        attempts = attempts + 1

        if guess != secret:
            wrong_guesses.append(guess)

        if guess == secret:
            score_list.append(
                {"name": name, "attempts": attempts, "secret number": secret, "wrong guesses": wrong_guesses,
                 "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("Congratulations, " + name + "! You have guessed correctly, it is number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print("Your wrong guesses were: " + str(wrong_guesses))

            break

        elif guess > secret and level == "easy":
            print("Your guess is not correct. Try something smaller.")
        elif guess < secret and level == "easy":
            print("Your guess is not correct. Try something bigger.")
        elif level == "hard":
            print("Your guess is not correct.")


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_scores = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_scores
