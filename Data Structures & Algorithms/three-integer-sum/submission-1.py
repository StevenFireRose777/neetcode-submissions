class Solution:
    # Total sum > 0: decrement right
    # Total sum < 0: increment left
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        all_triplets = []
        n = len(nums) - 1
        nums.sort() # sort it first
        for i, num in enumerate(nums):
            left = i + 1
            right = n

            # Skip any duplicates
            if i > 0 and num == nums[i - 1]:
                continue
            # Two ptrs tech.
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    all_triplets.append([num, nums[left], nums[right]])
                    left += 1 
                    # Skip any left-side elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return all_triplets
                
