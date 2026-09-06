class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if target == (nums[i] + nums[j]) and i != j:
                    return [i,j]
