class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        from collections import deque

        adjlist = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        queue = deque()
        result = []

        for u,v in prerequisites:
            adjlist[v].append(u)
            indegree[u]+=1

        for i in range(0,numCourses):
            if indegree[i]==0:
                queue.append(i)

        while len(queue) != 0:

            current_node = queue.popleft()
            result.append(current_node)

            for adjnode in adjlist[current_node]:
                indegree[adjnode] -= 1
                if indegree[adjnode] == 0:
                    queue.append(adjnode)

        if len(result) == numCourses:
            return result
        return []
