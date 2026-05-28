class Solution:
    # Brute Force Sol
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_after = []
        n = len(temperatures)
        for i in range(n):
            count = 0
            curr_temp = temperatures[i]
            for j in range(i + 1, n):
                next_temp = temperatures[j]
                if next_temp > curr_temp:
                    days_after.append(j - i)
                    break                    
            else: # when break doesn't get activated, for-loop executes normally.
                days_after.append(0)

        return days_after
