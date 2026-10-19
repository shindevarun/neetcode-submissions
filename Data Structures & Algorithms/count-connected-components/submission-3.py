class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # undirected adjacency map
        adj = {i:[] for i in range(n)}
        for edge in edges:
            src, des = edge[0], edge[1]
            adj[src].append(des)
            adj[des].append(src)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components