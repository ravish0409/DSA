import math
class Solution:

    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l,r=1, max(p)
        re=r
        while l<=r:
            hours=0
            mid=(l+r)//2
            for i in p:
                hours += math.ceil(i / mid)
            if hours<=h:
                re=mid
                r=mid-1
            else:
                l=mid+1
        return re

        




