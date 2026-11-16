# Using frequency maps with a trick: keep track of "have" and "need" variables so everytime frequency map for s is updated, we don't need to check
# the whole map with the whole map of t. Too hard to explain really, watch video
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, countS = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            countS[c] = countS.get(c, 0) + 1

            if c in countT and countS[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        
        if resLen != float("infinity"):
            return s[res[0] : res[1]+1]
        else:
            return ""