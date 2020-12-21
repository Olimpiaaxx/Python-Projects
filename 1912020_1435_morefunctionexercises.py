#1
#def numberSorter(ls)


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
    if x == '?':
        print(random.choice(answers))
    else:
        print('error')
print(randomQuestion('Ask me a question: '))





