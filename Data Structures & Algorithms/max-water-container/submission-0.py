class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        m=0
        while l<r:
            if h[l]>h[r]:
                m=max(h[r]*(r-l),m)
                r-=1
            else:
                m=max(h[l]*(r-l),m)
                l+=1
        return m