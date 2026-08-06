class MedianFinder:

    def __init__(self):
        self.small = [] # Will track the smaller elements. The top of the heap is the largest value in the lower half
        self.large = [] # Will track the larger elements. The top of this heap is the smallest in the upper half

    def addNum(self, num: int) -> None:
        # 1) We add the new number to the small heap. We use -num because heapq is a min-heap, by negating the value, the largest absolute number stays at the top
        heapq.heappush(self.small, -num)
        # 2) This checks if the largest number in the "small" half is actually bigger than the smallest number in the "large" half. If it is, the halves are out of order. We move the top of small to large to fix the boundary. 
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 3) Rebalance the sizes of the two heaps, maintaining the rule that small can have at most one more element than large, but never fewer
        if len(self.small) > len(self.large) + 1:
            # If small has more than one extra element compared to large, move the largest value from small to large
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            # If large becomes bigger than small, move the smallest value from large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

            # After these checks, either both heaps are the same size, or small has exactly one more element than large

    def findMedian(self) -> float:
        # If small has one more element than large(the total count is odd), the true median is exactly the single middle element which sits right at the top of small. Negate it back to its real value and return it as a float
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # If the total number of elements is even, the median is the average of the two middle numbers(the top of small and the top of large)
        return (-self.small[0] + self.large[0]) / 2.0