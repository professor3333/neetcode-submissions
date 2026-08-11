class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                
                # .add() is exclusively used to insert items into a set, while  is exclusively used to add items to the end of a list.
                used.add(num)
                path.append(num)

                backtrack()

                path.pop()
                used.remove(num)

        backtrack()
        return res