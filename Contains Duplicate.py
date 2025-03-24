class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # Create an empty set to track unique numbers
        for num in nums:
            if num in seen:
                return True  # Return True if the number is already in the set
            seen.add(num)  # Add the number to the set if not already present
        return False  # Return False if no duplicates were found
