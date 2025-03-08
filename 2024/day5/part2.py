def selection_sort(array, less):
    for i in range(len(array)):

        minIdx = i
        for j in range(i + 1, len(array)):
            if less(array[j], array[minIdx]):
                minIdx = j
        if minIdx != i:
            array[minIdx], array[i] = \
                array[i], array[minIdx]
    return array


def sort_according_to_rules(line, rules) -> int:

    new_dict: dict[int, set[int]] = dict()
    for x, y in rules:
        if x in new_dict.keys():
            new_dict[x].add(y)
        else:
            new_dict[x] = {y}

    def less(x, y) -> bool:
        if x in new_dict.keys() and y in new_dict[x]:
            return False
        return True

    arr = selection_sort(line, less)

    return arr[len(arr) // 2]


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

        if not is_good:
            my_sum += sort_according_to_rules(line_lookup, page_numbers)

    print(my_sum)
