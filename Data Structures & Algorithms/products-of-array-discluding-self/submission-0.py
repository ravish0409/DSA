class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        f=[n[0]]
        l=len(n)
        b=[n[-1]]

        for i in range(l-1):
            f.append(f[i]*n[i+1])

        for i in range(-1,-l,-1):
            b=[b[i]*n[i-1]]+b

        r=[]
        for i in range(l):
            if n[i]!=0:
                r.append((b[i]//n[i])*(f[i]//n[i]))
            else:
                if i >0 and i<l-1:
                    r.append(f[i-1]*b[i+1])
                elif i==0:
                    r.append(b[i+1])
                else:
                    r.append(f[i-1])
        return r


        