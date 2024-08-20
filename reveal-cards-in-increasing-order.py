class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)

        indices = deque(range(len(deck)))

        for card in deck:
            result[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())
        return result