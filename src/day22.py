#!/snap/bin/pypy3

from collections import defaultdict
from heapq import heappush, heappop

part2 = True

depth = 4845
tx,ty = 6,770

cave = {}

def get_cave_xy(x,y):
	if (x,y) in cave:
		return cave[(x,y)]
	if x < 0 or y < 0:
		return None
	if (x,y) == (0,0) or (x,y) == (tx,ty):
		geologic_index = 0
	else:
		if y == 0:
			geologic_index = 16807 * x
		elif x == 0:
			geologic_index = 48271 * y
		else:
			geologic_index = get_cave_xy(x-1,y)*get_cave_xy(x,y-1)
	cave[(x,y)] = (geologic_index+depth) % 20183
	return cave[(x,y)]

for x in range(tx+1):
	for y in range(ty+1):
		get_cave_xy(x,y)

# This could be cleverly colapsed, a bit too lazy :/
def get_cost_equipment(src_equipment, src_type, target_type):
	# return  cost, target_equipment
	if src_type == target_type:
		return 1, src_equipment
	if target_type == 4:	# special, end destination
		if src_type == 1:
			return 15, 2
		if src_type == 0:
			if src_equipment == 2:
				return 1, src_equipment
			if src_equipment == 1:
				return 8, 2
			assert False
		if src_type == 2:
			if src_equipment == 2:
				return 1, src_equipment
			if src_equipment == 0:
				return 8, 2
			assert False
		assert False
	if src_type == 0:
		if target_type == 1:
			if src_equipment == 1:
				return 1, src_equipment
			if src_equipment == 2:
				return 8, 1
			assert False
		if target_type == 2:
			if src_equipment == 2:
				return 1, src_equipment
			if src_equipment == 1:
				return 8, 2
			assert False
		assert False
	if src_type == 1:
		if target_type == 0:
			if src_equipment == 1:
				return 1, src_equipment
			if src_equipment == 0:
				return 8, 1
			assert False
		if target_type == 2:
			if src_equipment == 0:
				return 1, src_equipment
			if src_equipment == 1:
				return 8, 0
			assert False
		assert False
	if src_type == 2:
		if target_type == 0:
			if src_equipment == 2:
				return 1, src_equipment
			if src_equipment == 0:
				return 8, 2
			assert False
		if target_type == 1:
			if src_equipment == 0:
				return 1, src_equipment
			if src_equipment == 2:
				return 8, 0
			assert False
		assert False
	assert False

def get_neighbours(se, sx, sy):
	ns = [(sx-1,sy),(sx+1,sy),(sx,sy-1),(sx,sy+1)]
	st = get_cave_xy(sx,sy) % 3
	r = []
	for ttx,tty in ns:
		tt = get_cave_xy(ttx,tty)
		if tt == None:
			continue
		tt = 4 if ttx == tx and tty == ty else tt % 3
		c, te = get_cost_equipment(se, st, tt)
		r.append((c, te, ttx, tty))
	return r

def dijkstra():
	visited = set()
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[(2,0,0)] = 0
	heappush(pq, (0, 2, 0, 0))

	while pq:
		_, ne, nx, ny = heappop(pq)
		visited.add((ne,nx,ny))
		if (2,tx,ty) == (ne,nx,ny):
			break

		for cost, nne, nnx, nny in get_neighbours(ne,nx,ny):
			if (nne,nnx,nny) in visited:
				continue

			newCost = nodeCosts[(ne,nx,ny)] + cost
			if nodeCosts[(nne,nnx,nny)] > newCost:
				nodeCosts[(nne,nnx,nny)] = newCost
				heappush(pq, (newCost, nne, nnx, nny))

	return nodeCosts[(2,tx,ty)]

if part2:
	r = dijkstra()
else:
	r = sum([e % 3 for e in cave.values()])

print(f"Part {2 if part2 else 1}: {r}")
