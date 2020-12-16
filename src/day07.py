#!/usr/bin/python3

file = open("../data/data07.txt", "rt")
data = [tuple([x for x in l.split(' ') if len(x) == 1]) for l in file.read().strip().split('\n')]
file.close()

part2 = True

letters = set()
for x, y in data:
	letters |= {x, y}

total_workers = 4 if part2 else 1

deps = {}
for b, c in data:
	if c in deps.keys():
		deps[c].append(b)
		deps[c].sort()
	else:
		deps[c] = [b]

start = {}
for c in letters:
	if c not in deps.keys():
		start[c] = ord(c) - ord('A') + 61 if part2 else 1

result = []
time = -1
working = []

while len(start) > 0:
	for w in working:
		start[w] -= 1
	firsts = [c for c,t in start.items() if c in working and t == 0]
	for first in firsts:
		del start[first]
		working.remove(first)
		result.append(first)
		to_remove = []
		for c in deps.keys():
			if not c in start.keys() and not c in result and deps[c] == sorted([x for x in deps[c] if x in result]):
				start[c] = ord(c) - ord('A') + 61 if part2 else 1
				to_remove.append(c)
		for c in to_remove:
			del deps[c]
	l = sorted(list(start.keys()))
	while len(working) < total_workers and l != []:
		if not l[0] in working:
			working.append(l[0])
		l = l[1:]
	time += 1

if part2:
	print(time)
else:
	print("".join(result))
