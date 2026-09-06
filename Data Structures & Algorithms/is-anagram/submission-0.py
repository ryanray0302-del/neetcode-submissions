class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1freq = {}
        word2freq = {}
        for char in s:
            word1freq[char] = word1freq.get(char , 0) + 1 
        for char in t:
            word2freq[char] = word2freq.get(char , 0 ) + 1 
        
        if word1freq == word2freq:
            return True 
        else:
            return False 
        