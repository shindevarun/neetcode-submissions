class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # inDegreeMap = {}

        # for crs, pre in prerequisites:
        #     if crs not in inDegreeMap:
        #         inDegreeMap[crs] = 1
        #     else:
        #         inDegreeMap[crs] = inDegreeMap[crs] + 1

    
        # def bfs(noPreReqNodes):
        #     q = collections.deque()

        #     for node in noPreReqNodes:
        #         q.append(node)

        #     while q:
        #         currPre = q.popleft()
        #         courses = []

        #         for crs, pre in prerequisites:
        #             if pre == currPre:
        #                 courses.append(crs)

        #         for course in courses:
        #             inDegreeMap[crs] = inDegreeMap[crs] - 1

        #             if inDegreeMap[crs] == 0:
        #                 q.append(crs)
        #                 val = inDegreeMap.pop(crs)


        # noPreReqNodes = []
        # for crs, pre in prerequisites:
        #     if crs not in inDegreeMap:
        #         noPreReqNodes.append(crs)
        #     if pre not in inDegreeMap:
        #         noPreReqNodes.append(pre)

        # bfs(noPreReqNodes)

        # if not inDegreeMap:
        #     return True

        # return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq adjacency map
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True













