#!/usr/bin/python3

file = open("../data/data08.txt", "rt")
data = [int(x) for x in file.read().strip().split(' ')]
file.close()

part2 = False

#mem = {}
#mem[0] = 0

def build_tree(dlist, index):
	n_children = dlist[index]
	n_meta = dlist[index + 1]
	children = []
	next_index = index + 2
	for i in range(n_children):
		next_index,t = build_tree(dlist, next_index)
		children.append(t)
	meta = []
	for j in range(n_meta):
		m_value = dlist[next_index]
		# mem[0] += m_value
		meta.append(m_value)
		next_index += 1
	return (next_index, (meta,children))

tree = build_tree(data, 0)[1]

def sum_meta(t):
	meta, children = t
	r = sum(meta)
	for c in children:
		r += sum_meta(c)
	return r

def sum_meta2(t):
	meta, children = t
	if children == []:
		return sum(meta)
	else:
		r = 0
		for i in meta:
			if 0 < i < len(children) + 1:
				r += sum_meta2(children[i-1])
	return r

print(sum_meta2(tree))
