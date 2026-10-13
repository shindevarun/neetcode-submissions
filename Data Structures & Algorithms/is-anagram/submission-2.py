class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq1 = self.frequencyMap(s)
        freq2 = self.frequencyMap(t)
        

        return freq1 == freq2

    def frequencyMap(self, s: str) -> {}:
        freq = dict()

        for char in s:
            if freq.get(char) is None:
                freq.update({char: 1})
            else:
                freq.update({char: freq.get(char) + 1})

        return freq
    

    

