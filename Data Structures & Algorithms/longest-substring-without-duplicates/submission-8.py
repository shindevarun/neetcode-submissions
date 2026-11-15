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
            