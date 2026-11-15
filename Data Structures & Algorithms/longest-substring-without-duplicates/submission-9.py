# sliding window. use hashset to keep track of unique chars in window and o(1) lookup.
# you want to add s[r] to set until you come across duplicate. then you want to keep moving left forward
# and removing that element from set until no duplicates in set. no duplicates in this sense means until
# s[r] no longer in set since this was the duplicate element. 
# everytime you move r forward, you do a new window and check if it's the longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        l = 0
        maxWindow = 0

        for r in range(len(s)):
            while s[r] in uniqueChars:
                uniqueChars.remove(s[l])
                l += 1

            uniqueChars.add(s[r])
            currWindow = r - l + 1
            maxWindow = max(maxWindow, currWindow)

        return maxWindow
            