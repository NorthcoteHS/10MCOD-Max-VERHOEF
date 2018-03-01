letters = input("Enter a sentence to encrypt ")
offset = int(input("What do you want your offset to be? "))

for letter in letters:
    a = letter.isupper()
    number = ord(letter) + (offset)
    if a == True:
        if number > 90:
            number = number - 28 + (offset)
    if a == False:    
        if number > 122:
            number = number - 28 + (offset)
    print (chr(number))
