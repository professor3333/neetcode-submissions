class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # This creates a new list where every stone weight is negative
        max_heap = [-s for s in stones]
        # Converts the list into a heap in-place (O(N) time). Now, the most negative number is at max_heap[0]
        heapq.heapify(max_heap) 

        # The loop continues as long as there are at least two stones to smash against each other
        while len(max_heap) > 1:
            # heappop removes the smallest value. We use the - sign to turn it back into a positive number
            first = -heapq.heappop(max_heap) # Heaviest stone
            second = -heapq.heappop(max_heap) # Second heaviest stone
            # If the stones are the same weight, they both vanish. If they are different, a new store is created with weight (first-second)
            if first != second:
                # We push the negative of this new weight back to the heap to maintain out max_heap simulation
                heapq.heappush(max_heap, -(first - second))

        # After the loop, the heap will either have one stone left or be empty. If max_heap exists, we return the positive value of the remaining stone(-max_heap[0]). If it is empty, we return 0
        return -max_heap[0] if max_heap else 0