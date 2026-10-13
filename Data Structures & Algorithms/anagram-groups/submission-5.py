class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for s in strs:
            curr = ''.join(sorted(s))
            
            if myMap.get(curr) is None:
                myMap[curr] = [s]
            else:
                myMap[curr].append(s)

        
        res =[]

        for lst in myMap.values():
            res.append(lst)

        return res
            