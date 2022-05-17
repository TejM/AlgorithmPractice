class Solution(object):
    def isAnagram(self, s, t):
        letter_dict = {}
        if len(s) != len(t):
            return False
        for letter in t:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
        for letter in s:
            if letter not in letter_dict:
                return False
            else:
                letter_dict[letter] -= 1
                if letter_dict[letter] < 0:
                    return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
