class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency map
        preMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        output = []
        cycle = set()
        visited = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

            return True

        
        for crs in range(numCourses):
            if not dfs(crs): return []

        return output