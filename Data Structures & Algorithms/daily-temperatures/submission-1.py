class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                cold_day_index = stack.pop()
                answer[cold_day_index] = i - cold_day_index
            stack.append(i)
        return answer