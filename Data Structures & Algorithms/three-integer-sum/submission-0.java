class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        List<List<Integer>> list = new ArrayList<>();

        for(int i = 0; i < nums.length; i++) {
            if(i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            
            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < 0) {
                    left++;
                } else if(sum > 0) {
                    right--;
                } else {
                    List<Integer> sol = new ArrayList<>();
                    sol.add(nums[i]);
                    sol.add(nums[left]);
                    sol.add(nums[right]);

                    list.add(sol);

                    left++;
                    while(nums[left] == nums[left - 1] && left < right) {
                        left++;
                    }
                }
            }
        }

        return list;

    }
}
