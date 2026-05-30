class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: A list of numbers
        # Output: Integar
        # An empty list

        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                longest = max(length, longest)
    
        return longest
            

