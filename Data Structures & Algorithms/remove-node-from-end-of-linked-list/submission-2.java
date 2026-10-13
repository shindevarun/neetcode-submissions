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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next == null) {
            return null;
        }

        int length = 0;
        ListNode curr = head;

        while(curr != null) {
            length++;
            curr = curr.next;
        }

        curr = head;
        int iterations = length - n;


        if(iterations != 0) {
            for(int i = 0; i < iterations - 1; i++) {
                curr = curr.next;
            }

            curr.next = curr.next.next;
        } else {
            head = head.next;
        }

        return head;
    }
}
