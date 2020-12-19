#!/usr/bin/python3

part2 = True

num_players = 410
last_marble = 72059
if part2:
	last_marble *= 100

class Marbles:
	def __init__(self):
		self.val = 0
		self.prev = self
		self.next = self
	def next_marble(self,v):
		node = Marbles()
		node.val = v
		ins_node = self.next.next
		node.prev = ins_node.prev
		ins_node.prev.next = node
		node.next = ins_node
		ins_node.prev = node
		return node
	def remove_marble(self):
		node = self.prev.prev.prev.prev.prev.prev.prev
		v = node.val
		node.next.prev = node.prev
		node.prev.next = node.next
		return node.next, v

marbles = Marbles()
next_marble = 1
player = 0

scores = [0] * num_players

for _ in range(last_marble):
	if next_marble % 23 == 0:
		scores[player] += next_marble
		marbles, points = marbles.remove_marble()
		scores[player] += points
	else:
		marbles = marbles.next_marble(next_marble)
	next_marble += 1
	player = (player + 1) % num_players

print(max(scores))
