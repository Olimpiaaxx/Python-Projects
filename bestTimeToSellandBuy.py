class Solution(object):
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
                if profit_indices[1] < i:
                    current_profit = 0
                    profit_indices = [0, 0]
                if (prices[jj] - prices[i]) >= current_profit:
                    current_profit = prices[jj] - prices[i]
                    profit_indices = [i, jj]
                    total_profit += current_profit
                    print('this is profit index', profit_indices)
                    print('this is current profit', current_profit)
                    print('This is total profit', total_profit)
                if jj != len(prices) -1 and prices[jj + 1] <= prices[jj]:
                    break
                if i <= jj:
                    break
        return total_profit

#Solution
test_list = [4, 1, 3, 6, 9, 12]
my_solution = Solution()
print(my_solution.maxProfit(test_list))
