def restore_program(input_list):

    input_list[1] = 12
    input_list[2] = 2

    i = 0

    while input_list[i] != 99:
        if input_list[i] == 1:
            input_list[input_list[i + 3]] = input_list[input_list[i + 1]] + input_list[input_list[i + 2]]
        elif input_list[i] == 2:
            input_list[input_list[i + 3]] = input_list[input_list[i + 1]] * input_list[input_list[i + 2]]
        i += 4

    return input_list[0]


with open("./input.txt", "r") as file:
    lines = file.readlines()


for line in lines:

    int_line = [int(x) for x in line.strip().split(',')]
    result = restore_program(int_line)
    print(result)
