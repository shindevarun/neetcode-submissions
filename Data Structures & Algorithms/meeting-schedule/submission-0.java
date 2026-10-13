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
    public boolean canAttendMeetings(List<Interval> intervals) {
        boolean flag = true;

        if(intervals.size() < 2) {
            return flag;
        }

        Collections.sort(intervals, Comparator.comparingInt(i -> i.start));

        for(int i = 1; i < intervals.size(); i++) {
            int start = intervals.get(i).start;
            int prevEnd = intervals.get(i-1).end;

            if(start < prevEnd) {
                flag = false;
                break;
            }
        }

        return flag;
    }
}
