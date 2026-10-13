class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> map = new HashMap<>();

        for(String s : strs) {
            List<Integer> freq = new ArrayList<Integer>(Collections.nCopies(26, 0));

            for (int i = 0; i < s.length(); i++) {
                int index = s.charAt(i) - 'a';
                freq.set(index, freq.get(index) + 1);
            }

            if(!map.containsKey(freq)) {
                List<String> wordList = new ArrayList<>();
                wordList.add(s);
                map.put(freq, wordList);
            } else {
                List<String> wordList = map.get(freq);
                wordList.add(s);
                map.put(freq, wordList);
            }
        }

        List<List<String>> res = new ArrayList<>();
        for(List<Integer> key : map.keySet()) {
            res.add(map.get(key));
        }

        return res;
    }
}
