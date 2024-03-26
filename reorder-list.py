# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n1 = head
        n2 = head
        result = []
        while n2:
            result.append(n2.val)
            n2 = n2.next
        
        left, right = 0, len(result)-1
        while left <= right:
            n1.val = result[left]
            n1 = n1.next
            if n1:
                n1.val = result[right]
                n1 = n1.next
            left += 1
            right -= 1
