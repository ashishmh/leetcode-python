import sys
from collections import deque
from graph import *
import heapq


def bfs(graph, source):
	if graph is None:
		return
	if graph.isNodeInvalid(source):
		return

	d = [sys.maxsize] * len(graph.nodes)
	p = [None] * len(graph.nodes)
	output = []
	queue = deque()
	queue.append(source)
	d[source] = 0
	while queue:
		u = queue.popleft()
		for v, w in graph.getEgdeList(u).items():
			if d[v] > d[u] + w:
				d[v] = d[u] + w
				p[v] = u
				output.append(str(u) + '->' + str(v) + ': ' + str(w))
			queue.append(v)
	print('BFS: ', output)
	return (p, d, output)


def dfs(graph, source):
	if graph is None:
		return
	if graph.isNodeInvalid(source):
		return

	output = [] 										# for printing output of dfs
	numNodes = len(graph.nodes)
	p = [None] * numNodes 								# parent pointers
	visited = [False] * numNodes
	st, ft = [0] * numNodes, [0] * numNodes 			# starting and finishing times
	t = {'time': 0}
	if source is not None:
		dfsInner(graph, source, visited, p, st, ft, t, output)
	else:
		for i in range(numNodes):
			if visited[i] == False:
				dfsInner(graph, i, visited, p, st, ft, t, output)
	print('DFS: ', output)
	return (p, st, ft)


def dfsInner(graph, u, visited, p, st, ft, t, output):
	t['time'] += 1
	st[u] = t['time']
	for v, w in graph.getEgdeList(u).items():
		if visited[v] == False:
			p[v] = u
			output.append(str(u) + '->' + str(v) + ': ' + str(w))
			# t['time'] += 1
			dfsInner(graph, v, visited, p, st, ft, t, output)
	t['time'] += 1
	ft[u] = t['time']
	visited[u] = True



def main():
	graph1 = Graph(7)
	graph1.addEdge(0, 1, 1)
	graph1.addEdge(1, 2, 1)
	graph1.addEdge(2, 3, 1)
	graph1.addEdge(2, 4, 1)
	graph1.addEdge(3, 4, 1)
	graph1.addEdge(3, 5, 1)
	graph1.addEdge(4, 6, 1)

	# print('Get edge list of 2: ', graph1.getEgdeList(2))
	# print('Get edge list of 4: ', graph1.getEgdeList(4))
	# print('Find edge 3->5: ', graph1.findEdge(3, 5))
	# print('Find edge 5->6: ', graph1.findEdge(5, 6))
	print('\nBFS with source 2: ')
	bfs(graph1, 2)
	print('\nBFS with source 0: ')
	bfs(graph1, 0)
	print('\nDFS with source 0: ')
	_, st, ft = dfs(graph1, 0)
	for i in range(len(st)):
		print('node {}: st = {}, ft = {}'.format(i, st[i], ft[i]))
	print('\nDFS with source 2: ')
	dfs(graph1, 2)


if __name__ == '__main__':
    main()