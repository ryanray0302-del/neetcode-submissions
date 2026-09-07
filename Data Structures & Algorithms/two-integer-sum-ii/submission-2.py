class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 
        solution = [] 
        numbers.sort()

        while left != right:
            if numbers[left] + numbers[right] > target:
                right -= 1 
            elif numbers[left] + numbers[right] < target:
                left += 1 
            else:
                solution.append(left+1)
                solution.append(right+1)
                solution.sort()
                return solution