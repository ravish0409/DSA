class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        for i in range(len(n)):
            r=t-n[i]
            for j in range(i+1,len(n)):
                if n[j]==r:
                    return [i,j]

        