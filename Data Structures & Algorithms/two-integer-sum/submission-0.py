class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Inverse formula: target - curr_num == a value found in a dictionary
        # Dictionary: used to store indices as keys and int values as values
        some_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in some_dict:
                return [some_dict[target-nums[i]], i]
            else:
                some_dict[nums[i]] = i
        return [-1,-1]