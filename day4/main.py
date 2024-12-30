if __name__ == "__main__":

    with open("input.txt", "r") as file:
        lines = file.readlines()

    total_count: int = 0

    horizontal = len(lines[0])
    vertical = len(lines)
    matrix = [[0 for i in range(horizontal)] for i in range(vertical)]

    # Add all lines to a 2D grid.
    for first_idx, line in enumerate(lines):
        for second_idx, char in enumerate(line):
            matrix[first_idx][second_idx] = char

    for i in range(vertical):
        for j in range(horizontal):
            pass

    print(total_count)
