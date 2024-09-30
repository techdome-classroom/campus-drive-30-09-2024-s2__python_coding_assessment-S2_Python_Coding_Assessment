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


        print(solution.isValid("()[]{}"))  # Output: True

# Test case 2: Invalid case
print(Solution.isValid("(]"))  # Output: False

print(Solution.isValid("()[]{}"))  # Output: True

# Test case 2: Invalid case
print(Solution.isValid("(]"))  # Output: False

# Test case 3: Another valid case
print(Solution.isValid("({[]})"))  # Output: True

# Test case 4: Unmatched opening bracket
print(Solution.isValid("({[})"))  # Output: False










    



  

