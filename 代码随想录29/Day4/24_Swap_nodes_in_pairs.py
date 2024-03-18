# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        curr = dummyHead
        while curr.next is not None and curr.next.next is not None:
            temp = curr.next  # store node 1
            temp1 = curr.next.next.next  # store node 3
            curr.next = curr.next.next  # connect current node to node 2
            curr.next.next = temp  # connect node 2 to node 1
            temp.next = temp1  # connect node 1 to node 3
            curr = curr.next.next  # move the pointer
        return dummyHead.next
