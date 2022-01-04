#!/snap/bin/pypy3

# from collections import deque

with open("../data/data21.txt", "rt") as file:
	data = [d for d in file.read().strip().split('\n') if d != '']
	ip_reg = int(data[0][4])
	data = data[1:]

for i,d in enumerate(data):
	d = d.split(' ')
	for j in [1, 2, 3]:
		d[j] = int(d[j])
	data[i] = [d[0],d[1],d[2],d[3]]

part2 = True

r4s = []

def execute(regs, line):
	opcode = line[0]
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
		if opcode == "eqrr":
			if part2:
				if p1 in r4s:
					regs[0] = r4s[-1]
					p2 = regs[0]
				else:
					r4s.append(p1)
			else:
				regs[0] = p1
				p2 = regs[0]
		r = 1 if p1 == p2 else 0
	regs[line[3]] = r
	return regs

registers = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

ip = 0
while ip < len(data):
	d = data[ip]
	registers[ip_reg] = ip
	registers = execute(registers, d)
	ip = registers[ip_reg]
	ip += 1

print(f"Part {2 if part2 else 1}: {registers[0]}")
