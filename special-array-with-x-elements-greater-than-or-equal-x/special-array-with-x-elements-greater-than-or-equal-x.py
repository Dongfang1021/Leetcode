class Solution:
    def specialArray(self, nums: List[int]) -> int:
        number = 0
        for i in sorted(nums,reverse=True):
            number+=1
            if i < number or i<=0:
                number-=1
                break
        return number if number == sum(map(lambda x:x>=number, nums)) else -1