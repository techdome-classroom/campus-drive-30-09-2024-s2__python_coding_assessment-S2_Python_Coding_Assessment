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


solution = Solution()


