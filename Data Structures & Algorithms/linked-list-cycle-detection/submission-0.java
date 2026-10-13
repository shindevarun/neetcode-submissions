/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        boolean firstCycle = true;
        ListNode slow = head;
        ListNode fast = head;

        while(fast != null && fast.next != null) {
            if(slow == fast) {
                if(firstCycle == false) {
                    return true;
                } else {
                    firstCycle = false;
                }
            }

            slow = slow.next;
            fast = fast.next.next;
        }

        return false;
    }
}
