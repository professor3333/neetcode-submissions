class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # Heaviest stone
            second = -heapq.heappop(max_heap)  # Second heaviest stone
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
                
        return -max_heap[0] if max_heap else 0