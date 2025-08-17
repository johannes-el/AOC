from collections import defaultdict

with open('./input.txt', 'r') as f:
    content = [line.strip().split(' -> ') for line in f.readlines()]

grid = defaultdict(int)

for line in content:

    x1, y1 = map(int, line[0].split(','))
    x2, y2 = map(int, line[1].split(','))

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[(x1, y)] += 1

    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[(x, y2)] += 1

overlaps = sum(1 for v in grid.values() if v >= 2)
print(overlaps)
