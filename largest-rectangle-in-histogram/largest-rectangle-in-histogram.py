class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pos = []
        val = []
        max1 = 0
        temp = 0
        for i in range(len(heights)):
            if val == [] or val[-1]<heights[i]:
                pos.append(i)
                val.append(heights[i])
            else:
                temp = i
                while(val != [] and val[-1]>heights[i]):
                    max1 = max(max1, val[-1]*(i-pos[-1]))
                    val.pop()
                    temp = pos.pop()
                if val == [] or val[-1]!=heights[i]:
                    val.append(heights[i])
                    pos.append(temp)
        i = len(heights)
        while(val!=[]):
            max1 = max(max1, val[-1]*(i-pos[-1]))
            val.pop()
            pos.pop()
        return max1
