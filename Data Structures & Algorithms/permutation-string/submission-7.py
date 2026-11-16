# slide window on s2. window will be of length s1. first precompute s1 frequency map
# then everytime you fixed size window forward on s2 by 1 index, compute the frequency map for that window
# everytime you compute the frequency map of the window, compare it to s1Freq. if same, permuted subtring is found so return true
# if not found by end, return false
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        for s in range(len(s1)):
            if s1[s] in s1Count:
                s1Count[s1[s]] = s1Count[s1[s]] + 1
            else:
                s1Count[s1[s]] = 1

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            s2Count = {}
            for s in range(l, r+1):
                if s2[s] in s2Count:
                    s2Count[s2[s]] = s2Count[s2[s]] + 1
                else:
                    s2Count[s2[s]] = 1

            if s1Count == s2Count:
                return True

            l+= 1
            r += 1
        return False