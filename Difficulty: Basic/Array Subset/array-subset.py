class Solution:
    def isSubset(self, a, b):
        # code here
        freq_a ={}
        for x in a:
            freq_a[x] = freq_a.get(x,0)+1
        freq_b ={}
        for y in b:
            freq_b[y] = freq_b.get(y,0)+1
        for element,count in freq_b.items():
            if freq_a.get(element,0)<count:
                return False
        return True
    
    
    
    
