#1
#ls = [3, 4, 6, 5, 1, 2]

def numberSorter(ls):
    ls.sort()
    return ls
#print(numberSorter(ls))



def addToList(lista2, newitem):
    # assumption: lista2 is already sorted
    if lista2 == []:
        lista2.append(newitem)
        return lista2
    # find index
    count = 0
    for item2 in lista2:
        if newitem <= item2:
            break
        count += 1
    lista2.insert(count, newitem)
    
    
            
def listSorter(ls):
    newlist = []
    for item in ls:
        addToList(newlist, item)
    ls = newlist
    return newlist



lista = [6, 3, 5, 1, 4, 2,]

sortedList = listSorter(lista)

print(sortedList)



#2
def wordLength(message):
    x = input(message)
    return(len(x))
    
#print(wordLength('your word: '))


def wordLength(word):
    x = 0
    for i in word:
        x = x + 1
    return x
#print(wordLength('spadaj'))




#3

#def numberCounter(word):
    count = 0
    for letter in word:
        if letter.isdigit():
            count = count + 1
    return count

#print('Your count is: ', numberCounter('gh764449g'))



#4
import random
def randomQuestion(message):
    x = input(message)
    answers = ['yes', 'no']
    if x[-1: ] == '?':
        return random.choice(answers)   
    else:
        return 'Not a question'
        
#print(randomQuestion('Ask me a question: '))




#5

def trueStatement(msg1, msg2):
    x = input(msg1)
    y = input(msg2)
    return x.casefold() == y.casefold()
        
#print(trueStatement('Type a word: ', 'Type another word: '))
        


#6
#for i in range(n):
    #print('/', end='')




#def pyramid(n):
    for i in range(n):
        #for k in range(n-i):
           # print(' ', end='')
        for j in range(i + 1):
           print('/', end='')
        print()
#pyramid(5)







