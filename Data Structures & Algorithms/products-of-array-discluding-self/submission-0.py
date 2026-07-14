class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length

        # From left to right
        running_product =  1
        for i in range(length):
            answer[i] = running_product
            running_product *= nums[i]

        # From right to left
        running_product = 1
        for i in range(length -1, -1, -1):
            answer[i] *= running_product
            running_product *= nums[i]

        return answer