#1
a = 2
b = 3
c = a + b
print(c)

#2

x = 'Hello World!'
for i in range(4):
    print(x)

#3
a = 1
b = 2
c = a + b
print(c)

#4
x = 4
y = x + 1
x = 2
print(x, y)

#5
x, y = 2, 6
x, y = y, x +2
print(x, y)

#6
a, b = 2, 3
c, b = a, c + 1
print(a, b, c)


#7
def square(x):
    return x

print(square(5))
print(square( 2 * 5))


#8
x = 1
def f():
    return x
print(x)
print(f())


#9
x = 1
def f():
    x = 2
    return x
print(x)
print(f())
print(x)


#10
x = 1
def f():
    global x  # important to remember: when you want to use a global variable you need to state it in the function
    y = x
    x = 2
    return x + y
print(x)
print(f())
print(x)




#11

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y)


#12
def numberCounter(word):
    count = 0
    for letter in word:
        if letter.isdigit():
            count = count + 1
    return count

print('Your count is: ', numberCounter('gh764449g'))


#13
def trueStatement(msg1, msg2):
    x = input(msg1)
    y = input(msg2)
    return x.casefold() == y.casefold()
        
#print(trueStatement('Type a word: ', 'Type another word: '))
        

#14



#15
x = 4
y = 5
p = x < y or x < z
print(p)


#20
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)


#24

def factorial(n):
    return n*n

print(factorial(4))


#25
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)
    


















