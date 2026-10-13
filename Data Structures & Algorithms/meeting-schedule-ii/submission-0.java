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
