def getUserInputCapitalized(message):
    x = input(message)
    return x.capitalize()



#ls = getUserInputCapitalized('Test 1: ')
#print(as1)

#print(getUserInputCapitalized('Whats your name?'))


def getUserInputData():
    
    a = input('Day: ')
    while int(a) < 1 or int(a) > 31:
         a = input('Day: ')
    b = input('Month: ')
    c = input('Year: ')
    
    return a + '/' + b + '/' + c 

print(getUserInputData())
