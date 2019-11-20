from itertools import cycle

changes = [];
with open('2018/day01/input.txt', 'r') as f:
    for line in f:
        if line != '':
            changes.append(int(line));

startFrequency = 0;
currentFrequency = startFrequency;
reachedFrequencies = [];

part1 = 0;
part2 = 0;

for change in changes:
    part1 += change;

print("Part 1:", part1);

for change in cycle(changes):
    part2 += change;
    if part2 in reachedFrequencies:
        break;
    reachedFrequencies.append(part2);

print("Part 2:", part2);
