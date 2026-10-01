class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={
            "(":")",
            "{":"}",
            "[":"]"
        }
        for i in s:
            if i in d.keys():
                l.append(i)
            else:
                if len(l)>0:
                    if d[l.pop()]!=i:
                        return False
                else:
                    return False
        return False if l else True
        
        