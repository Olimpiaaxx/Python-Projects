class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


        last_item = len(digits) -1
        for i in range(len(digits)):
            digits[last_item] += 1
            print(digits[last_item])
            if digits[last_item] > 9:
                new_digits = list(map(int, str(digits[last_item])))
                digits.remove(digits[last_item])
                digits += new_digits
                #digits.remove(digits[last_item -2])
                #digits[last_item -2] += 1
            return digits




                
          # return digits[last_item]


            
          #  if digits[-1] > 9:
           #     arr = str(digits[-1])
            #    digits.remove(digits[-1])
             #   arr = list(arr)
              #  digits += arr
           # return digits

#maybe do another function for the other digits?  [2, 9] = [3, 0]

#Solution

test_list = [2, 9, 9]
9,9

my_solution = Solution()

print(my_solution.plusOne(test_list))


