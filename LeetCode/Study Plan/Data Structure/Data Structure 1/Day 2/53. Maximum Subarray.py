# Brute Force solution.
# Time complexity = O(N^2)
# Space Complexity = O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = - math.inf
        local_max = 0
        for i in range(len(nums)):
            local_max = 0
            for j in range(i, len(nums)):
                local_max += nums[j]
                global_max = max(local_max, global_max)
        return global_max
     
# Optimal solution using Kadane's algorithm.
# Time complexity = O(N)
# Space Complexity = O(1)    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = local_max
        for x in range (1, len(nums)):
            current_number = nums[x]
            local_max = max(current_number, local_max + current_number)
            global_max = max(global_max, local_max)
        return global_max
