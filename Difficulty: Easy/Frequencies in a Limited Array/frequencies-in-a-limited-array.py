class Solution:
    def frequencyCount(self, arr):
        #  code here
            n = len(arr)
            freq = {}
            for i in arr:
                freq[i] = freq.get(i, 0) + 1

            result = []
            for i in range(1, n+1):         
                result.append(freq.get(i, 0)) 

            return result

    

