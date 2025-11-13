class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        seen = {}
        seen2 = {}
        for i in a:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in b:
            if i in seen2:
                seen2[i] += 1
            else:
                seen2[i] = 1
                
        if seen != seen2:
            return False
        return True
                