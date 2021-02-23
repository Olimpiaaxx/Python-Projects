import re

my_list = ['Sylan', 'Sylan', 'Olimpia', 'Olaf', 'Magda', 'olek']
new_dict = {}
new_list = []

for item in my_list:
    ##check for any special charactrs
    #if any(c in my_list[0] for c in item[0]):
    #    print("yes")
   # else:
   #     print("no")

    char = item[0]
    char = char.lower()

    if char not in new_dict:
        new_dict.update({char : 1})
    else:
        new_dict[char] += 1
#for item in new_dict:
#    if new_dict[item[0]] > 1:
#        new_list.append(item[0])

print(new_dict)
