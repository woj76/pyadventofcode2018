file = open("data/data05.txt", "rt")

def polymer_match(lst, position):
    if position + 1 >= len(lst):
        return False
    c1 = lst[position]
    c2 = lst[position+1]
    if ((c1.islower() and c2.isupper()) or (c1.isupper() and c2.islower())) and c1.upper() == c2.upper():
        return True
    return False

part2 = True

ls = [c for c in file.readline()[:-1]]

min_result = float('inf')

for c in range(ord('a'), ord('z')+1):
    if part2:
        smaller_ls = [sc for sc in ls if sc != chr(c) and sc != chr(c).upper()]
    else:
        smaller_ls = ls
    while True:
        positions = []
        i = 0
        while i < len(smaller_ls):
            if polymer_match(smaller_ls, i):
                positions = [i] + positions
                i += 2
            else:
                i += 1
        if len(positions) == 0:
            break
        for p in positions:
            del smaller_ls[p:p+2]
    if not part2:
        print("Part 1: {}".format(len(smaller_ls)))
        break
    else:
        min_result = min(min_result, len(smaller_ls))

if part2:
    print("Part 2: {}".format(min_result))
