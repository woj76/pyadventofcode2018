#!/snap/bin/pypy3

with open("../data/data24.txt", "rt") as file:
	[team1,team2] = file.read().strip().split('\n\n')
	team1 = team1.strip().split('\n')
	team2 = team2.strip().split('\n')

part2 = True

def parse_team(team, boost):
	team_name = team[0][:-1]
	groups = []
	for t in team[1:]:
		if '(' in t:
			i1 = t.index('(')
			i2 = t.index(')')
			ft = t[i1+1:i2]
			ft = ft.split('; ')
			t = t[:i1-1]+t[i2+1:]
		else:
			ft = []
		weaks = []
		immunes = []
		for wi in ft:
			if wi[:8] == "weak to ":
				weaks = wi[8:].split(', ')
			elif wi[:10] == "immune to ":
				immunes = wi[10:].split(', ')
		t = t.split(' ')
		groups.append((team_name, int(t[0])*(int(t[12])+boost), int(t[17]), int(t[0]), int(t[4]), int(t[12])+boost, t[13], weaks, immunes))
	return groups

def power(team):
	r = 0
	for t in team:
		r += t[3]
	return r


def try_game(boost):
	g1 = parse_team(team1, boost)
	g2 = parse_team(team2, 0)

	won = None
	while True:
		g1.sort()
		g1.reverse()
		g2.sort()
		g2.reverse()
		attackers = []
		(pt1, pt2) = (power(g1), power(g2))
		for tm, t1, t2 in [(12, g1, g2), (21, g2, g1)]:
			selected = []
			for i,g in enumerate(t1):
				eff_power = g[1]
				if eff_power == 0:
					continue
				damage_type = g[6]
				max_damage = float('-inf')
				selected_enemy = None
				for j,eg in enumerate(t2):
					if j in selected or eg[1] == 0:
						continue
					damage = eff_power
					if damage_type in eg[8]:
						damage = 0
						continue
					elif damage_type in eg[7]:
						damage *= 2
					if damage > max_damage:
						max_damage = damage
						selected_enemy = j
				if selected_enemy != None:
					selected.append(selected_enemy)
					attackers.append((g[2], tm, i, selected_enemy))
		attackers.sort()
		attackers.reverse()
		for _, t, a, d in attackers:
			att, df = (g1, g2) if t == 12 else (g2, g1)
			att_group = att[a]
			df_group = df[d]
			att_eff_power = att_group[1]
			damage_type = att_group[6]
			df_name, df_eff_power, df_init, df_units, df_points, df_damage, df_damage_type, df_weaks, df_immunes = df_group
			if damage_type in df_weaks:
				att_eff_power *= 2
			if att_eff_power == 0 or df_eff_power == 0:
				continue
			kill_units = att_eff_power // df_points
			if kill_units > df_units:
				kill_units = df_units
			df_units -= kill_units
			df[d] = (df_name, df_units*df_damage, df_init, df_units, df_points, df_damage, df_damage_type, df_weaks, df_immunes)
			if power(df) == 0:
				won = att
				break
		if (pt1, pt2) == (power(g1), power(g2)) or won != None:
			break
	return (won[0][0], power(won)) if won != None else (None, 0)

if part2:
	booster = 0
	while True:
		n,res = try_game(booster)
		if n == "Immune System":
			break
		booster += 1
else:
	_,res = try_game(0)

print(f"Part {2 if part2 else 1}: {res}")
