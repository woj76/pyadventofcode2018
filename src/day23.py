#!/snap/bin/pypy3

with open("../data/data23.txt", "rt") as file:
	data = [d[5:] for d in file.read().strip().split('\n') if d != '']

for i in range(len(data)):
	d = data[i].split('>, r=')
	data[i] = tuple([int(d[1])]+[int(x) for x in d[0].split(',')])

part2 = True

if part2:
	max_count = float('-inf')
	min_x, min_y, min_y = None, None, None
	max_ints = None
	for i in range(len(data)):
		ri, xi, yi, zi = data[i]
		xi, yi, zi = xi-ri, yi-ri, zi-ri
		ints = [i]
		for j in range(i+1,len(data)):
			rri, xxi, yyi, zzi = data[j]
			ok = True
			for k in ints:
				rrri, xxxi, yyyi, zzzi = data[k]
				if abs(xxi-xxxi)+abs(yyi-yyyi)+abs(zzi-zzzi) > rri+rrri:
					ok = False
					break
			if ok:
				xi = min(xi, xxi-rri)
				yi = min(yi, yyi-rri)
				zi = min(zi, zzi-rri)
				ints.append(j)
		if len(ints) > max_count:
			max_count = len(ints)
			max_ints = ints
			min_x, min_y, min_z = xi, yi, zi
	res=min_x+min_y+min_z
	while True:
		ok = True
		for i in max_ints:
			rr,xx,yy,zz = data[i]
			if abs(xx)+abs(yy)+abs(zz) > rr+res:
				ok = False
				break
		if ok:
			break
		res += 1
else:
	data.sort()
	data.reverse()
	r, x, y, z = data[0]
	res = 0
	for _, ox, oy, oz in data:
		if abs(ox-x) + abs(oy-y) + abs(oz-z) <= r:
			res += 1

print(f"Part {2 if part2 else 1}: {res}")
