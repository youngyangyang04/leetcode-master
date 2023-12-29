# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(
            0, head
        )  # Initialized with a value of 0, and its next pointer is set to the input head

        fast = dummyHead
        slow = dummyHead
        for i in range(n + 1):
            fast = fast.next
            # The fast pointer is moved ahead by n + 1 steps.

        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        #  The slow pointer is at the node right before the target node to be removed. The next pointer of slow is then adjusted to skip the n-th node.

        return dummyHead.next
