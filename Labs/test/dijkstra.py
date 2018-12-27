import stack as stack
import queue as queue


# adj is a list of [vertex,weight]
class graph:
    def __init__(self):
        self.adj = []

    def addVertex(self, n):
        for i in range(0, n):
            self.adj = self.adj + [[]]
        return len(self.adj)

    def addEdge(self, from_idx, to_idx, directed, weight):
        N = len(self.adj)
        if (from_idx >= N) or (to_idx >= N) or (weight == 0) or \
                ((directed != False) and (directed != True)):
            return False

        self.adj[from_idx] = self.adj[from_idx] + [[to_idx, weight]]

        if (directed == False):
            self.adj[to_idx] = self.adj[to_idx] + [[from_idx, weight]]

    def printEdges(self):
        print self.adj

    def traverse(self, start, typeB):
        if typeB == True:
            C = queue.queue()
        else:
            C = stack.stack()

        N = len(self.adj)
        Discovered = [False] * N
        Processed = [False] * N
        # print Discovered, Processed
        accum = []
        if start == None:
            Vertices = range(0, N)
        else:
            Vertices = [start]
        for i in Vertices:
            saccum = []
            if Discovered[i] == False:
                C.store(i)
                Discovered[i] = True
            while C.empty() == False:
                status, w = C.retrieve()
                # print w
                if Processed[w] == False:
                    saccum = saccum + [w]
                    Processed[w] = True
                # print self.adj[w]
                for x in sorted(self.adj[w]):
                    if Discovered[x[0]] == False:
                        # print x[0]
                        C.store(x[0])
                        Discovered[x[0]] = True
            if saccum != []:
                accum = accum + [saccum]
        if start == None:
            return accum
        else:
            return accum[0]

    def dijkstra(self, start):
        N = len(self.adj)

        L = range(0, N)
        dist = [-1] * N  # we'll call this infinity since -1 doesn't overlap legit values of dist
        prev = [-1] * N  # we'll call this undefined since -1 doesn't overlap legit values of vertex indices

        dist[start] = 0
        while len(L) != 0:
            # I: find minIdx \in L s.t. dist[minIdx] is minimized
            minDist = -1
            minIdx = -1
            for i in L:
                if dist[i] <> -1:
                    if (minDist == -1) or ((minDist <> -1) and (dist[i] < minDist)):
                        minDist = dist[i]
                        minIdx = i
            if minIdx == -1:
                return [False, dist, prev]

            # II: remove minIdx from L
            L.remove(minIdx)

            # III: for all neighbors,x, of minIdx that are in L
            #           if d < dist[minIdx]:
            #               update dist[x] = d
            #               update prev[x] = minIdx
            for x in sorted(self.adj[minIdx]):
                if x[0] in L:  # x[0] is the vertex
                    d = minDist + x[1]  # x[1] is the weight

                    if (dist[x[0]] == -1) or ((dist[x[0]] <> -1) and (d < dist[x[0]])):
                        dist[x[0]] = d
                        prev[x[0]] = minIdx
        return [True, dist, prev]


g = graph()
g.addVertex(7)
g.addEdge(0, 1, False, 7)
g.addEdge(0, 3, False, 9)
g.addEdge(0, 4, False, 3)
g.addEdge(1, 2, False, 10)
g.addEdge(2, 3, False, 1)
g.addEdge(3, 5, False, 1)
g.addEdge(4, 5, False, 2)
g.addEdge(2, 6, False, 13)
g.addEdge(5, 6, False, 10)
print g.dijkstra(0)