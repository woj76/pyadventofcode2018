file = open("data/data01.txt", "rt")

deltas = [int(d) for d in file.readlines()]

print("Part 1: {}".format(sum(deltas)))

freq = 0
frequencies = set()
found = False
while not found:
    for d in deltas:
        freq += d
        if freq in frequencies:
            found = True
            break
        else:
            frequencies.add(freq)

print("Part 2: {}".format(freq))
