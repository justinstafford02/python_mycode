#!/usr/bin/env python3

round = 0

while True: 
    round += 1
    print('Finish the movie title, "Monty Python\'s: The Life of ------"')
    answer = input("Your guess--->\n  ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")




