ls = [1555, 772, 34, 64, 5, 26, 77, 38, 94, 140]



#Print each item
print(ls)

#Print index of each item
for i in range(len(ls)):
    print(i)

#Print index of each items starting with the last

index = len(ls) - 1
while index >= 0:
    print(index)
    index -= 1

a = len(ls) -1
while a >= 0:
    print(ls[a])
    a -= 2

#Print all items except the last
print(ls[:-1])

#Print all items except the first
print(ls[1:])

#Print all items reversed without using .reverse function
   
b = len(ls) - 1
while b >= 0:
    print(ls[b])
    b -= 1

#Print every other item

a = len(ls) -1
while a >= 0:
    print(ls[a])
    a -= 2


