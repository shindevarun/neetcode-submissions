class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        } else if (s.length() == 1) {
            return 1;
        }

        HashSet<Character> set = new HashSet<>();
        int maxLength = 0;
        int left = 0;

        for(int right = 0; right < s.length(); right++) {
            if (set.size() == 0) {
                set.add(s.charAt(right));
                if(set.size() > maxLength) {
                    maxLength = set.size();
                }
                right++;
            }

            char currChar = s.charAt(right);
            if(!set.contains(currChar)) {
                set.add(currChar);
                if(set.size() > maxLength) {
                    maxLength = set.size();
                }
            } else {
                while(set.contains(currChar)) {
                    set.remove(s.charAt(left));
                    left++;
                }

                set.add(currChar);

                if(set.size() > maxLength) {
                    maxLength = set.size();
                }
            }

        }

        return maxLength;
    }
}
