class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = []
        char_count = {}
        for char in s:
            q.append(char)
            char_count[char] = char_count.get(char, 0) + 1
        
        for i in range(len(s)):
            if char_count[q.pop(0)] == 1:
                return i
            
        return -1