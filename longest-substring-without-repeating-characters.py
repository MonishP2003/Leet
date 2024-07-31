class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = maxlen = 0
        seenchar = set()
        for r in range(len(s)):
            while s[r] in seenchar:
                seenchar.remove(s[l])
                l += 1
            seenchar.add(s[r]) 
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen                   