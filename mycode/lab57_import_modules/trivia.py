#!/usr/bin/env python3

import html

def trivia_fun(trivia):
    question = trivia["question"]
    correct = trivia["correct_answer"]
    incorrect1 = trivia["incorrect_answers"][0]
    incorrect2 = trivia["incorrect_answers"][1]
    incorrect3 = trivia["incorrect_answers"][2]

    print(f'Question: {html.unescape(question)}')
    print(f'1: {html.unescape(correct)}')
    print(f'2: {html.unescape(incorrect1)}')
    print(f'3: {html.unescape(incorrect2)}')
    print(f'4: {html.unescape(incorrect3)}\n')

    user_answer = input("Enter your answer (1-4): ")

    if user_answer == '1':
        print("Correct!")
    elif user_answer in ['2', '3', '4']:
        print("Incorrect!")
    else:
        print("Invalid input!")

trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca?",
    "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
    "incorrect_answers": [
        "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
        "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
        "&quot;Round up the usual suspects.&quot;"
    ]
}

trivia_fun(trivia)

