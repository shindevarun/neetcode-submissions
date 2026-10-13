class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_new = ''.join(char for char in s if char.isalnum()) # remove all non alphanumeric chars
        # s_new = s_new.lower() # make all chars lower case

        # left = 0
        # right = len(s_new) - 1

        # while right > left:
        #     if s_new[left] != s_new[right]:
        #         return False

        #     left += 1
        #     right -= 1
        

        
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s = alnum_s + char.lower()

        print(alnum_s)

        l = 0
        r = len(alnum_s) - 1

        while r > l:
            if alnum_s[r] is not alnum_s[l]:
                print(alnum_s[r], alnum_s[l])
                return False

            r -= 1
            l += 1
        return True
        