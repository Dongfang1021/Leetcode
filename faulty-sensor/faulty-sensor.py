class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        for i in range(len(sensor1)):
            if sensor1[i] != sensor2[i]:
                a = sensor2[i+1:] == sensor1[i:-1]
                b = sensor1[i+1:] == sensor2[i:-1]
                if a and b: return -1
                return 1 if a else 2
        return -1