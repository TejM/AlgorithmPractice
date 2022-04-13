class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index in range(len(nums)):
            num_dict[nums[index]] = index 
        
        for index in range(len(nums)):
            number = nums[index]
            complement = target - number
            if complement in num_dict and num_dict[complement] != index:
                return [index, num_dict[complement]]
# Time complexity = O(N)
# Space Complexity = O(N)
