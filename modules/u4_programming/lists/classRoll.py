import random

roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
print("guinea pig: " + roll[2])
enrolment = len(roll)
roll.append('James')
del roll[2]
roll[4] = 'Mike'
leno = len(roll) - 1


num = random.randint(0, leno) ##challenge Print the name of a random student in the class.

print("random student: " + roll[num])
print("number of students: " + str(enrolment))

list.reverse(roll)
print("revesed list: " + str(roll))

list.sort(roll)
print("sorted list: " + str(roll))

roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']

list1 = []
list2 = []

list1.append(roll[0])
list1.append(roll[1])
list1.append(roll[2])
list1.append(roll[3])
list1.append(roll[4])
list2.append(roll[5])
list2.append(roll[6])
list2.append(roll[7])
list2.append(roll[8])
list2.append(roll[9])

print("first half: " + str(list1))
print("second half: " + str(list2))

