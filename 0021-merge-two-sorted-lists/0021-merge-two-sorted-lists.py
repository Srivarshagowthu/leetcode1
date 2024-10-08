# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        if list1 is None and (list2 is None):
            return
        cur=list1
        while cur:
            res.append(cur.val)
            cur=cur.next
        cur1=list2
        while cur1:
            res.append(cur1.val)
            cur1=cur1.next
        need=sorted(res)
        head=ListNode(need[0])
        mover=head
        for i in range(1,len(need)):
            temp=ListNode(need[i])
            mover.next=temp
            mover=mover.next
        return head
        