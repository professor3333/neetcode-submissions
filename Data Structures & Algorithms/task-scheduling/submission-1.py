from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Creates a dictionary like object that counts how many times each task appears
        task_counts = Counter(tasks)
        # This tells us how many times the most frequent task appears. Find the maximum frequency among all tasks
        max_freq = max(task_counts.values())
        # Count how many different task types share this maximum frequency
        max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        # Calculate minimum required time slots
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        # Result cannot be smaller than total number of tasks
        return max(len(tasks), ans)