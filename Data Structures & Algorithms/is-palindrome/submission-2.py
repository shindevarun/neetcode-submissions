class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(char for char in s if char.isalnum())
        s_new = s_new.lower()

        left = 0
        right = len(s_new) - 1

        while right > left:
            if s_new[left] != s_new[right]:
                return False

            left += 1
            right -= 1
        
        return True
        