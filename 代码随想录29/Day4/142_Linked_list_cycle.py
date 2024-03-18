# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, fast and slow, both starting from the head
        fast = head
        slow = head

        # Move fast pointer twice as fast as the slow pointer
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            # If there is a cycle, the fast and slow pointers will meet at some point
            if fast == slow:
                # Move one pointer to the head and continue until they meet again,
                # this will be the start of the cycle
                index1 = fast
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                # Return the node where the cycle begins
                return index1

        # If there is no cycle, return None
        return None
