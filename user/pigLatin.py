a = str(input("Enter a sentence to translate to pig latin ")).split()
vowels = ("a","e","i","o","u","A","E","I","O","U")
x = 0
b = 9999999
d = 0
e = a[d]
while d < len(a):
    while x < len(vowels):
        c = (e.find(vowels[x]))
        x = x + 1
        if c > -1:
            if b > c:
                b = c
    print(e[b:] + e[0:b] + "ay")
    d = d + 1
    if d < len(a):
        e = a[d]
    x = 0
    b = 9999999
