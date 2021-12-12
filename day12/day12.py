import pydash as _

with open("day12/input.txt") as file:
    edges = file.read().splitlines()

for i in range(len(edges)):
    edges[i] = edges[i].split("-")

class Graph:
    edges = []
    def add_edge(self, edge):
        self.edges.append(edge)
    def getNeighborNodes(self, node):
        neighbors = []
        for edge in self.edges:
            if edge[0] == node:
                neighbors.append(edge[1])
            elif edge[1] == node:
                neighbors.append(edge[0])
        return neighbors

    def getStartEdges(self):
        startEdges = []
        for edge in self.edges:
            if edge[0] == "start" or edge[1] == "start":
                startEdges.append(edge)
        return startEdges

def extendPath(path, graph):
    originalPath = path.copy()
    for neighborNode in graph.getNeighborNodes(originalPath[-1]):
        if neighborNode == "start":
            continue
        elif neighborNode == "end":
            newPath = path.copy()
            newPath.append(neighborNode)
            print(newPath)
            allPaths.append(newPath)
            continue

        elif neighborNode.isupper():
            newPath = path.copy()
            newPath.append(neighborNode)
            extendPath(newPath, graph)
        elif neighborNode.islower():
            if neighborNode not in path:
                newPath = path.copy()
                newPath.append(neighborNode)
                extendPath(newPath, graph)
            else:
                space = True
                for node in path:
                    if node.islower() and path.count(node) > 1:
                        space = False

                if space:
                    newPath = path.copy()
                    newPath.append(neighborNode)
                    extendPath(newPath, graph)
                else:
                    continue

graph = Graph()
for edge in edges:
    graph.add_edge(edge)

allPaths = []
for startEdge in graph.getStartEdges():
    currPath = []
    currPath.append(startEdge[0])
    currPath.append(startEdge[1])
    extendPath(currPath, graph)

print(len(allPaths))