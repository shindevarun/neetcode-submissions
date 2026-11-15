# just do 2 frequency maps for each word and compare them
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = self.freqMap(s)
        tMap = self.freqMap(t)

        return sMap == tMap

    
    def freqMap(self, word):
        freq = {}

        for letter in word:
            if letter in freq:
                freq[letter] = freq[letter] + 1
            else:
                freq[letter] = 0

        return freq
    

    

