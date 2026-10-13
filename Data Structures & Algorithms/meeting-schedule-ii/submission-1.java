/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */


// problem is essentially asking for what is the maximum number of intervals that ever overlap. find this out by 
// creating 2 arrays. One for start times and one for end times. Then sort these arrays. Now use 2 pointers to check
// elements from start and end array. Compare and if startTines[start] < endTimes[iend], you have to start a 
// new meeting. Therefore increment meeting counter and upfate days (max overlapping meetings) appropriately. 
// Else cond meens meeting has to end. Therefore dececrement meeting counter and update endTimes pointer.

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int[] startTimes = new int[intervals.size()];
        int[] endTimes = new int[intervals.size()];

        for(int i = 0; i < intervals.size(); i++) {
            startTimes[i] = intervals.get(i).start;
            endTimes[i] = intervals.get(i).end;
        }

        Arrays.sort(startTimes);
        Arrays.sort(endTimes);

        int start = 0;
        int end = 0;
        int days = 0;
        int meetings = 0;

        while(start < startTimes.length) {
            if(startTimes[start] < endTimes[end]) {
                meetings++;;
                start++;

                if(meetings > days) {
                    days = meetings;
                }
            } else {
                meetings--;
                end++;
            }
        }

        return days;
    }
}
