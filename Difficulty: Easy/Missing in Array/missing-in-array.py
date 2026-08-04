class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        expectedsum =  n * (n+1)//2
        actualsum = sum(arr)
        missing = expectedsum - actualsum
        return missing
        