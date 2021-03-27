#problem-https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#author-Vallabh

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp=head
        while head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return temp
    
                    