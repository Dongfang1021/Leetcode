class Solution:
    def average(self, salary: List[int]) -> float:
        del salary[salary.index(min(salary))]
        del salary[salary.index(max(salary))]
        return sum(salary)/len(salary)