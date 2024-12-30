import numpy as np
from enum import Enum


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

if __name__ == "__main__":

    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    horizontal = len(lines[0])
    vertical = len(lines)

    grid = [[' ' for i in range(horizontal)] for i in range(vertical)]

    startPos = (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[i][j] = char

            if char == "^":
                startPos = i, j

    visited_nodes = set()
    current_direction = Direction.UP

    current_node = startPos
    visited_nodes.add(startPos)

    while True:
        if current_direction == Direction.UP:
            proposed_pos = current_node[0] - 1, current_node[1]
        elif current_direction == Direction.RIGHT:
            proposed_pos = current_node[0], current_node[1] + 1
        elif current_direction == Direction.DOWN:
            proposed_pos = current_node[0] + 1, current_node[1]
        elif current_direction == Direction.LEFT:
            proposed_pos = current_node[0], current_node[1] - 1

        if proposed_pos[0] < 0 or proposed_pos[0] >= horizontal or proposed_pos[1] < 0 or proposed_pos[1] >= vertical:
            break

        if grid[proposed_pos[0]][proposed_pos[1]] == '#':

            if current_direction == Direction.UP:
                current_direction = Direction.RIGHT

            elif current_direction == Direction.RIGHT:
                current_direction = Direction.DOWN

            elif current_direction == Direction.DOWN:
                current_direction = Direction.LEFT

            elif current_direction == Direction.LEFT:
                current_direction = Direction.UP
        else:
            current_node = proposed_pos
            visited_nodes.add(proposed_pos)



    print(len(visited_nodes))
