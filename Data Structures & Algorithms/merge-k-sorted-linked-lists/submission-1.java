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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) {
            return null;
        }

        for(int i = 1; i < lists.length; i++) {
            lists[i] = twoListMerge(lists[i], lists[i-1]);
        }

        return lists[lists.length - 1];
    }

    private ListNode twoListMerge(ListNode list1, ListNode list2) {
        ListNode output = new ListNode(0);
        ListNode curr = output;

        while(list1 != null && list2 != null) {
            if(list1.val < list2.val) {
                curr.next = list1;
                list1 = list1.next;
            } else {
                curr.next = list2;
                list2 = list2.next;
            }

            curr = curr.next;
        }

        if(list1 == null) {
            curr.next = list2;
        } else if (list2 == null) {
            curr.next = list1;
        }

        return output.next;
    }

    public static void printList(ListNode head) {
        ListNode curr = head;
        while(curr != null) {
            System.out.print(curr.val + "->");
            curr = curr.next;
        }
        System.out.println();
    }
}
