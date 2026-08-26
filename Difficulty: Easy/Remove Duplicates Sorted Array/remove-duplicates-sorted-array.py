class Solution:
    def removeDuplicates(self, arr):
        # code here 
        l = 0
        for r in range(1,len(arr)):
            if arr[l] != arr[r]:
                l +=1
                arr[l] = arr[r]
        return arr[:l+1]