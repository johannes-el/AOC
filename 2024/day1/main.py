def parse_line(line: str) -> tuple[int, int]:
    """Extract two integers from a line."""

    first_number = ""
    second_number = ""
    first = True

    for char in line:
        if char.isdigit():
            if first:
                first_number += char
            else:
                second_number += char
        else:
            first = False

    return int(first_number), int(second_number)


if __name__ == "__main__":

    left_list = []
    right_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = parse_line(line.strip())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    # ------------------------------------------------------
    # First problem
    # Solution: 2192892
    # ------------------------------------------------------
    total_distance = 0

    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    print(total_distance)

    # ------------------------------------------------------
    # Second problem:
    # Solution: 22962826
    # ------------------------------------------------------

    memo: dict[int, int] = dict()
    total_sim = 0

    for x in left_list:
        count = 0

        # The memo never triggers because all numbers
        # in the left list are unique [making it redundant].
        if x in memo.keys():
            total_sim += memo[x]
            continue

        for y in right_list:
            if x == y:
                count += 1

        result = x * count
        total_sim += result
        memo[x] = result

        count = 0

    print(total_sim)
