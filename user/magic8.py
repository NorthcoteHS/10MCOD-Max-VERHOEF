import random

n = 1

while n > 0:
    Responses = ("It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful")
    a = input("Enter a Question to get an answer from the magic 8 ball ")
    print(random.choice(Responses))
    b = input("Do you want to ask another question? (yes or no) ")
    if b == ("yes"):
        n = 1
    if b == ("no"):
        n = 0
