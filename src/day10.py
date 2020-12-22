#!/snap/bin/pypy3

from time import sleep

file = open("../data/data10.txt", "rt")
data = [x for x in file.read().strip().split('\n')]
file.close()

part2 = False

x_min = y_min = float('inf')
x_max = y_max = float('-inf')

points = {}

for d in data:
	[_, p1, p2] = d.split('<')
	p1 = p1.strip().split('>')[0]
	p2 = p2[:-1]
	[px,py] = [int(x.strip()) for x in p1.split(',')]
	[vx,vy] = [int(x.strip()) for x in p2.split(',')]
	x_min = min(x_min, px)
	x_max = max(x_max, px)
	y_min = min(y_min, py)
	y_max = max(y_max, py)
	points[(px,py)] = (px,py,vx,vy)

iter = 1

while True:
	x_min = y_min = float('inf')
	x_max = y_max = float('-inf')
	for p, (px,py,vx,vy) in points.items():
		nx = px+vx
		ny = py+vy
		x_min = min(x_min, nx)
		x_max = max(x_max, nx)
		y_min = min(y_min, ny)
		y_max = max(y_max, ny)
		points[p] = (nx, ny, vx, vy)
		points[p] = (nx, ny, vx, vy)
	xw = x_max - x_min
	yw = y_max - y_min
	#print(iter, wx, wy)
	#if wx < 200 and wy < 100:
	#	sleep(2)
	if iter == 10932:
		xw = x_max - x_min
		yw = y_max - y_min
		plane = [['.'] * (xw+1) for y in range(yw+1)]
		for (px,py,vx,vy) in points.values():
			plane[py-y_min][px-x_min] = '#'
		r = "\n".join(["".join(r) for r in plane])
		break
	iter += 1

print("Part 1:")
print(r)
print("\nPart 2: ", iter)
