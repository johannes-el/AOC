with open('./input.txt', 'r') as file:
    line = file.readline()

pos = (0, 0)
houses = {pos}

for char in line:
    if char == '<':
        pos = (pos[0] - 1, pos[1])
    elif char == '>':
        pos = (pos[0] + 1, pos[1])
    elif char == '^':
        pos = (pos[0], pos[1] - 1)
    elif char == 'v':
        pos = (pos[0], pos[1] + 1)

    houses.add(pos)

print(len(houses))
