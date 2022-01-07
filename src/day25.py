#!/snap/bin/pypy3

with open("../data/data25.txt", "rt") as file:
	data = [[tuple([int(y) for y in x.split(',')])] for x in file.read().strip().split('\n')]

while True:
	changed = False
	for i,c1 in enumerate(data):
		for j in range(i+1, len(data)):
			c2 = data[j]
			for t1 in c1:
				for t2 in c2:
					if abs(t1[0]-t2[0]) + abs(t1[1]-t2[1]) + abs(t1[2]-t2[2]) + abs(t1[3]-t2[3]) <= 3:
						changed = True
						break
				if changed:
					break
			if changed:
				break
		if changed:
			break
	if not changed:
		break
	else:
		data[i] = data[i]+data[j]
		del data[j]

res = len(data)

print(f"Part 1: {res}")
