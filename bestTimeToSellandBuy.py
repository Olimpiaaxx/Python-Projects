class Solution(object):
    def maxProfit2(self, prices):
        maxProfit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        current_profit = 0
        profit_indices = [0, 0]

        for i in range(len(prices) -1):
            if i == len(prices) -1:
                total_profit += current_profit
                current_profit = 0
                profit_indices = [0, 0]
            for j in range(len(prices[i:])):
                jj = j + (i+1)
                if jj > len(prices) -1:
                    #print('here ' + str(jj))
                    break
                if profit_indices[1] < i and profit_indices[1] != 0:
                    total_profit += current_profit
                    current_profit = 0
                    profit_indices = [0, 0]

                if (prices[jj] - prices[i]) >= current_profit:
                    current_profit = prices[jj] - prices[i]
                    profit_indices = [i, jj]
                    #total_profit += current_profit

                if jj != len(prices) -1 and prices[jj + 1] < prices[jj]: #to check if next item in jj is larger than the current jj
                    break
                if prices[i] >= prices[jj]:
                    break
        if current_profit > 0:
            total_profit += current_profit
        return total_profit

#Solution
test_list = [4, 1, 3, 6, 9, 12]
test2 = [7,1,5,3,6,4]
test3 = [1,2,3,4,5]
my_solution = Solution()
print(my_solution.maxProfit2(test_list))
print(my_solution.maxProfit2(test3))
