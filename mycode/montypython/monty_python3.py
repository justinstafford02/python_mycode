#!/usr/bin/python3
""" Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and answer.lower() != "brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian":     # case-insensitive check for the correct answer
        print("Correct!")
    elif answer.lower() == "shrubbery":     # check for the super secret answer
        print("Excellent, you have given the super secret answer!")
        break     # exit the loop after finding the super secret answer
elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

