# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1 = head
        n2 = head
        result = []

        while n2:
            result.append(n2.val)
            n2 = n2.next

        if result:
            k = k % len(result)
            result = result[-k:] + result[:-k]

        n1 = head
        index = 0

        while n1:
            n1.val = result[index]
            index += 1
            n1 = n1.next
        return head 