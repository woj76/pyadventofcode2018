#!/snap/bin/pypy3

import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(100000)

file = open("../data/data20.txt", "rt")
re = list(file.read().strip())

part2 = True

dirs = {'N' : (0,-1), 'S' : (0,1), 'E' : (1,0), 'W' : (-1,0) }

def dijkstra(G, startingNode):
	visited = set()
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heapq.heappush(pq, (0, startingNode))

	while pq:
		_, node = heapq.heappop(pq)
		visited.add(node)

		for adjNode in G[node]:
			if adjNode in visited:
				continue

			newCost = nodeCosts[node] + 1
			if nodeCosts[adjNode] > newCost:
				nodeCosts[adjNode] = newCost
				heapq.heappush(pq, (newCost, adjNode))

	return nodeCosts

class tree:
	def __init__(self,s,cs):
		self.node = s
		self.children = cs

	def max_len(self):
		if self.children == None:
			return 1, self.node
		else:
			max_len = float('-inf')
			for t in self.children:
				l, s = 0, ""
				for tt in t:
					ll, ss = tt.max_len()
					l += ll
					s += ss
				if l > max_len:
					max_len = l
					max_s = s
			return max_len, max_s

	def build_graph(self, g, pts):
		if self.children == None:
			npts = set()
			dx,dy = dirs[self.node]
			for x,y in pts:
				if (x,y) not in g:
					g[(x,y)] = set()
				if (x+dx,y+dy) not in g:
					g[(x+dx,y+dy)] = set()
				g[(x,y)].add((x+dx,y+dy))
				g[(x+dx,y+dy)].add((x,y))
				npts.add((x+dx,y+dy))
			return npts
		else:
			nnpts = set()
			for t in self.children:
				npts = pts
				for tt in t:
					npts = tt.build_graph(g, npts)
				nnpts |= npts
			return nnpts

def parse(tr,re, pos):
	if re[pos] in ['N','S','W','E']:
		tr.children[-1].append(tree(re[pos], None))
		pos = pos + 1
	elif re[pos] == '|':
		tr.children.append([])
		pos = pos + 1
	elif re[pos] == ')' or re[pos] == '$':
		return pos+1
	elif re[pos] == '(':
		ntr = tree(None, [[]])
		pos = parse(ntr, re, pos+1)
		tr.children[-1].append(ntr)
	return parse(tr, re, pos)

tr = tree(None, [[]])
parse(tr, re, 1)

def get_shortest(directions):
	path = []
	x,y = 0,0
	for d in directions:
		dx, dy = dirs[d]
		x += dx
		y += dy
		if (x,y) in path:
			path = path[0:path.index((x,y))+1]
		else:
			path.append((x,y))
	return len(path)

if part2:
	graph = {}
	tr.build_graph(graph, {(0,0)})
	r = 0
	for c in dijkstra(graph, (0,0)).values():
		if c >= 1000:
			r += 1
else:
	r = get_shortest(tr.max_len()[1])

print(f"Part {2 if part2 else 1}: {r}")
