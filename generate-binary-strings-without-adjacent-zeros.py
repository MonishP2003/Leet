class Solution:
    def validStrings(self, n: int) -> List[str]:
        return [''.join(bits) for bits in product('01',repeat = n) if '00' not in ''.join(bits)]