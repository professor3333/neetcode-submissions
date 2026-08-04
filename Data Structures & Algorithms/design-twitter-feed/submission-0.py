from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)  
        self.user_follows = defaultdict(set)  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        self.user_follows[userId].add(userId)

        for followee_id in self.user_follows[userId]:
            tweets = self.user_tweets[followee_id]
            if tweets:
                last_idx = len(tweets) - 1
                time, tweet_id = tweets[last_idx]
                max_heap.append((-time, tweet_id, followee_id, last_idx - 1))

        heapq.heapify(max_heap)

        while max_heap and len(res) < 10:
            neg_time, tweet_id, followee_id, next_idx = heapq.heappop(max_heap)
            res.append(tweet_id)

            if next_idx >= 0:
                time, prev_tweet_id = self.user_tweets[followee_id][next_idx]
                heapq.heappush(max_heap, (-time, prev_tweet_id, followee_id, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)