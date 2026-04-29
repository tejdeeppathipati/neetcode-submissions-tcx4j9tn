class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if s[i] == ')':
                    if elem != '(':
                        return False
                elif s[i] == '}':
                    if elem != '{':
                        return False
                else:
                    if elem != '[':
                        return False
        return len(stack) == 0
