class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                s += a[0]
            else:
                return s
        return s
Solution()