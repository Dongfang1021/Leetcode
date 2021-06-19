class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        lst = self.map[key]
        ln = len(lst)
        if timestamp < lst[0][0]:
            return ""
        if timestamp > lst[-1][0]:
            return lst[-1][1]
        s = 0
        e = ln - 1
        while s <= e:
            mid = s + (e - s) // 2
            if lst[mid][0] == timestamp:
                return lst[mid][1]
            if lst[mid][0] < timestamp:
                if mid == ln - 1 or lst[mid + 1][0] > timestamp:
                    return lst[mid][1]
                s += 1
            else:
                if mid == 0:
                    return ""
                e -= 1
            
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)