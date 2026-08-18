class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                return True       
            elif current_sum > target:
                right -= 1        
            else:
                left += 1         

        return False