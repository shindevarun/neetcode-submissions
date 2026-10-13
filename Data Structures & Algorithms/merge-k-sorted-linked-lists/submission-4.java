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

// Best case: O(n*k) time complexity where n = avg len(list) & k = # of lists
// Essentially can just merge 2 lists at once and store it back in lists. 
// i.e. lists[i] will become the merged version of lists[i] & lists[i-1]. Keep doing this for all list in lists
// and then last list will contain the merged version of all lists.

// Exception check: If lists is empty, return null

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) {
            return null;
        }

        // start from 1 because we are calculting the merged version of the curr list and prev list
        for(int i = 1; i < lists.length; i++) {
            lists[i] = twoListMerge(lists[i], lists[i-1]);
        }

        return lists[lists.length - 1];
    }

    // takes 2 sorted linked lists and merges them. returns a new list thats the merged version of input lists
    // can't be static because we are declaring new ListNodes
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

    // debugging method to print list
    public static void printList(ListNode head) {
        ListNode curr = head;
        while(curr != null) {
            System.out.print(curr.val + "->");
            curr = curr.next;
        }
        System.out.println();
    }
}
