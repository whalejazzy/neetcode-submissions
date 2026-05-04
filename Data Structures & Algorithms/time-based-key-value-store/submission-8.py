class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if self.tmap[key] == [] or self.tmap[key][0][1] > timestamp:
            return ""
        else:
            
            lst = [pair[1] for pair in self.tmap[key]]
            if len(lst) == 2:
                print(lst)
            l = 0
            r = len(lst) - 1
            time_idx = 0
            while l <= r:
                m = (r - l) // 2 + l
                if len(lst) == 2:
                    print(m)
                if timestamp == lst[m]:
                    return self.tmap[key][m][0]
                elif timestamp < lst[m]:
                    r = m -1
                else:
                    time_idx = (m if lst[m] > lst[time_idx] else time_idx)
                    l = m + 1
            return self.tmap[key][time_idx][0]
