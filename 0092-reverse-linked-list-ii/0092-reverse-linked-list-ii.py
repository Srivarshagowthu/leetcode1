# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        res=[]
        res1=[]
        cur=head
        while cur:
            res1.append(cur.val)
            cur=cur.next
        res=res1[:left-1]+res1[left-1:right][::-1]+res1[right:]
        print(res)
        ##into ll
        head=ListNode(res[0])
        mover=head
        for i in range(1,len(res)):
            temp=ListNode(res[i])
            mover.next=temp
            mover=mover.next
        return head


            
        