class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicate = False 
        for num in nums:
            if num in seen:
                duplicate = True 

            seen.add(num)
        return duplicate 