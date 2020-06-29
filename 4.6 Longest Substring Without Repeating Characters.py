#link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        start=0
        end=0
        n=len(s)
        m=0
        while end <n:
            if s[end] not in st:
                st.add(s[end])
                end+=1
                m=max(m,end-start)
            else:
                st.remove(s[start])
                start+=1
        return m
