#!/snap/bin/pypy3

from collections import deque

with open("../data/data16.txt", "rt") as file:
	[samples,program] = file.read().strip().split('\n\n\n\n')
	samples = [s.split('\n') for s in samples.strip().split('\n\n')]
	program = [[int(x) for x in p.split(' ')] for p in program.strip().split('\n')]

part2 = True

for i,s in enumerate(samples):
	[b,ins,a] = s
	b,a = eval(b[8:]),eval(a[8:])
	ins = [int(i) for i in ins.split(' ')]
	samples[i] = (b, ins, a)


def execute(regs, line, octable, opcode = None):
	if opcode == None:
		opcode = octable[line[0]]
	r = None
	p1, p2 = line[1], line[2]
	if opcode[:3] == "add":
		p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = p1 + p2
	elif opcode[:3] == "mul":
		p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = p1 * p2
	elif opcode[:3] == "ban":
		p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = p1 & p2
	elif opcode[:3] == "bor":
		p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = p1 | p2
	elif opcode[:3] == 'set':
		if opcode[3] == 'r':
			p1 = regs[p1]
		r = p1
	elif opcode[:2] == 'gt':
		if opcode[2] == 'r':
			p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = 1 if p1 > p2 else 0
	elif opcode[:2] == 'eq':
		if opcode[2] == 'r':
			p1 = regs[p1]
		if opcode[3] == 'r':
			p2 = regs[p2]
		r = 1 if p1 == p2 else 0
	else:
		print(opcode)
	regs[line[3]] = r
	return regs


opcodes_table = {}

opcode_list = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

part1 = 0

for (b, ins, a) in samples:
	r = 0
	for opcode in opcode_list:
		if execute(b[:], ins, {}, opcode) == a:
			r += 1
			oc = ins[0]
			if oc in opcodes_table:
				if opcode not in opcodes_table[oc]:
					opcodes_table[oc].append(opcode)
			else:
				opcodes_table[oc] = [opcode]
	if r >= 3:
		part1 += 1

print("Part 1:", part1)

while sum([1 if len(o) > 1 else 0 for o in opcodes_table.values()]) > 0:
	for oc in opcodes_table.keys():
		v = opcodes_table[oc]
		if len(v) == 1:
			v = v[0]
			for oc2 in opcodes_table.keys():
				if oc2 == oc:
					continue
				elif v in opcodes_table[oc2]:
					opcodes_table[oc2].remove(v)

for k in opcodes_table:
	opcodes_table[k] = opcodes_table[k][0]

regs = [0, 0, 0, 0]
for p in program:
	execute(regs, p, opcodes_table)

print("Part 2:", regs[0])
