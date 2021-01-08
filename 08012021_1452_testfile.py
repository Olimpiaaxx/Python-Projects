#30
#def dups(lista):
    #dups_list = []
    ##lista2 = []
   # for item in lista:
  #      if item not in dups_list:
 #           dups_list.append(item)
#
    #
   # print(lista2)
  #  print(dups_list)
 #             
#
#dups([7, 1, 8, 2, 7, 2])



#31
def dups(lista):
    temp_list = []
    dups_list = []
    unique_list = []

    for item in lista:
            if item in temp_list:
                    dups_list.append(item)
            else:
                temp_list.append(item)
                
    for item in lista:
            if item in dups_list:
                    pass
            else:
                unique_list.append(item)
    
    print(dups_list)
    print(unique_list)
    

dups([7, 1, 8, 7, 2, 1, 4, 8])
