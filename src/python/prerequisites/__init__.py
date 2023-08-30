class Prerequisites:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pres = {i: [] for i in range(numCourses)}
        for [course, pre] in prerequisites:
            pres[course].append(pre)
        stack = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in pres.get(course):
                if dfs(pre) is False:
                    return False
            cycle.remove(course)
            visited.add(course)
            stack.append(course)
            return True

        for course in range(numCourses - 1, -1, -1):
        # for course in range(numCourses):
            if dfs(course) is False:
                return []
        return stack
