# first clean input string by building new string that keeps only alphanumeric characters
# then just 2 pointers, one in the beginning, one at the end. iterate towards the middle until right > left
# if the character at the 2 pointers ever is not the same, return false
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first clean string by removing non alphanumeric and spaces
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s = alnum_s + char.lower()

        l = 0
        r = len(alnum_s) - 1

        while r > l:
            if alnum_s[r] is not alnum_s[l]:
                return False

            r -= 1
            l += 1

        return True
        