#!/snap/bin/pypy3

from collections import deque

with open("../data/data15.txt", "rt") as file:
	data = [list(x) for x in file.read().split('\n') if x != ""]

part2 = True

y_max = len(data)
x_max = len(data[0])

def collect_units(e = ['E', 'G']):
	r = []
	for y in range(y_max):
		for x in range(x_max):
			if game[y][x] in e:
				r.append((y,x))
	return r

def neighbours(y, x, e = '.'):
	return [(py, px) for py, px in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)] if game[py][px] == e]

def get_dist(d, y, x):
	if (y, x) in d:
		return d[(y,x)]
	return float('inf')

num_elves = sum([r.count('E') for r in data])
elves_attack_power = 3

while True:
	game = [row[:] for row in data]

	hit_points = {}
	for uy, ux in collect_units():
		hit_points[(uy,ux)] = 200

	rounds = 0
	combat_end = False

	while not combat_end:
		for uy, ux in collect_units():
			if game[uy][ux] not in ['G', 'E']:
				continue
			enemy = 'G' if game[uy][ux] == 'E' else 'E'
			if not collect_units([enemy]):
				combat_end = True
				break
			if not neighbours(uy,ux, enemy):
				in_range = []
				for ey,ex in collect_units([enemy]):
					in_range.extend(neighbours(ey,ex))
				dist = {}
				prev = {}
				q = deque()
				q.append((uy,ux))
				dist[(uy,ux)] = 0
				while len(q) > 0:
					wy, wx = q.popleft()
					for vy,vx in neighbours(wy,wx):
						alt = get_dist(dist, wy, wx) + 1
						if alt < get_dist(dist, vy, vx):
							dist[(vy,vx)] = alt
							prev[(vy,vx)] = (wy,wx)
							q.append((vy,vx))
				for p in [p for p in dist.keys() if p not in in_range]:
					del dist[p]
				if dist:
					min_dist = float('inf')
					for d in dist:
						if dist[d] < min_dist:
							min_dist = dist[d]
							my, mx = d
					while prev[(my,mx)] != (uy,ux):
						my, mx = prev[(my,mx)]
					hit_points[(my,mx)] = hit_points[(uy,ux)]
					del hit_points[(uy,ux)]
					game[my][mx] = game[uy][ux]
					game[uy][ux] = '.'
					uy,ux = my,mx
			attack = neighbours(uy,ux, enemy)
			if attack:
				min_attack = float('inf')
				for ay, ax in attack:
					if hit_points[(ay,ax)] < min_attack:
						min_attack = hit_points[(ay,ax)]
						pay, pax = ay, ax
				hit_points[(pay, pax)] -= (3 if enemy == 'E' else elves_attack_power)
				if hit_points[(pay, pax)] <= 0:
					del hit_points[(pay, pax)]
					game[pay][pax] = '.'
		if not combat_end:
			rounds += 1
	if not part2 or sum([r.count('E') for r in game]) == num_elves:
		break
	elves_attack_power += 1

print(rounds * sum(hit_points.values()))
