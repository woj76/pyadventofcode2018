#!/snap/bin/pypy3

with open("../data/data12.txt", "rt") as file:
	[init_state, trans] = file.read().strip().split('\n\n')

part2 = True

steps = 100 if part2 else 20

init_state = "."*60*steps+init_state[15:]+"."*60*steps

patterns = {}

for t in trans.split('\n'):
	[p,r] = t.split(" => ")
	patterns[p] = r

prev_r = 0
for j in range(steps):
	new_state = ["."] * len(init_state)
	for i in range(2, len(new_state)-2):
		k = init_state[i-2:i+3]
		if k in patterns:
			new_state[i] = patterns[k]
	init_state = "".join(new_state)
	r = 0
	for i, v in enumerate(init_state):
		if v == '#':
			r += (i-60*steps)
	diff = r - prev_r
	prev_r = r

if part2:
	r += (50000000000-steps)*diff

print(r)
