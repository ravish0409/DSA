class Solution:
    def trap(self, h: list[int]) -> int:
        s=len(h)
        l=0
        r=s-1
        ml=0
        mr=0
        sum=0
        while l<r:
            if ml-h[l]>0:
                sum+=ml-h[l]
            if mr-h[r]>0:
                sum+=mr-h[r]
            ml=max(ml, h[l])
            mr=max(mr,h[r])
            if h[l]>h[r]:
                r-=1
            else:
                l+=1
        return sum