class Graph:
    def __init__(self, numNodes):
        self.nodes = []
        for i in range(numNodes):
            self.nodes.append(dict())

    def addNode(self):
        size = len(nodes)
        self.nodes.append(dict())
        return size

    def isNodeInvalid(self, nodeNum):
        if nodeNum < 0 or nodeNum > len(self.nodes) - 1:
            return True
        return False

    def addEdge(self, fromNode, toNode, weight):
        if self.isNodeInvalid(fromNode):
            raise ValueError('Node {} not present'.format(fromNode))
        if self.isNodeInvalid(toNode):
            raise ValueError('Node {} not present'.format(toNode))
        self.nodes[fromNode][toNode] = weight

    def getEgdeList(self, nodeNum):
        if self.isNodeInvalid(nodeNum):
            raise ValueError('Node {} not present'.format(nodeNum))
        return self.nodes[nodeNum]

    def findEdge(self, fromNode, toNode):
        if self.isNodeInvalid(fromNode):
            raise ValueError('Node {} not present'.format(fromNode))
        if self.isNodeInvalid(toNode):
            raise ValueError('Node {} not present'.format(toNode))
        return self.nodes[fromNode].get(toNode)


def main():
    graph1 = Graph(7)
    graph1.addEdge(0, 1, 1)
    graph1.addEdge(1, 2, 1)
    graph1.addEdge(2, 3, 1)
    graph1.addEdge(2, 4, 1)
    graph1.addEdge(3, 5, 1)
    graph1.addEdge(4, 6, 1)

    print('Get edge list of 2: ', graph1.getEgdeList(2))
    print('Get edge list of 4: ', graph1.getEgdeList(4))
    print('Find edge 3->5: ', graph1.findEdge(3, 5))
    print('Find edge 5->6: ', graph1.findEdge(5, 6))


if __name__ == '__main__':
    main()