class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = [-1, arr[-1]]
        l = len(arr)
        if l>2:
            m=(arr[-1])
            for i in range(l-2, 0, -1):
                if arr[i]>m:
                    a.append(arr[i])
                    m=arr[i]
                else:
                    a.append(m)
            return reversed(a)
        else:
            if l == 1:
                return [-1]
            else:
                return[arr[-1], -1]