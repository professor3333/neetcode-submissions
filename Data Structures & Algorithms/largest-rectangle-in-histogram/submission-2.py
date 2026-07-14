class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights + [0]):
            start_index = i
            while stack and stack[-1][1] > h:
                pop_index, pop_height = stack.pop()
                width = i - pop_index
                current_area = pop_height * width
                max_area = max(max_area, current_area)
                start_index = pop_index
            stack.append((start_index, h))
        return max_area