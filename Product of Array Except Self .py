class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # Step 1: Calculate left products and store in the result array
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Step 2: Calculate right products and multiply with the result array
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
