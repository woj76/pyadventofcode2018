file = open("data/data06.txt", "rt")
data = [tuple([int(xy) for xy in l.split(',')]) for l in file.read().strip().split('\n')]
file.close()

part2 = True

x_min = min([xy[0] for xy in data])
x_max = max([xy[0] for xy in data])
y_min = min([xy[1] for xy in data])
y_max = max([xy[1] for xy in data])

data = [(nx-x_min,ny-y_min) for (nx,ny) in data]
x_max -= x_min - 1	
y_max -= y_min - 1

l = len(data)

grid = [ [-1] * x_max for y in range(y_max)]

for x in range(x_max):
	for y in range(y_max):
		distances = []
		for nx, ny in data:
			distances.append(abs(x-nx) + abs(y-ny))
		if part2:
			grid[y][x] = sum(distances)
		else:
			ds = sorted(distances)
			if ds[0] < ds[1]:
				grid[y][x] = distances.index(ds[0])
r = 0

if part2:
	for x in range(x_max):
		for y in range(y_max):
			if grid[y][x] < 10000:
				r += 1
else:
	areas = set(range(l))

	for x in range(x_max):
		areas -= {grid[0][x]} 
		areas -= {grid[y_max-1][x]} 

	for y in range(y_max):
		areas -= {grid[y][0]} 
		areas -= {grid[y][x_max-1]} 

	counts = [0] * l

	for x in range(x_max):
		for y in range(y_max):
			i = grid[y][x]
			if i in areas:
				counts[i] += 1

	r = max(counts)

print(r)
