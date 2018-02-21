a = str(input("Enter a word to translate to pig latin "))
vowels = ("a","e","i","o","u","A","E","I","O","U")
for i in range(len(a)):
   if a[i] in vowels:
       print("")
a = a[i:] + a[:i]
print(a + "ay")
