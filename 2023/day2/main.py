# Possible configurations
red_max = 12
green_max = 13
blue_max = 14

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

sum_id = 0

for line in lines:

    game_number = line.split(':')[0].split(' ')[1]
    second_part = line.split(':')[1]

    is_possible = True

    for current_game in second_part.split(';'):
        r = g = b = 0

        for part in current_game.strip().split(','):

            count, color = part.strip().split()
            count = int(count)

            if color == 'red':
                if count > red_max:
                    is_possible = False

            elif color == 'green':
                if count > green_max:
                    is_possible = False

            elif color == 'blue':

                if count > blue_max:
                    is_possible = False

    if is_possible:
        sum_id += int(game_number)

print(sum_id)
