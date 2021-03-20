class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


        last_item = len(digits) -1
        for i in range(len(digits)):
            digits[last_item] += 1
            
            while last_item > 9:
                new_digits = list(map(int, str(digits[last_item])))
                digits.remove(digits[last_item])
                digits += new_digits
            return digits


       # last_item = len(digits) -1
        #next_item = last_item -1
        #for i in range(len(digits)):
         #   digits[last_item] += 1
         #   if digits[last_item] > 9:
        #        new_digits = list(map(int, str(digits[last_item])))
         #       digits.remove(digits[last_item])
        #        digits += new_digits
         #   return digits




                
          # return digits[last_item]



#maybe do another function for the other digits?  [2, 9] = [3, 0]

#Solution

test_list = [9, 9]
9,9

my_solution = Solution()

print(my_solution.plusOne(test_list))


