#problem-https://leetcode.com/problems/remove-linked-list-elements/
#author-Vallabh



Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        temp=head
        while temp:
            if temp==head and temp.val==val: # if the first element is equal to val
                temp=temp.next
                head=temp
            else:
                prev=temp
                temp=temp.next
                if temp:
                    if temp.val==val:
                        prev.next=temp.next
                        temp=prev
        return head