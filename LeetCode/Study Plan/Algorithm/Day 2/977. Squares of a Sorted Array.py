class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums) - 1
        sorted_array = [0 for x in range(len(nums))]
        insert_position = len(nums) - 1
        while left_pointer <= right_pointer:
            right_item = nums[right_pointer]
            left_item = nums[left_pointer]
            if abs(right_item) >= abs(left_item):
                sorted_array[insert_position] = right_item**2
                right_pointer -= 1           
            else:
                sorted_array[insert_position] = left_item**2
                left_pointer += 1
            insert_position -= 1
        return sorted_array
# Time Complexity O(N)
# Space Complexity O(1)
