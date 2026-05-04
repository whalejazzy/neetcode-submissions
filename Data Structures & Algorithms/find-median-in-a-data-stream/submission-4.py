class MedianFinder:

    def __init__(self):
        self.maxhp = []
        self.minhp = []

    def addNum(self, num: int) -> None:
        if len(self.minhp) == len(self.maxhp):
            if self.maxhp and num < -self.maxhp[0]:
                heapq.heappush(self.maxhp, -num)
                minval = -heapq.heappop(self.maxhp)
                heapq.heappush(self.minhp, minval)
            else:
                heapq.heappush(self.minhp, num)
        elif len(self.minhp) > len(self.maxhp):
            if num > self.minhp[0]:
                heapq.heappush(self.minhp, num)
                maxval = heapq.heappop(self.minhp)
                heapq.heappush(self.maxhp, -maxval)
            else:
                heapq.heappush(self.maxhp,-num)
        print("maxhp: ")
        print(self.maxhp)
        print("minhp: ")
        print(self.minhp)
        


    def findMedian(self) -> float:
        if len(self.minhp) > len(self.maxhp):
            return self.minhp[0]
        else:
            return (self.minhp[0] - self.maxhp[0]) / 2

        
        