class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerCase = s.lower()
        alphaNumericSet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                           'n','o','p','q','r','s','t','u','v','w','x','y','z',
                           '0','1','2','3','4','5','6','7','8','9'}
        phrase = []
        for char in lowerCase:
            if char in alphaNumericSet:
                phrase.append(char)
        left = 0
        right = len(phrase) - 1
        
        while left <= right:
            if phrase[left] == phrase[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
  # Time Complexity O(N)
  # Space Complexity O(N)
