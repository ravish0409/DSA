class Solution:
    def evalRPN(self, t: List[str]) -> int:
        l=[]
        if len(t)==1:
            return int(t[0])
        o=['+', '-', '*','/']
        for i in t:
            if i not in o:
                l.append(i)
            else:
                f=l.pop()
                print(l)
                s=l.pop()
                print(l)
                op=f"{s}{i}{f}"
                print(op)
                l.append(int(eval(op)))
                print(l)
        return l[-1]

            