class Solution:
    def search(self, n: List[int], t: int) -> int:
        
        l=0
        r=len(n)-1
        while l<=r:
            mid=(l+r)//2
            if n[mid]==t:
                return mid
            elif n[mid]<t:
                l=mid+1
            else:
                r=mid-1
        return -1

                