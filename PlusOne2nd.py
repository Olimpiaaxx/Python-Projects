class Solution:
    def plusOne(self, digits):
        back_number = len(digits) -1
        for i in range(len(digits)):
            #print(digits[back_number - i])
            checker_list = self.incrOne(digits[back_number - i])
            digits[back_number - i] = checker_list[0]
            if checker_list[1] == 0:
                break
            if digits[back_number - i] == digits[0]:
                digits.insert(0, checker_list[1])

            
        return digits
            
            

    def incrOne(self, number):
        ret_list = []
        if number == 9:
            ret_list.append(0)
            ret_list.append(1)
        else:
            ret_list.append(number + 1)
            ret_list.append(0)
        return ret_list


#SOLUTION

lista = [9, 9, 1, 8, 9]

my_solution = Solution()

print(my_solution.plusOne(lista))
