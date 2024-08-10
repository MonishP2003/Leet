class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def baseconvertion(n,b):
            s = ""
            while n > 0:
                s += str(n%b)
                n //= b
            return int(s[::-1])
        for i in range(2,n):
            if baseconvertion(n,i) != n:
                return False
        return True
            