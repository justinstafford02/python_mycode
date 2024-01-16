#!/usr/bin/env python3

user_name = input("What is your name? ")
user_quest = input("What is your quest? ")

while True:
    try: 
        quest_difficulty = int(input("On a scale between 1-10, what is the difficulty of your quest? "))
        if quest_difficulty >= 1 and quest_difficulty <= 10:
            break  # Exit the while loop if valid input.
        else:
            print("Input Error.")
    except ValueError:
        print(f"{user_name}, please enter a number between 1 and 10.")

print(f"Hello {user_name}! You are requesting a level {quest_difficulty} quest in order to: {user_quest}. Good luck!")

