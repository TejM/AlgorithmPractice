class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotated_array = [0]*len(nums)
        for x in range(len(rotated_array)):
            rotated_array[x] = nums[(len(nums) + x - k)% len(nums)]
        for x in range(len(rotated_array)):
            nums[x] = rotated_array[x]

# Time Complexity = O (N)
# Space Complexity = O(N)
