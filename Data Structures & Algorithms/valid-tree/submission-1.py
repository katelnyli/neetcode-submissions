class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                q.append([neighbor, node])
            
        return len(visited) == n