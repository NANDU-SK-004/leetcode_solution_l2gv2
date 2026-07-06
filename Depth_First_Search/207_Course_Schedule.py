class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque ,defaultdict

        storage = defaultdict(list)
        indegree=[0]*numCourses

        for courses ,pre in prerequisites :
            storage[pre].append(courses)
            indegree[courses]+=1

        queue =deque([i for i in range(numCourses) if indegree[i] == 0])
        visited_course =0
        while queue:
            course =queue.popleft()
            visited_course +=1
            for i in storage[course]:
                indegree[i] -=1
                if indegree[i] ==0:
                    queue.append(i)

        return visited_course == numCourses