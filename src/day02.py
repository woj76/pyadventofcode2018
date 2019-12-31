file = open("data/data02.txt", "rt")

lists = []

for line in [l[:-1] for l in file.readlines()]:
    lists.append([c for c in line])

counts = []

for l in lists:
    count = set()
    for c in range(ord('a'), ord('z')+1):
        count.add(l.count(chr(c)))
    counts.append(count)

twos = threes = 0

for s in counts:
    if 2 in s:
        twos += 1
    if 3 in s:
        threes += 1

print("Part 1: {}".format(twos * threes))

for (l1, l2) in [(l1, l2) for l1 in lists for l2 in lists if lists.index(l1) < lists.index(l2)]:
    zl = zip(l1, l2)
    r = [c1 for (c1,c2) in zip(l1, l2) if c1 == c2]
    if len(r) == len(l1) - 1:
        print("Part 2: {}".format(''.join(r)))
        break
