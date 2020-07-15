# link  :   https://leetcode.com/problems/compare-version-numbers/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1, num2 = 0,0
        i,j = 0,0
        n,m = len(version1),len(version2)
        while i < n or j < m:
            while i < n and version1[i] != '.':
                num1 = num1*10+int(version1[i])
                i += 1
            while j < m and version2[j] != '.':
                num2 = num2*10+int(version2[j])
                j += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                i += 1 if i < n else 0
                j += 1 if j < m else 0
                num1, num2 = 0,0
        return 0
