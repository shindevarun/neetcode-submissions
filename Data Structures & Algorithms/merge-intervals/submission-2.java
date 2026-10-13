class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length < 2) {
            return intervals;
        }

        List<int[]> res = new ArrayList<>();

        // sort intervals based on start time
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

        // add the first interval to avoid edge cases
        res.add(intervals[0]);

        // iterate through intervals starting from 1, not 0. Check if the start of the current interval is less than
        // the end of the interval already in the list. if it is, they have to be merged. To merge simply change the end
        // value of the last item in the list to be max of itself and the end time of current interval. If no merge, just
        // add current interval to list
        for(int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            int lastEnd = res.get(res.size() - 1)[1];

            if(start <= lastEnd) {
                res.get(res.size()-1)[1] = Math.max(lastEnd, end);
            } else {
                res.add(intervals[i]);
            }
        }

        return res.toArray(new int[res.size()][]);
        
        
    }
}
