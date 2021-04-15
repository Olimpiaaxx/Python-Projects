def sumOfNums(num):
    
    previous_num = 0
    
    for i in range(num):
        sumof = i + previous_num
        print('task1: ', sumof)
        previous_num = i

n = 10
sumOfNums(n) 


def evenIndex(s):
    
    for i in range(len(s)):
        if i % 2 == 0:
            print('task2: ', (s[i]))


s = 'pynative'
evenIndex(s)


def cutString(s, n):
    return s[n:]

s = 'pynative'
print('task3: ', cutString(s, 4))


def sameFirstAndLast(ls):
    return ls[0] == ls[-1]

ls = [1, 2, 3, 1]

print('task4: ', sameFirstAndLast(ls))


def divisibleOf(ls):
    for i in range(len(ls)):
        if ls[i] % 5 == 0:
           print('task5: ', ls[i])
    

ls = [10, 20, 33, 46, 55]
#print(divisibleOf(ls))
divisibleOf(ls)


def substringCount(s): # not working 
    counter = 0
    s = s.split()
    if 'Emma' in s:
        counter += 1
    return counter
            



s = "Emma is good developer. Emma is a writer"
print('task6: ', substringCount(s))
#substringCount(s)



def twoLists(ls1, ls2):
    tempLs = []
    for i in range(len(ls1)):
        if ls1[i] % 2 != 0:
            tempLs.append(ls1[i])
    for j in range(len(ls2)):
        if ls2[j] % 2 == 0:
            tempLs.append(ls2[j])
    return tempLs



list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

print('task7: ', twoLists(list1, list2))


def taxable(income):
    if income > 10000:
        firstpercent = 10000 * 0
        income -= 10000
    if income > 10000:
        secondpercent = 10000 * 0.1
        income -= 10000
    if income > 0:
        thirdpercent = income * 0.2
    

    total = firstpercent + secondpercent + thirdpercent

    return total
    

income = 45000
print('task8: ', taxable(income))


    
