#!/snap/bin/pypy3

# from collections import defaultdict

with open("../data/data17.txt", "rt") as file:
	data = file.read().strip().split('\n')

part2 = True

min_y, max_y = float('inf'), float('-inf')
min_x, max_x = float('inf'), float('-inf')

for d in data:
	d = d.split(', ')
	x=int(d[0][2:])
	[ys1,ys2]=[int(x) for x in d[1][2:].split('..')]
	for y in range(ys1,ys2+1):
		if d[0][0] == 'x':
			xx,yy = x,y
		else:
			xx,yy = y,x
		min_x = min(xx,min_x)
		max_x = max(xx,max_x)
		min_y = min(yy, min_y)
		max_y = max(yy, max_y)


plane = [['.']*(max_x-min_x+2) for _ in range(0,max_y+3)]

for d in data:
	d = d.split(', ')
	x=int(d[0][2:])
	[ys1,ys2]=[int(x) for x in d[1][2:].split('..')]
	for y in range(ys1,ys2+1):
		if d[0][0] == 'x':
			xx,yy = x,y
		else:
			xx,yy = y,x
		plane[yy][xx-min_x-1] = '#'


sources = [(500,0)]
# plane[sources[0]] = '+'

while sources:
	sx,sy = sources.pop()
	while (plane[sy+1][sx-min_x+1] == '.' or  plane[sy+1][sx-min_x+1] == '|') and sy <= max_y:
		if sy != 0:
			plane[sy][sx-min_x+1] = '|'
		sy += 1
	if sy == max_y+1:
		continue
	lefts = []
	i = 0
	while plane[sy][sx-i-min_x+1] != '#' and (plane[sy+1][sx-i-min_x+1] == '#'  or plane[sy+1][sx-i-min_x+1] == '~'):
		lefts.append((sx-i,sy))
		i += 1
	left_block = plane[sy][sx-i-min_x+1] == '#'
	left_source = (sx-i,sy)
	rights = []
	i = 0
	while plane[sy][sx+i-min_x+1] != '#' and (plane[sy+1][sx+i-min_x+1] == '#'  or plane[sy+1][sx+i-min_x+1] == '~'):
		rights.append((sx+i,sy))
		i += 1
	right_block = plane[sy][sx+i-min_x+1] == '#'
	right_source = (sx+i,sy)
	if left_block and right_block:
		for xx,yy in lefts+rights:
			plane[yy][xx-min_x+1] = '~'
		sy -= 1
		sources.append((sx,sy))
	else:
		for xx,yy in lefts:
			plane[yy][xx-min_x+1] = '|'
		for xx,yy in rights:
			plane[yy][xx-min_x+1] = '|'
		if not left_block:
			sources.append(left_source)
		if not right_block:
			sources.append(right_source)

r = 0
for y in range(min_y,max_y+1):
	for x in range(min_x-2,max_x+1):
		c = plane[y][x-min_x+1]
		if c == '~' or (c == '|' and not part2):
			r += 1
		#print(c,end='')
	#print()


print(f"Part {2 if part2 else 1}:", r)
