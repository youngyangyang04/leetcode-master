/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let dummyHead = new ListNode(0, head);
    let cur = dummyHead, count = 0;

    // calculate the total number of elements in the list
    while(cur){
        cur = cur.next;
        count++;
    }

    // pointer goes back to the head
    cur = dummyHead;
    while(count--){
        if(count === n)  cur.next = cur.next.next;
        else cur = cur.next;
    }

    return dummyHead.next;
};
