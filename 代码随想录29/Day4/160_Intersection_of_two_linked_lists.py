# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Calculate the length difference between two linked lists
        dis = self.getLength(headA) - self.getLength(headB)

        # Adjust the starting point of the longer linked list
        if dis > 0:
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))

        # Traverse both linked lists until an intersection point is found
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        # If no intersection is found, return None
        return None

    # Helper function to calculate the length of a linked list
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # Helper function to move the pointer forward in a linked list by a specified number of steps
    def moveForward(self, head: ListNode, step: int) -> ListNode:
        while step > 0:
            head = head.next
            step -= 1
        return head
