class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Input: Int array
        Output: Int array
        Idea:
        - output[i] = nums[i] = nums[i + 1] * nums[i + 2] ... 
        - NOTE: nums[i] is excluded
        - When multiplying start at beginning at array and SKIP the number that i is currently on
        - We POSSIBLY need i for appending to current pos of output array
        ex: [1,2,4,6]
        product = 0
        output = []
        loop #1:
        product = 2 * 4 * 6 = 48
        output = [48]
        loop #2: 
        product = 1 * 4 * 6 = 24
        output = [48,24]
        loop #3:
        product = 1 * 2 * 6 = 12
        output = [48,24,12]
        loop #4:
        product = 1 * 2 * 4 = 8
        output = [48,24,12,8]
        '''
        
        # Brute Force O(n^2)
        product = 1
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    product *= nums[j]
            output.append(product)
            product = 1
        return output
        
            


        