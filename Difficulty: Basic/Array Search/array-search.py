class Solution:
    def search(self, arr, x):
        # code here
        for index, value in enumerate(arr):
            if value == x:
                return index
        return -1