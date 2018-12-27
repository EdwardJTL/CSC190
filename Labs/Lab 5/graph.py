class graph:
    def __init__(self):
        self.store = []

    def addVertex(self, n):
        if not isinstance(n, int):
            return -1
        if n < 1:
            return -1
        for i in range(0,n,1):
            self.store += [[]]
        return len(self.store)

    def addEdge(self, from_idx, to_idx, directed, weight):
        if not isinstance(directed, bool):
            return False
        if not (isinstance(from_idx, int) and isinstance(to_idx, int) and isinstance(weight, int)):
            return False
        if (from_idx < 0) or (to_idx < 0) or (weight == 0):
            return False
        length = len(self.store)
        if (from_idx >= length) or (to_idx >= length):
            return False
        for i in self.store[from_idx]:
            if i[0] == to_idx:
                return False
        if directed is False:
            for i in self.store[to_idx]:
                if i[0] == from_idx:
                    return False
            self.store[to_idx] += [[from_idx, weight]]
        self.store[from_idx] += [[to_idx, weight]]
        return True

    def traverse(self, start, typeBreadth):
        r_list = []
        if not ((isinstance(start, int) or start is None) and isinstance(typeBreadth, bool)):
            return r_list
        if not (start in range(0, len(self.store), 1) or start is None):
            return r_list
        found_list = [False for i in range(0, len(self.store), 1)]
        processed_list = [False for i in range(0, len(self.store), 1)]
        line = []
        temp_list = []
        if start is None:
            for i in range(0, len(self.store), 1):
                if found_list[i] is False:
                    line += [i]
                    found_list[i] = True
                while len(line) != 0:
                    if typeBreadth is True:
                    # Breadth First, Use Queue
                        node = line[0]
                        line = line[1:]
                    else:
                    # Depth First, Use Stack
                        node = line[-1]
                        line = line[:-1]
                    if processed_list[node] is False:
                        temp_list += [node]
                        processed_list[node] = True
                        child_unprocessed = False
                        for i in self.store[node]:
                            child = i[0]
                            if found_list[child] is False:
                                line += [child]
                                found_list[child] = True
                            if processed_list[child] is False:
                                child_unprocessed = True
                        if child_unprocessed == False:
                            r_list += [temp_list]
                            temp_list = []
        if isinstance(start, int):
            line += [start]
            while len(line) != 0:
                if typeBreadth is True:
                # Breadth First, Use Queue
                    node = line[0]
                    line = line[1:]
                else:
                # Depth First, Use Stack
                    node = line[-1]
                    line = line[:-1]
                if processed_list[node] is False:
                    r_list += [node]
                    processed_list[node] = True
                    for i in self.store[node]:
                        child = i[0]
                        if found_list[child] is False:
                            line += [child]
                            found_list[child] = True
        return r_list

    def connectivity(self, vx, vy):
        element = [False, False]
        if not (isinstance(vx, int) and isinstance(vy, int)):
            return element
        if not (vx in range(0, len(self.store), 1) and vy in range(0, len(self.store), 1)):
            return element
        vx_connected = self.traverse(vx, True)
        vy_connected = self.traverse(vy, True)
        if vy in vx_connected:
            element[0] = True
        if vx in vy_connected:
            element[1] = True
        return element

    def path(self,vx,vy):
        if not (isinstance(vx, int) and isinstance(vy, int)):
            return [[],[]]
        if not (vx in range(0, len(self.store), 1) and vy in range(0, len(self.store), 1)):
            return [[],[]]
        path_to = []
        path_back = []
        visited_list = [False] * len(self.store)
        path_to = self.path_helper(vx, vy, path_to, visited_list)
        visited_list = [False] * len(self.store)
        path_back = self.path_helper(vy, vx, path_back, visited_list)
        element = [path_to, path_back]
        return element

    def path_helper(self, from_idx, to_idx, path, visited_list):
        visited_list[from_idx] = True
        path.append(from_idx)
        if from_idx == to_idx:
            return path
        else:
            for i in self.store[from_idx]:
                successor_node = i[0]
                if visited_list[successor_node] is False:
                    path = self.path_helper(successor_node, to_idx, path, visited_list)
                    if to_idx in path:
                        return path
        path = path[:-1]
        visited_list[from_idx] = False
        return path
