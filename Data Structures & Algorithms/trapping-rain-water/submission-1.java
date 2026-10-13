class Solution {
    public int trap(int[] height) {
        if(height.length == 0) {
            return 0;
        }

        int total = 0;
        int left = 0;
        int right = height.length - 1;
        int maxLeft = height[left];
        int maxRight = height[right];

        while(left < right) {
            if(maxLeft < maxRight) {
                left++;
                int vol = maxLeft - height[left];
                if(vol > 0) {
                    total += vol;
                }

                if(height[left] > maxLeft) {
                    maxLeft = height[left];
                }

            } else {
                right--;
                int vol = maxRight - height[right];
                if (vol > 0) {
                    total += vol;
                } 

                if(height[right] > maxRight) {
                    maxRight = height[right];
                }
                
            }
        }

        return total;
    }
}
