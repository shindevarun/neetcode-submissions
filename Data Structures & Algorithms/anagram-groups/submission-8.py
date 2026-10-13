class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # myMap = {}

        # for s in strs:
        #     curr = ''.join(sorted(s))
            
        #     if myMap.get(curr) is None:
        #         myMap[curr] = [s]
        #     else:
        #         myMap[curr].append(s)

        
        # res =[]

        # for lst in myMap.values():
        #     res.append(lst)

        # return res

        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)

        res = []
        for grouped_words in anagrams.values():
            res.append(grouped_words)

        return res


            