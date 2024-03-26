class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1 = head
        n2 = head
        result = []

        while n2:
            result.append(n2.val)
            n2 = n2.next

        for i in range(0, len(result), k):
            if i + k <= len(result):
                result[i:i+k] = reversed(result[i:i+k])

        n1 = head
        index = 0
        while n1:
            n1.val = result[index]
            index += 1
            n1 = n1.next

        return head