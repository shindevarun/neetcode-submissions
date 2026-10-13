class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length < 2) {
            return intervals;
        }

        List<int[]> res = new ArrayList<>();
        // sort intervals based on start time
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

        res.add(intervals[0]);

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
