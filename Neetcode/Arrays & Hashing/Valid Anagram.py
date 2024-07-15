class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize two lists of size 26 for each alphabet letter
        count_s = [0] * 26
        count_t = [0] * 26
        
        # Fill the frequency lists
        for char in s:
            count_s[ord(char) - ord('a')] += 1
        for char in t:
            count_t[ord(char) - ord('a')] += 1
        
        # Compare the frequency lists
        return count_s == count_t

# Example usage:
solution = Solution()

# Example 1
s1 = "racecar"
t1 = "carrace"
print(solution.isAnagram(s1, t1))  # Output: True

# Example 2
s2 = "jar"
t2 = "jam"
print(solution.isAnagram(s2, t2))  # Output: False