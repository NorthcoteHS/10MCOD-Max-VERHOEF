"""
Prog:   yesNoProgram.py
Name:   Student Name
Date:   2018/04/18
Desc:   Answers yes or no to any question.
"""

import random

# Ask the user for a question.
question = input('Ask me anything!')

# Check for special input.
if question == 'Quit':
    print('Goodbye.')
if question == 'Hi' or question == 'Hello':
    print("What's up?")

# Answer yes or no randomly.
else:
    num = random.randint(1,2);
    if num == 1:
        print("Yes!")
    if num == 2:
        print("No")
print("done")
