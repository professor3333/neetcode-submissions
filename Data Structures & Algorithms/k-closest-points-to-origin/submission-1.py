class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [] # This list will be treated as our heap structure

        # We loop through every point [x,y]
        for x, y in points:
            # This is the squared Euclidean distance. We don't need to take the square root because if a^2 < b^2, then a < b
            dist = x*x + y*y
            # heapq in Python is a min_heap by default. To turn it into a max_heap, we store the distance as a negative value(-dist)
            heapq.heappush(max_heap, (-dist, [x,y]))
            # Everytime we add a point, we check if the heap has more than k points. If it does, we heappop. 
            if len(max_heap) > k:
                # Becuase the distances are negative, the "smallest" number in the heap is actually the largest distance. By popping it, we are removing the point that is farthest from the origin
                heapq.heappop(max_heap)

        # Once all points have been processed, max_heap contains exactly the k closest point overall. This list comprehension unpacks each (-dist, point) tuple, discards the distance (using _ as a throwaway variable name), and collects just the point values into the final result list
        return [point for _, point in max_heap]