file = open("data/data03.txt", "rt")

plane = {}
ids = {}

for l in file.readlines():
    l = l[:-1].split(' @ ')
    id = int(l[0][1:])
    l = l[1].strip()
    l = l.split(': ')
    l = [int(v) for v in l[0].split(',') + l[1].split('x')]
    (x, y, xw, yw) = tuple(l)
    ids[id] = (x, y, xw, yw)
    for i in range(xw):
        for j in range(yw):
            plane[(x+i,y+j)] = 1 + (0 if not (x+i,y+j) in plane else plane[(x+i,y+j)])

count = 0

for v in plane.values():
    if v > 1:
        count += 1

print("Part 1: {}".format(count))

for id in ids:
    found = True
    (x, y, xw, yw) = ids[id]
    for i in range(xw):
        for j in range(yw):
            if plane[(x+i,y+j)] > 1:
                found = False
                break
        if not found:
            break
    if found:
        print("Part 2: {}".format(id))
        break
