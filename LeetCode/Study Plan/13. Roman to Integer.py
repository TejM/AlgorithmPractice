class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        look_ahead_letters = {'I' : ['V', 'X', 1], 'X' : ['L', 'C', 10], 'C' : ['D', 'M', 100]}
        
        num = 0
        for x in range(len(s)-1):
            letter = s[x]
            next_letter = s[x+1]
            if letter in look_ahead_letters and next_letter in look_ahead_letters[letter]:
                num -= look_ahead_letters[letter][-1]
            else:
                num += roman_dict[letter]
        num += roman_dict[s[-1]]
        return num
