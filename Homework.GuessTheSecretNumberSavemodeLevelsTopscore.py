

import json
import datetime
import random

# Defining the Result class


class Result:
    def __init__(self, name, attempts, date):
        self.name = name
        self.attempts = attempts
        self.date = date

# The game itself


def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    name = input("What's your name player? ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            result = Result(name=name, attempts=attempts, date=str(datetime.datetime.now()))
            with open("score_list.txt", "w") as score_file:
                score_file.write(str(result.__dict__))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
        else:
            print("Your guess is not correct.")


# Get a list of all scores
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_score_list

# Run the game


while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_list in get_top_scores():
            result_obj = Result(attempts=score_list.get("attempts"),
                                name=score_list.get("name", "Anonymous"),
                                date=score_list.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=result_obj.name,
                                                                              attempts=result_obj.attempts,
                                                                              date=result_obj.date))
    else:
        break