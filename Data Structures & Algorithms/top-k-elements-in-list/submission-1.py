class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracker = Counter(nums)

        frequent = count_tracker.most_common(k)

        return[item[0] for item in frequent]