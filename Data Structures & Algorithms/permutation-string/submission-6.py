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