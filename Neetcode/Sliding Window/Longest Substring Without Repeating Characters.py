class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueCharacters = []
        maxRes = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] not in uniqueCharacters:
                uniqueCharacters.append(s[r])
                res += 1
            else:
                maxRes = max(maxRes, res)
                # Remove characters from the beginning until the duplicate character is removed
                while uniqueCharacters and uniqueCharacters[0] != s[r]:
                    uniqueCharacters.pop(0)
                if uniqueCharacters:
                    uniqueCharacters.pop(0)  # Remove the duplicate character itself
                uniqueCharacters.append(s[r])  # Add current character to uniqueCharacters
                res = len(uniqueCharacters)  # Update res with the new count of unique characters
        
        maxRes = max(maxRes, res)  # Final check after the loop ends
        return maxRes

# Example usage:
solution = Solution()
Input1 = "zxyzxyz"
Input2 = "xxxx"

print(solution.lengthOfLongestSubstring(Input1))  # Expected output: 6
print(solution.lengthOfLongestSubstring(Input2))  # Expected output: 0