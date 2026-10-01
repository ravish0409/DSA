class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(s)):
            t="".join(sorted(s[i]))
            if t in d:
                d[t].append(s[i])
            else:
                
                d[t]=[s[i]]
        r=[]
        for i in d:
            r.append(d[i])
        return r
