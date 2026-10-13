class Solution {
    public int lengthOfLongestSubstring(String s) {

        // done using sliding window algorithm. have left and right pointers. right will add chars to
        // a hashset and keep track of all unique chars. at every iteration of right, chceck if that 
        // char already exists in the set, if it does you have to incrmenet the left side of the window
        // until that charAt(left) is no longer in the set (shrink and/or move window forward) before adding
        // in charAt(right). Anytime you add char into set, compare with max length to keep track of max length
    
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
            }

        }

        return maxLength;
    }
}
