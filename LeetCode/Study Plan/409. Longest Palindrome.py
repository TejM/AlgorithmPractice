class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_num = {}
        for letter in s:
            if letter in dict_num:
                dict_num[letter] += 1
            else:
                dict_num[letter] = 1
        total_sum = 0
        one_flag = 0
        for letter in dict_num:
            if (dict_num[letter] % 2 == 0):
                total_sum += dict_num[letter]
            elif (dict_num[letter] > 1):
                total_sum += dict_num[letter] - 1
            else:
                one_flag = 1
        return total_sum + one_flag
                
