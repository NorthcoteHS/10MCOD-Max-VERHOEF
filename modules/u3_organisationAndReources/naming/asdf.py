"""
Prog:   userInfo.py
Name:   Student Name
Date:   2018/04/18
Desc:   Asks the user for their name, address, etc.
"""

# Display welcome message.
print('Welcome to the User Information Booth! Please enter your info.')

# Get user's name.
firstName = input('First Name: ')
lastName = input('Last Name: ')

# Get user's birth date.
birthdayYear = input('Birth Year: ')
birthdayMonth = input('Birth Month: ')
birthdayDay = input('Birth Day: ')

# Get user's favourites.
colour = input('Favourite colour: ')
song = input('Favourite song: ')
sport = input('Favourite sport: ')

# Display exit message.
print('Thank you, your information has been saved.')
