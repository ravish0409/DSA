class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for i in nums:
            if i in d.keys():
                return True
            else:
                d[i]=1

        return False
        