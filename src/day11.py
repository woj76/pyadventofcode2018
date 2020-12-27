#!/snap/bin/pypy3

serial_id = 9798

part2 = True
grid_x = grid_y = 300

def cell_power(x,y):
	rack_id = x + 10
	pw = rack_id * y + serial_id
	pw = pw * rack_id
	pw = (pw % 1000) // 100
	return pw - 5

power_grid = [[0] * grid_x for _ in range(grid_y)]

for y in range(grid_y):
	for x in range(grid_x):
		power_grid[y][x] = cell_power(x+1, y+1)

# This makes both parts run more or less the same time,
# brute force (below) makes part 1 much quicker. Moreover,
# calculating power_sums can be made faster by going in
# reverse, or even by trying to exploit the cell_power
power_sums = [[0] * (grid_x+1) for _ in range(grid_y+1)]

for y in range(grid_y):
	for x in range(grid_x):
		sum = 0
		for i in range(grid_x-x):
			for j in range(grid_y-y):
				sum += power_grid[y+j][x+i]
		power_sums[y][x] = sum

max_power = float('-inf')

for s in (range(1, 301) if part2 else range(3, 4)):
	for y in range(grid_y - s + 1):
		for x in range(grid_x - s + 1):
			sub_power = power_sums[y][x] - power_sums[y+s][x] - power_sums[y][x+s] + power_sums[y+s][x+s]
#			sub_power = 0
#			for i in range(s):
#				for j in range(s):
#					sub_power += power_grid[y+j][x+i]
			if sub_power > max_power:
				max_power = sub_power
				the_x, the_y, the_s = x+1, y+1, s

print(str(the_x)+","+str(the_y)+(","+str(the_s) if part2 else ""))
