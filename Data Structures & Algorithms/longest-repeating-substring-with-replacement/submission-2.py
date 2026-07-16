class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # A dictionary(map) to store frequency of each character
        left = 0 
        max_freq = 0
        max_len = 0

        # Starts a loop where right is the pointer representing the end of the sliding window, it moves from left to right expanding the window
        for right in range(len(s)):
            # Include the current character in the frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            # (right - left + 1) = size of the current window
            # (size - max_freq) = number of character we must replace. Shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1 # Shrink by decrementing the count of the character at the left pointer
                left += 1 # Move the left pointer forward to shrink the window size
            # Update the maximum valid window size
            max_len = max(max_len, right - left + 1)

        return max_len