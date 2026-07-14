import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_speed = right
        while left <= right:
            mid_speed = left + (right - left) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid_speed)

            if total_hours <= h:
                best_speed = mid_speed
                right = mid_speed - 1
            else:
                left = mid_speed + 1
        return best_speed