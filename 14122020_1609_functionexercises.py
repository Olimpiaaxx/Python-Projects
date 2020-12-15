#1
def getUserInputTitle(message):
    x = input(message)
    return x.title()


#2
def getUserInputData():
    
    print('Whats your date of birth?')
    a = input('Day: ')
    while int(a) < 1 or int(a) > 31:
         a = input('Day: ')
    b = input('Month: ')
    c = input('Year: ')
    
    return a + '/' + b + '/' + c 


#3
def addWordToList(word, ls):
    ls.append(word)



def getEmployeeDetails(ls):
    
    addWordToList(getUserInputTitle('Whats your first name?: '), ls)
    addWordToList(getUserInputTitle('Whats your last name?: '), ls)
    addWordToList(getUserInputData(), ls)
    addWordToList(getUserInputTitle('How old are you?: '), ls)
    addWordToList(getUserInputTitle('Whats your post code?: '), ls)
    addWordToList(getUserInputTitle('Where are your from?: '), ls)





#4
def printDetails(ls):
    print('Name: ', ls[0])
    print('Surname: ', ls[1])
    print('Date of Birth: ', ls[2])
    print('Age: ', ls[3])
    print('Post Code: ', ls[4])
    print('Country: ', ls[5])


details = []
employee = []



getEmployeeDetails(details)
printDetails(details)
getEmployeeDetails(employee)
printDetails(employee)









