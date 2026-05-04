class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda tup: tup[0], reverse = True)
        stack = []
        for car in cars:
            p, s = car
            time = (target - p)/s
            if len(stack) > 0 and time <= stack[-1]:
                print("here")
                continue
            stack.append(time)
        print(stack)
        return len(stack)
