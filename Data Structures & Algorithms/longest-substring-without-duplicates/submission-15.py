class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        longest = 0
        hashmap = {}
        while right < len(s):
            if s[right] in hashmap:
                while left <= hashmap[s[right]]:
                    left += 1
            hashmap[s[right]] = right
            longest = max(longest, right - left+1)
            right += 1 
        return longest

        