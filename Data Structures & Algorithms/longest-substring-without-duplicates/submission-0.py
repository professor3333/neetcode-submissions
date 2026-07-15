class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1

            char_map[current_char] = right

            max_len = max(max_len, right - left + 1)

        return max_len