class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        if len(n)==0:
            return 0
        s=sorted(n)
        m=1
        t=1

        for i in range(1,len(n)):
            if  s[i]!=s[i-1]:
                if abs(s[i]-s[i-1])==1:
                   
                    t+=1
                else:
                    m=max(t,m)
               
                    t=1
        return max(m,t)
