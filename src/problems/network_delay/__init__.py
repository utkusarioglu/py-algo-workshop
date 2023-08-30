class NetworkDelay:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        @dev
        k is the start point
        n is the number of nodes
        """
        unvisited = set(range(n + 1))
        edges = {i: [] for i in range(n + 1)}
        distances = {i: float("inf") for i in range(n + 1)}

        for [source, target, distance] in times:
            edges[source].append((target, distance))

        # unvisited.discard(k)
        distances[k] = 0
        print(unvisited)

        def findMinNode():
            min_key = None
            min_distance = float("inf")
            for key, distance in distances.items():
                if not min_key:
                    min_key = key
                    min_distance = distance
                if key in unvisited and distance < min_distance:
                    min_key = key
                    min_distance = distance
            return min_key

        iter = 0
        while unvisited and iter < 20:
            iter += 1
            curr = findMinNode()
            if not curr:
                print("not curr")
                continue
            unvisited.discard(curr)
            distances[curr] = iter
            # neighbors = edges.get(curr)
            # curr_dist = distances.get(curr)
            # if not neighbors:
            #     print("no neighbors")
            #     continue
            # for neighbor in neighbors:
            #     new_distance = neighbor[1] + curr_dist
            #     if new_distance < distances.get(neighbor[0]):
            #         distances[neighbor[0]] = new_distance
            # print(curr, neighbors, curr_dist, unvisited)

        print(unvisited)
        print(distances)

        if len(unvisited):
            return -1
        return max(distances.values())
