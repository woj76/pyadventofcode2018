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

power_sums = [[0] * (grid_x+1) for _ in range(grid_y+1)]
for y in range(grid_y-1,-1,-1):
	for x in range(grid_x-1,-1,-1):
		power_sums[y][x] = cell_power(x+1, y+1) + power_sums[y+1][x] + power_sums[y][x+1] - power_sums[y+1][x+1]

max_power = float('-inf')

for s in (range(1, 301) if part2 else range(3, 4)):
	for y in range(grid_y - s + 1):
		for x in range(grid_x - s + 1):
			sub_power = power_sums[y][x] - power_sums[y+s][x] - power_sums[y][x+s] + power_sums[y+s][x+s]
			if sub_power > max_power:
				max_power = sub_power
				the_x, the_y, the_s = x+1, y+1, s

print(str(the_x)+","+str(the_y)+(","+str(the_s) if part2 else ""))
