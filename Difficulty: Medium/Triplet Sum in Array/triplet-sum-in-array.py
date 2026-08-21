class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        n = len(arr)

        for i in range(n-2):
            l = i+1
            r = n-1
            remaining = target - arr[i]

            while l < r:
                current = arr[l] + arr[r]
                if current == remaining:
                    return True
                elif current > remaining:
                    r -= 1
                else:
                    l +=1
        return False