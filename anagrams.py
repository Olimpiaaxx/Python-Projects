class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)

        if len(s_list) == len(t_list):
            s_list.sort()
            t_list.sort()

        return s_list == t_list

        



# Solution
s = 'anagram'
t = 'nagaras'

my_solution = Solution()

print(my_solution.isAnagram(s, t))
