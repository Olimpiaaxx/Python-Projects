
class Solution(object):
    def reverseString(self, s):
       # s[4]
        #s[3]
        #s[2]
        #s[1]
        #s[0]
        #for i in range(len(s)):
         #   print(s[])


#        for i in range(len(s)):
 #           print((len(s) - 1) - i)


            
        for i in range(len(s)):
            print(s[len(s) - 1 - i])
            if i >= (len(s) - 1 - i):
                break
            

            temp = s[i]
            s[i] = s[len(s) -1 -i]
            s[len(s) - 1 - i] = temp
            
            #print(s)


        
       # for i in range(len(s)):
        #    print(i)


       # for item in reversed(s):
        #    print(item)


        



# Solution
test_list = ['h', 'e',  'l', 'l', 'o']

my_solution = Solution()

my_solution.reverseString(test_list)
print(test_list)
