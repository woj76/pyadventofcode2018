current_schedule = None
guard_id = None
last_time = 0
sleeping = False
schedules = {}

file = open("data/data04.txt", "rt")

for l in sorted([x[:-1] for x in file.readlines()]):
    if l.find("Guard") != -1:
        if current_schedule != None:
            schedules[guard_id] = [current_schedule] + ([] if not guard_id in schedules else schedules[guard_id])
        guard_id = int(l.split(' ')[3][1:])
        sleeping = False
        last_time = 0
        current_schedule = [False] * 60
    else:
        tm = int(l.split(' ')[1][3:5])
        current_schedule[last_time:tm] = [sleeping] * (tm - last_time)
        sleeping = not sleeping
        last_time = tm
schedules[guard_id] = [current_schedule] + ([] if not guard_id in schedules else schedules[guard_id])

total_minutes_max = float('-inf')
sleepy_guard = None
sleepy_minute_guard = 0

for g in schedules:
    ss = schedules[g]
    minutes_asleep = 0
    sleepy_minute_max = float('-inf')
    sleepy_minute = 0
    for minute in range(60):
        max_minute = 0
        for j in range(len(ss)):
            if ss[j][minute]:
                minutes_asleep += 1
                max_minute += 1
        if max_minute > sleepy_minute_max:
            sleepy_minute_max = max_minute
            sleepy_minute = minute
    if minutes_asleep > total_minutes_max:
        total_minutes_max = minutes_asleep
        sleepy_guard = g
        sleepy_minute_guard = sleepy_minute

print("Part 1: {}".format(sleepy_guard * sleepy_minute_guard))

sleepy_minute_max = float('-inf')
sleepy_guard = None
sleepy_minute_guard = None

for minute in range(60):
    for g in schedules:
        ss = schedules[g]
        minutes_asleep = 0
        for j in range(len(ss)):
            if ss[j][minute]:
                minutes_asleep += 1
        if minutes_asleep > sleepy_minute_max:
            sleepy_minute_max = minutes_asleep
            sleepy_guard = g
            sleepy_minute_guard = minute

print("Part 2: {}".format(sleepy_guard * sleepy_minute_guard))
