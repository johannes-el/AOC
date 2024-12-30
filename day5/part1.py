if __name__ == "__main__":

    with open("input.txt", "r") as file:
        lines = file.readlines()

    page_numbers: list[(int, int)] = []

    line_iterator = iter(lines)

    for line in line_iterator:

        line = line.strip()
        if line == "":
            break

        first, second = line.split("|")
        num1, num2 = int(first), int(second)

        page_numbers.append((num1, num2))

    my_sum: int = 0

    for line in line_iterator:

        line_lookup: list[int] = [int(x) for x in line.strip().split(",")]
        line_mid: int = len(line_lookup) // 2
        mid_element = line_lookup[line_mid]

        map: dict[int, int] = dict()

        for idx, i in enumerate(line_lookup):
            map[i] = idx

        is_good = True

        for num1, num2 in page_numbers:
            if num1 in map and num2 in map and map[num1] > map[num2]:
                is_good = False
                break

        if is_good:
            my_sum += mid_element

    print(my_sum)
