class Solution:
    def findDuplicates(self, arr):
        # code here
        freq = {}    
        result = []    
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        for key, val in freq.items():
            if val == 2:
                result.append(key)

        return result
            