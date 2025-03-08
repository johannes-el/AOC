from typing import Optional

def calculate_sum(lines, checkEnabled: bool) -> int:
    number_pairs: list[str] = []

    enabled = True

    for line in lines:
        sub_string = ""
        memorize: bool = False

        for char in line:
            if char == "m":
                memorize = True
            if memorize:
                sub_string += char
            if char == ")":
                memorize = False
                idx = sub_string.rfind("mul(")
                if idx == -1:
                    continue
                sub_string = sub_string[(idx + 4):-1]
                number_pairs.append(sub_string)
                sub_string = ""

    number_pairs = [x for x in number_pairs if x]

    total_sum: int = 0
    for pair in number_pairs:
        if "," not in pair or pair.count(",") != 1:
            continue
        first, second = pair.split(",", 1)
        if not first.isdigit() or not second.isdigit():
            continue
        total_sum += int(first) * int(second)
    return total_sum

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()

    total_sum: int = calculate_sum(lines, False)
    # First solution: 167650499
    print(total_sum)

    total_sum: int = calculate_sum(lines, True)
