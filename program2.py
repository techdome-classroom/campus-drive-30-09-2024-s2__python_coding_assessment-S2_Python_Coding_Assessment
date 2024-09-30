class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        i = 0

        while i < len(s):
            cur = sym[s[i]]
            next = sym[s[i + 1]] if i + 1 < len(s) else 0

            if cur < next:
                result += next - cur
                i += 2
            else:
                result += cur
                i += 1

        return result
solution = Solution()
print(solution.romanToInt("III"))   # Output: 3
print(solution.romanToInt("IV"))    # Output: 4
print(solution.romanToInt("IX"))    # Output: 9
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994