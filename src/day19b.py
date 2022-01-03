#!/snap/bin/pypy3

part2 = True

target = 10551282 if part2 else 882

r = 0

for n in range(1, target//2+1):
	if target % n == 0:
		r += n

r+=target

print(r)