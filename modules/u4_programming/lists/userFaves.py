favourites = []
ratings = []
quit = input("do you want to quit? y/n ")
while quit == "n":
    movies = input("what is one of your favortie movies? ")
    rating = input("how would you rate this movie out of 10? ")
    favourites.append(movies + " " + (rating + "/10"))
    ratings.append(rating + "/10")
    quit = input("do you want to quit? y/n ")
print("Thank you you added " + str(len(favourites)) + " movies")
print("Here are your movies: " + str(favourites))
##print("Here are your movies ratings: " + str(ratings))

a = 0

while a < len(favourites):
    print(favourites[a])
    a = a + 1



