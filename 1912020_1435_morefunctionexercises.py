#1
ls = [3, 4, 6, 5, 1, 2]

def numberSorter(ls):
    ls.sort()
    return ls
#print(numberSorter(ls))


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

#def numberCounter




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
        
print(trueStatement('Type a word: ', 'Type another word: '))
        



