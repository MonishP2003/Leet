# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        left, right = 0, len(result)-1

        while left < right and result[left] == result[right]:
            left += 1
            right -= 1
        return left >= right
        