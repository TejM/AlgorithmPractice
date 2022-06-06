class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letter_dict = {}
        for letter in magazine:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        for letter in ransomNote:
            if letter in letter_dict and letter_dict[letter] > 0:
                letter_dict[letter] -= 1
            else:
                return False
        return True
                
                
        
                    
