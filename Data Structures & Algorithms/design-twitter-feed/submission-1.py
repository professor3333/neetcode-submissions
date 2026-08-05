import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweet_map = defaultdict(list)    # userId -> list of [count, tweetId]
        self.follow_map = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1  # Decrementing so min-heap acts as max-heap for timestamps
        self.tweet_map[userId].append([self.timer, tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []

        # Ensure user follows themselves to see their own tweets in news feed
        self.follow_map[userId].add(userId)

        # Initialize heap with the most recent tweet from each followee
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                # Push: [count, tweetId, followeeId, index - 1]
                min_heap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(min_heap)

        # Retrieve up to 10 most recent tweets
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, next_index = heapq.heappop(min_heap)
            res.append(tweetId)

            # If the followee has more tweets, push their next latest tweet
            if next_index >= 0:
                next_count, next_tweetId = self.tweet_map[followeeId][next_index]
                heapq.heappush(min_heap, [next_count, next_tweetId, followeeId, next_index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId] and followerId != followeeId:
            self.follow_map[followerId].remove(followeeId)