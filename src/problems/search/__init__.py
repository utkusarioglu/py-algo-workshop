class Search:
    def bfs(self, node_list: list[list[int]], count: int, start: int) -> list[int]:
        node_map = {i: [] for i in range(count + 1)}
        for [source, sink] in node_list:
            pairs = node_map.get(source)
            if sink not in pairs:
                pairs.append(sink)

        def bfs(node: int):
            if node in visited:
                return
            visited.add(node)
            queue.pop(0)
            stack.append(node)
            for pair in node_map.get(node):
                if pair not in visited:
                    queue.append(pair)

        visited = set()
        stack = []
        queue = [0]
        while queue:
            bfs(queue[0])

        return stack

    def dfs(self, node_list: list[list[int]], count: int, start: int) -> list[int]:
        node_map = {i: [] for i in range(count + 1)}
        for [source, sink] in node_list:
            pairs = node_map.get(source)
            if sink not in pairs:
                pairs.append(sink)

        print(node_map)
        visited = set()
        stack = []
        queue = []
        stack = [start]

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            queue.append(node)
            for pair in node_map.get(node):
                stack.append(pair)

        while stack:
            dfs(stack.pop(0))

        return queue
