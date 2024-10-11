# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        cur=head
        li=[]
        fin=[]
        while cur:
            li.append(cur.val)
            cur=cur.next
        print(li)
        if len(li)!=0:
            for k in li:
                if k==val:
                    continue
                else:
                    fin.append(k)
            if len(fin)!=0:
                head=ListNode(fin[0])
                mover=head
                if len(fin)!=0:
                    for i in range(1,len(fin)):
                        temp=ListNode(fin[i])
                        mover.next=temp
                        mover=mover.next
                return head
        else:
            return []
        