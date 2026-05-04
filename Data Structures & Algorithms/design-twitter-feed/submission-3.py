class Twitter:

    def __init__(self):
        self.users = {}
        self.timer = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [set([(self.timer, tweetId)]), set()]
        else:
            self.users[userId][0].add((self.timer, tweetId))        
        self.timer -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.users:
            hp = list(self.users[userId][0])
            for follower in self.users[userId][1]:
                hp.extend(list(self.users[follower][0]))
            heapq.heapify(hp)
            res = []
            for _ in range(10):
                if hp:
                    res.append(heapq.heappop(hp)[1])
            return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [set(), set([followeeId])]
        elif followerId != followeeId:
            self.users[followerId][1].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
