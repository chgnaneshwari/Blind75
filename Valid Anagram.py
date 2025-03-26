class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count the frequency of each character in both strings
        return sorted(s) == sorted(t)
