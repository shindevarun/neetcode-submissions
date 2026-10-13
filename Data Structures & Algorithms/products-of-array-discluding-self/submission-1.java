class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefixArray = new int[nums.length];
        int[] suffixArray = new int[nums.length];

        prefixArray[0] = 1;
        suffixArray[nums.length - 1] = 1;

        // populate the prefix product array
        for(int i = 1; i < nums.length; i++) {
            prefixArray[i] = prefixArray[i-1] * nums[i-1];
        }

        // populate the suffix array
        for(int i = nums.length - 2; i >= 0; i--) {
            suffixArray[i] = suffixArray[i+1] * nums[i+1];
        }

        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            res[i] = prefixArray[i] * suffixArray[i];
        }

        return res;

    }
}  
