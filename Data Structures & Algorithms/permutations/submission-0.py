class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            # Base case: completed a full permutation
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                # Choose
                used.add(num)
                path.append(num)

                # Explore
                backtrack()

                # Unchoose (Backtrack)
                path.pop()
                used.remove(num)

        backtrack()
        return res