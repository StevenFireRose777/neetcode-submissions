class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: Int array
        Output: Int array
        Idea:
        - output[i] = nums[i] = nums[i + 1] * nums[i + 2] ...
        - NOTE: nums[i] is excluded
        - When multiplying start at beginning at array and SKIP the number that i is currently on
        - We POSSIBLY need i for appending to current pos of output array

        # Brute Force O(n^2)
        # product = 1
        # output = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         else:
        #             product *= nums[j]
        #     output.append(product)
        #     product = 1
        # return output
        """
        output = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
