class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dictionary = {}
        top_k_values = []
        for num in nums:
            freq_dictionary[num] = freq_dictionary.get(num, 0) + 1 

        largest_to_smallest = sorted(freq_dictionary.items(), key = lambda x: x[1], reverse = True)
        return [item[0] for item in largest_to_smallest[:k]]