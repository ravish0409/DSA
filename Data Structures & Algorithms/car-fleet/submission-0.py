class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        d={}
        for i in range(len(p)):
            d[p[i]]=s[i]

        sp=[]
        arr=sorted(d.keys())
        for i in arr:
            sp.append((t-i)/d[i])


        fm=0
        count=0

        while sp:
            cpo=sp.pop()
            if fm<cpo:
                count+=1
                fm=cpo
        return count
                