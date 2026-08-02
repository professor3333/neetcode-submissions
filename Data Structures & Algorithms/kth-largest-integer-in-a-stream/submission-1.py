class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Store k. Then take the initial nums list and turn it into a valid min_heap in place using heapq.heapify()
        self.k = k
        # Takes the initial list of numbers and assigns it to a class variable
        self.min_heap = nums
        # This converts the list nums into a valid heap structure in-place
        heapq.heapify(self.min_heap)

        # If the initial list is larger than k, we don't need all the numbers. We only care about the k largest
        while len(self.min_heap) > self.k:
            # heappop removes the smallest element. So repeatedly pop off the smallest element until only k elements remain. Now, the smallest element in this heap (at index 0) is the kth largest
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Adds the new value into the heap. The heap automatically reorganizes itself so the smallest element stays at the top
        heapq.heappush(self.min_heap, val)
        # After adding the new value, the heap might have k+1 elements
        if len(self.min_heap) > self.k:
            # So we pop the smallest one. This ensures that the heap always contains only the k largest elements encountered so far
            heapq.heappop(self.min_heap)

        # In a Min-Heap, heap[0] is always the smallest element. Since our heap contains the k largest elements, the smallest among them is the kth largest overall
        return self.min_heap[0]
