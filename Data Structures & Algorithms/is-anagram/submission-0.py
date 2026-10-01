class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1=[0 for i in range(26)]
        s2=[0 for i in range(26)]
        for i in range(len(s)):
            s1[ord(s[i])-ord('a')]+=1
            s2[ord(t[i])-ord('a')]+=1

        for i in range(26):
            if s1[i]!=s2[i]:
                return False

        return True
