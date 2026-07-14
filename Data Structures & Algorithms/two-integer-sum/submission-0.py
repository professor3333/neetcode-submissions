class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        notepad = {}

        for i, num in enumerate(nums):

            missing_piece = target - num

            if missing_piece in notepad:
                return [notepad[missing_piece], i]

            notepad[num] = i

    