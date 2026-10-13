class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        # pars_open = set(['{', '[', '('])
        pairs = {'}' : '{', ']' : '[', ')' : '('}

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
                

        return False if stack else True
        