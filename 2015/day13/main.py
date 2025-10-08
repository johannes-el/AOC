import itertools
from collections import defaultdict

def main():
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    like_status = defaultdict(dict)

    for line in lines:
        parts = line.strip().split(' ')
        first_name = parts[0]
        second_name = parts[-1].strip('.')

        # Determine if gain or lose
        happiness_score = int(parts[3])
        if parts[2] == 'lose':
            happiness_score = -happiness_score

        like_status[first_name][first_name] = 0
        like_status[first_name][second_name] = happiness_score

    # Brute force the ordering and remember the one that gives the biggest joy.
    names = []
    for i in like_status:
        names.append(i)

    max_score = 0

    for permutation in itertools.permutations(names):
        current_score = 0
        n = len(permutation)

        for i in range(n):
            person = permutation[i]
            left_neighbor = permutation[i - 1]
            right_neighbor = permutation[(i + 1) % n]

            current_score += like_status[person][left_neighbor]
            current_score += like_status[person][right_neighbor]

        if current_score > max_score:
            max_score = current_score

    print(max_score)


if __name__ == '__main__':
    main()
