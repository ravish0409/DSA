class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        count={}
        for i in n:
            count[i]=1+count.get(i,0)
        l=[[] for i in range(len(n)+1)]
        for x,y in count.items():
            l[y].append(x)
        h=[]
        for i in range(len(l)-1,0,-1):
            for y in l[i]:
                h.append(y)
                k-=1
                if k==0:
                    return h
            



            
        