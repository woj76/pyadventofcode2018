#!/snap/bin/pypy3

with open("../data/data13.txt", "rt") as file:
	data = [list(x) for x in file.read().split('\n') if x != ""]

part2 = True

y_max = len(data)
x_max = len(data[0])

carts = []

for y in range(y_max):
	for x in range(x_max):
		if data[y][x] == '>':
			carts.append((y,x,1,0,True))
			data[y][x] = '-'
		elif data[y][x] == '<':
			carts.append((y,x,3,0,True))
			data[y][x] = '-'
		elif data[y][x] == '^':
			carts.append((y,x,0,0,True))
			data[y][x] = '|'
		elif data[y][x] == 'v':
			carts.append((y,x,2,0,True))
			data[y][x] = '|'

stop = False

while not stop:
	carts.sort()
	for i in range(len(carts)):
		c = carts[i]
		y, x, d, t, a = c
		if not a:
			continue
		if d == 0:
			y -= 1
			if data[y][x] == '\\':
				d = 3
			elif data[y][x] == '/':
				d = 1
		elif d == 1:
			x += 1
			if data[y][x] == '/':
				d = 0
			elif data[y][x] == '\\':
				d = 2
		elif d == 2:
			y += 1
			if data[y][x] == '/':
				d = 3
			elif data[y][x] == '\\':
				d = 1
		elif d == 3:
			x -= 1
			if data[y][x] == '/':
				d = 2
			elif data[y][x] == '\\':
				d = 0
		if data[y][x] == '+':
			d = (d + t - 1) % 4
			t = (t + 1) % 3
		colliding = [j for j in range(len(carts)) if j != i and carts[j][0] == y and carts[j][1] == x]
		if colliding:
			if not part2:
				r = str(x)+","+str(y)
				stop = True
				i = len(carts)
			else:
				for j in colliding:
					carts[j] = (0,0,0,0,False)
				carts[i] = (0,0,0,0,False)
		else:
			carts[i] = (y,x,d,t,a)
	if part2:
		active_carts = [c for c in carts if c[4]]
		if len(active_carts) == 1:
			r = str(active_carts[0][1])+","+str(active_carts[0][0])
			stop = True

print(r)
