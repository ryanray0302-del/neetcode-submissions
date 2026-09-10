class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_of_dictionaries = []
        labels = {}

        for word in strs:

            frequency = {}

            for char in word:

                frequency[char] = frequency.get(char, 0) + 1 
            
            key = tuple(sorted(frequency.items()))

            if key not in labels:
                    labels[key] = []

            labels[key].append(word)

        return list(labels.values())



'''
        for i, dictionary in enumerate (list_of_dictionaries): 

            for j in range(len(list_of dictionaries) - 1):

                if dictionary == list_of_dictionaries[j]:
                    anagram.append()

'''
                