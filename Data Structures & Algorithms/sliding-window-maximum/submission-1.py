from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        # This will collect the maximum of each window
        output = []
        # Stores indices into nums. nums[q[0]] ia always the largest value currently in the window
        q = deque()

        # r is the right edge of the window, moving one step at a time across the whole array
        for r in range(len(nums)):
            # If the value at the back of the queue(nums[q[-1]]) is less than or equal to the new value nums[r], it can never be the maximum of any future window that still contains nums[r], so pop it from the back
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            # Since smaller/equal elements are cleared from the back, add the current index to the back of the deque
            q.append(r)

            # If the leftmost index in the queue is outside the active window, remove it from the left. A window of size k spans exactly k consecutive indices
            if q[0] < r - k + 1:
                q.popleft()

            # Since indexing starts at 0, the very fitst window[0, 1, ..., k-1] only becomes complete once r reaches its last index k - 1
            # Once this is true, q[0] holds the index of the max value in the current window. nums[q[0]] returns that value
            if r >= k - 1:
                output.append(nums[q[0]])

        # output contains the maximum for every window position, in order
        return output