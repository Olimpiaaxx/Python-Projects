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
























