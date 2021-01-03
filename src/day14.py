#!/snap/bin/pypy3

part2 = True

if part2:
	input = "110201"
else:
	input = 110201

elf_1, elf_2 = 0, 1

recepies = [3,7]

if part2:
	while True:
		recepies.extend([int(x) for x in list(str(recepies[elf_1] + recepies[elf_2]))])
		elf_1 = (elf_1 + recepies[elf_1] + 1) % len(recepies)
		elf_2 = (elf_2 + recepies[elf_2] + 1) % len(recepies)
		if len(recepies) < len(input)+1:
			continue
		last = recepies[-len(input)-1:]
		s = "".join([str(x) for x in last])
		if input in s:
			print(len(recepies) - len(input) + s.index(input) - 1)
			break
else:
	while len(recepies) < input + 10:
		recepies.extend([int(x) for x in list(str(recepies[elf_1] + recepies[elf_2]))])
		elf_1 = (elf_1 + recepies[elf_1] + 1) % len(recepies)
		elf_2 = (elf_2 + recepies[elf_2] + 1) % len(recepies)
	print("".join([str(x) for x in recepies[input:input+10]]))
