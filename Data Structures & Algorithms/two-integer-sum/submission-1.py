class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        d={}
        for i in range(len(n)):
            if n[i] in d:
                return [d[n[i]] , i]
            else:
                d[t - n[i]]=i
