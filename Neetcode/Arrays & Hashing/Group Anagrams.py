from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = []
        strsVector = []
        
        # Fill the frequency vectors for each word
        for word in strs:
            # Initialize a list of size 26 for each alphabet letter
            wordVector = [0] * 26
            # Fill the frequency list
            for char in word:
                wordVector[ord(char) - ord('a')] += 1
            strsVector.append(wordVector)
        
        # Group anagrams
        for i in range(len(strs)):
            added = False
            for group in returnList:
                # Check if current word's vector matches the vector of any group member
                if strsVector[i] == strsVector[strs.index(group[0])]:
                    group.append(strs[i])
                    added = True
                    break
            # If the word was not added to any existing group, create a new group
            if not added:
                returnList.append([strs[i]])
        
        # Return anagram list
        return returnList

# Test cases
solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])) # [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
print(solution.groupAnagrams(["x"])) # [["x"]]
print(solution.groupAnagrams([""])) # [[""]]
