class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        sp=[]
        arr=sorted(zip(p,s))
        for i,j in arr:
            sp.append((t-i)/j)


        fm=0
        count=0

        while sp:
            cpo=sp.pop()
            if fm<cpo:
                count+=1
                fm=cpo
        return count
                