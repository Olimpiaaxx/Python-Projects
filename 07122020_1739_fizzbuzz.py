#for i in range(1, 101):
 #   if (i % 3 == 0) and (i % 5 == 0):
  #      print('fizzbuzz')
   # elif i % 3 == 0:
    #    print('fizz')

    #elif i % 5 == 0:
     #   print('buzz')
    #else:
     #   print(i)


for i in range (1, 101):
    toprint = ''
    if i % 3 == 0:
        toprint += 'fizz'
    if i % 5 == 0:
        toprint += 'buzz'
    if toprint:
        print(toprint)
    else:
        print(i)
    
