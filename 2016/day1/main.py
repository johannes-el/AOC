def parse_input(line):
    instructions = line.strip().split(', ')
    return [(instr[0], int(instr[1:])) for instr in instructions]


def move():
    with open("input.txt") as f:
        line = f.readline()

    instructions = parse_input(line)

    # NORTH, EAST, SOUTH, WEST
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heading = 0  # start facing NORTH
    x, y = 0, 0

    already_visited = set()
    already_visited.add((x, y))

    for turn, steps in instructions:
        if turn == 'R':
            heading = (heading + 1) % 4
        elif turn == 'L':
            heading = (heading - 1) % 4

        dx, dy = directions[heading]

        for _ in range(steps):
            x += dx
            y += dy

            if (x, y) in already_visited:
                # First location visited twice
                return abs(x) + abs(y)

            already_visited.add((x, y))

    # If no location is visited twice
    return abs(x) + abs(y)


if __name__ == "__main__":
    distance = move()
    print(f"Distance to first location visited twice: {distance}")
