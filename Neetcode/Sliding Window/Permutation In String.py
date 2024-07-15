class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Function to get character count array
        def get_char_count(s: str) -> list:
            char_count = [0] * 26
            for char in s:
                char_count[ord(char) - ord("a")] += 1
            return char_count

        # Initialize character count arrays for s1 and the first window in s2
        s1_char_count = get_char_count(s1)
        window_char_count = get_char_count(s2[:len(s1)])

        # Check if the initial window matches s1_char_count
        if window_char_count == s1_char_count:
            return True

        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_char_count[ord(s2[i]) - ord("a")] += 1
            # Remove the character that is no longer in the window
            window_char_count[ord(s2[i - len(s1)]) - ord("a")] -= 1

            # Check if the current window matches s1_char_count
            if window_char_count == s1_char_count:
                return True

        return False

# Example usage
solution = Solution()
print(solution.checkInclusion("abc", "lecabee"))  # Output: True
print(solution.checkInclusion("abc", "lecaabee"))  # Output: False
