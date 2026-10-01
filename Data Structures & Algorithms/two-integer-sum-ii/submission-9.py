class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l,r =0, len(n)-1
        while l<r:
            q=n[l]+n[r]
            if t>q:
                l+=1
            elif t<q:
                r-=1
            else:
                return [l+1,r+1]