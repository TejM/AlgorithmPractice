class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = local_max
        for x in range (1, len(nums)):
            current_number = nums[x]
            local_max = max(current_number, local_max + current_number)
            global_max = max(global_max, local_max)
        return global_max

# Time complexity: O(N)
# Space complexity: O(1)
