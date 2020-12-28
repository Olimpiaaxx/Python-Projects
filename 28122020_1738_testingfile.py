x = 1
def f():
    #global x  # important to remember: when you want to use a global variable you need to state it in the function
    y = x
    #x = 2
    return x + y
print(x)
print(f())
print(x)
