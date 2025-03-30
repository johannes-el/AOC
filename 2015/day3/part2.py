def move(pos):
    if char == '<':
        pos = (pos[0] - 1, pos[1])
    elif char == '>':
        pos = (pos[0] + 1, pos[1])
    elif char == '^':
        pos = (pos[0], pos[1] - 1)
    elif char == 'v':
        pos = (pos[0], pos[1] + 1)
    return pos


with open('./input.txt', 'r') as file:
    line = file.readline()

pos_santa = (0, 0)
pos_robo = (0, 0)

houses_visited = {(0, 0)}

santa_turn = True

for char in line:
    if santa_turn:
        pos_santa = move(pos_santa)
        houses_visited.add(pos_santa)
    else:
        pos_robo = move(pos_robo)
        houses_visited.add(pos_robo)

    santa_turn = not santa_turn

print(len(houses_visited))
