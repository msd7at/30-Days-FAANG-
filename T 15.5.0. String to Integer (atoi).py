# link : https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        if str[0] != "+" and str[0] != "-" and not str[0].isdigit():
            return 
        else:
            if str[0] in ["+", "-"]: # first letter is "+" or "+"
                sign = str[0]
                res = self.helper(str[1:])
                return min(res, 2147483647) if sign == "+" else max(0-res, -2147483648)
            else: # first letter is a digit 
                return min(self.helper(str), 2147483647)

    def helper(self, string):
        res = 0
        for s in string:
            if not s.isdigit():
                break
            res = 10 * res + int(s)
        return res
