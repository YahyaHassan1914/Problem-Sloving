from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniqueNumVector = []
        frequencyVector = []
        
        for num in nums:
            if num not in uniqueNumVector:
                uniqueNumVector.append(num)
                frequencyVector.append(1)
            else:
                frequencyVector[uniqueNumVector.index(num)] += 1
        
        # Find the k most frequent elements
        result = []
        for _ in range(k):
            max_freq = max(frequencyVector)
            max_index = frequencyVector.index(max_freq)
            result.append(uniqueNumVector[max_index])
            # Set the frequency to -1 to avoid selecting it again
            frequencyVector[max_index] = -1
        
        return result

# Test cases
solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3], 2)) # [2, 3]
print(solution.topKFrequent([7,7], 1))         # [7]
