class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        out = []
        stack = []  # store temperatures
        dist_stack = []  # store distances
        
        # reverse traversal using pop()
        while t:
            cur = t.pop()
            days = 0
            
            # pop until we find a hotter day
            while stack and cur >= stack[-1]:
                days += dist_stack.pop()
                stack.pop()
            
            if not stack:
                out.append(0)
                dist_stack.append(1)
            else:
                out.append(days + 1)
                dist_stack.append(days + 1)
            
            stack.append(cur)
        
        return out[::-1]
