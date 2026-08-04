from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        return max(len(tasks), ans)