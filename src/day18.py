#!/snap/bin/pypy3

file = open("../data/data18.txt", "rt")

data = [list(x) for x in file.read().strip().split('\n') if x != '']

part2 = True

def n(x,y,d):
	l = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
	return [(x,y) for x,y in l if 0<=x<len(d[0]) and 0<=y<len(d)]

target = 1000000000 if part2 else 10

prevs = {}
prevs2 = []

for index in range(target):
	ss = "".join(["".join(d) for d in data])
	if ss in prevs:
		break
	prevs[ss] = index
	prevs2.append(ss)
	new_data = [[' ']*len(data[0]) for y in range(len(data))]
	for y in range(len(data)):
		for x in range(len(data[0])):
			ns = [data[j][i] for i,j in n(x,y,data)]
			if data[y][x] == '.':
				if ns.count('|') >= 3:
					new_data[y][x] = '|'
				else:
					new_data[y][x] = '.'
			elif data[y][x] == '|':
				if ns.count('#') >= 3:
					new_data[y][x] = '#'
				else:
					new_data[y][x] = '|'
			elif data[y][x] == '#':
				if ns.count('#') >= 1 and ns.count('|') >= 1:
					new_data[y][x] = '#'
				else:
					new_data[y][x] = '.'
	data = new_data

if part2:
	s = prevs2[prevs[ss] + (target - prevs[ss]) % (index - prevs[ss])]
else:
	s = "".join(["".join(d) for d in data])

wood = 0
lumber = 0
for c in s:
	if c == '|':
		wood += 1
	elif c == '#':
		lumber += 1
r = lumber * wood

print(f"Part {2 if part2 else 1}: {r}")
