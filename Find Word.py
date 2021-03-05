def find_word(word, string):
    word = list(word)
    string = list(string)

    for item in word:
        if item in string:
            continue
        else:
            return False
    return True


def find_word_once(word, string):
    word = list(word)
    string = list(string)

    for item in word:
        if item in string:
            string.remove(item)
            continue
        else:
            return False
    return True


def find_word_from_list(ls, string):
    for i in range(len(ls)):
        if find_word_once(ls[i], string):
            return ls[i]
    return 'Not Found!'
    


# Create a function that will return true or false if the word
# can be made up of the letters in the string

# Create a function that will return true or false if the word
# can be made up of the letters but you can only use each letter once

# Create a function that will take a list of words and return first word
# in the list that can be made up of these letters

#word1 = 'catcat'
#word2 = 'piepie'

words = ['catcat', 'bird', 'baby', 'slonce', 'piesek']

string1 = 'asdopdieracbayat'  # True for cat, False for pie
string2 = 'tbacieptacpeidry'      # True for act, True for pie
string3 = 'caerpsdfseapiip'      # False for cat, False for pie
string4 = 'petiabbyctaciopeact'    # True for cat, True for pie
string5 = 'kot'         # False for cat, False for pie
string6 = 'ppiieeskottaccat'  # True for cat, True for pie


print('str1: ', find_word_from_list(words, string1))
print('str2: ', find_word_from_list(words, string2))
print('str3: ', find_word_from_list(words, string3))
print('str4: ', find_word_from_list(words, string4))
print('str5: ', find_word_from_list(words, string5))
print('str6: ', find_word_from_list(words, string6))

#print('cat in string1: ', find_word_once(word1, string1))
#print(' cat in string2: ', find_word_once(word1, string2))
#print(' cat in string3: ', find_word_once(word1, string3))
#print(' cat in string4: ', find_word_once(word1, string4))
#print(' cat in string5: ', find_word_once(word1, string5))
#print(' cat in string6: ', find_word_once(word1, string6))

#print('pie in string1: ', find_word_once(word2, string1))
#print('pie in string2: ', find_word_once(word2, string2))
#print('pie in string3: ', find_word_once(word2, string3))
#print('pie in string4: ', find_word_once(word2, string4))
#print('pie in string5: ', find_word_once(word2, string5))
#print('pie in string6: ', find_word_once(word2, string6))

