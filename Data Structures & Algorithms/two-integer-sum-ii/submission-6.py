class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l=0
        r=1
        while True:
            if r>=len(n):
                l+=1
                r=l+1
            sub=t-n[l]
            if sub==n[r]:
                return [l+1,r+1]
            elif sub>n[r]:
                r+=1
            else:
                l+=1
                r=l+1




