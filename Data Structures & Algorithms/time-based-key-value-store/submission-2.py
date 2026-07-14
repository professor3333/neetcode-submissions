class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        history = self.store[key]

        left = 0
        right = len(history) - 1
        best_match = ""

        while left <= right:
            mid = left + (right - left) // 2
            if history[mid][0] <= timestamp:
                best_match = history[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return best_match
