class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This will hold at most k elements at any point, it will end up holding exactly the k largest values seen from nums
        min_heap = []
        # Scan through every number in nums, pushing each one onto the heap. heapq keeps the smallest currently held value sitting at the top
        for num in nums:
            heapq.heappush(min_heap, num)
            # If the heap grows past k elements, pop off the top, which removes the smallest value currently being tracked
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # The top of the heap is the kth largest element. The smallest of the k largest numbers is the kth largest
        return min_heap[0]