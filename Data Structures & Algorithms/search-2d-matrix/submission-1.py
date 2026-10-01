class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        arr=[i[0] for i in matrix]
        where=0
        if matrix[0][0]>t or matrix[-1][-1]<t:
            return False
        l=0
        r=m-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==t:
                return True
            elif arr[mid]<t:
                l=mid+1
            else:
                r=mid-1
        where=l-1
        return self.search(matrix[where],t)

    def search(self, n: List[int], t: int) -> int:
        
        l=0
        r=len(n)-1
        while l<=r:
            mid=(l+r)//2
            if n[mid]==t:
                return True
            elif n[mid]<t:
                l=mid+1
            else:
                r=mid-1
        return False



        
