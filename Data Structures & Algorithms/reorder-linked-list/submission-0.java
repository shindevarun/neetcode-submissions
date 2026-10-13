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
    public void reorderList(ListNode head) {
        if(head.next != null) {
            int length = 0;
            ListNode curr = head;
            
            // find the length
            while(curr != null) {
                length++;
                curr = curr.next;
            }

            curr = head;
            ListNode temp = curr;

            // find middle point
            for(int i = 0; i < length / 2; i++) {
                if(i == length/2 - 1) {
                    temp = curr;
                }
                curr = curr.next;
            }

            temp.next = null;

            // create new list and add the second half of the original list to it
            ListNode head2 = new ListNode(0);
            head2.next = curr;

            curr = head;
            head2 = head2.next;
            ListNode curr2 = head2;

            // reverse 2nd list
            ListNode prev = null;
            while(curr2 != null) {
                ListNode temp2 = curr2.next;
                curr2.next = prev;
                prev = curr2;
                curr2 = temp2;
            }

            curr2 = prev;
            

            // interweave both list starting with list1
            boolean flag = true;
            while(curr != null && curr2 != null) {
                if(flag) {
                    ListNode temp3 = curr.next;
                    curr.next = curr2;
                    curr = temp3;
                } else {
                    ListNode temp3 = curr2.next;
                    curr2.next = curr;
                    curr2 = temp3;
                }

                flag = !flag;
            }

            

            
        }
        
        // return 1;
    }

    public static void printList (ListNode curr) {
        while(curr != null) {
            System.out.print(curr.val + "->");
            curr = curr.next;
        }
        System.out.println();
    }
}
