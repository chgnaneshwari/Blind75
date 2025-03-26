class Solution:
    def findMaxSumSubArray(self, k, arr):
        # Edge case: if the array is smaller than k, return -1 (invalid case)
        if len(arr) < k or k <= 0:
            return -1
        
        # Calculate the sum of the first 'k' elements
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # Slide the window over the rest of the array
        for i in range(k, len(arr)):
            # Slide the window by subtracting the element going out and adding the new element
            window_sum += arr[i] - arr[i - k]
            
            # Keep track of the maximum sum
            max_sum = max(max_sum, window_sum)
        
        return max_sum
