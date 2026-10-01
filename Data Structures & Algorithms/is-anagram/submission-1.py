class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}

        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in a:
                a[i]-=1
                if a[i]<0:
                    return False
            else:
                return False
        if sum(a.values())==0:
            return True
        else: 
            return False
 

        