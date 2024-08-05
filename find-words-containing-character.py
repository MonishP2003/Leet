class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l = []
        for index, word in enumerate(words):
            if x in word:
                l.append(index)
        return l