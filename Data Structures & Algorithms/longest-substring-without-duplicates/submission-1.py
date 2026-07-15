class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Maps character to it's most recent index
        left = 0
        max_len = 0
        
        # The right pointer moves across the string from start to finish
        for right in range(len(s)):
            current_char = s[right]
            # char_map[current_char] >= left, checks if we have a duplicate
            if current_char in char_map and char_map[current_char] >= left:
                # Jump the left pointer to remove the duplicate
                left = char_map[current_char] + 1
            # Update the character's position to the current right index
            char_map[current_char] = right
            
            # right - left + 1, calculate the window size or number of characters
            # If left = 0 and right = 2, there are 3 characters: index 0, 1, and 2
            max_len = max(max_len, right - left + 1)

        return max_len