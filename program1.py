class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif char == '(':
                stack.append(')')
            elif not stack or stack.pop() != char:
                return False
        return not stack

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.isValid("()[]{}"))      # Output: True
print(solution.isValid("(]"))          # Output: False
print(solution.isValid("({[]})"))      # Output: True
print(solution.isValid("({[})"))       # Output: False
