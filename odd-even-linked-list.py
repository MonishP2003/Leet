# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n1 = head
        n2 = head
        result = []
        odd = []
        even = []
        while n2:
            result.append(n2.val)
            n2 = n2.next

        for i in range(0, len(result), 2):
            odd.append(result[i])
        
        for i in range(1, len(result), 2):
            even.append(result[i])
 
        result = odd + even
        index = 0
        while n1:
            n1.val = result[index]
            index += 1
            n1 = n1.next

        return head
        