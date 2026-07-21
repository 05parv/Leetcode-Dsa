# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp= head
        n=0
        while temp is not None:
            temp=temp.next
            n+=1

        temp=head
        for i in range (0,n//2):
            temp=temp.next
        return temp
