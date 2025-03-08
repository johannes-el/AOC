if __name__ == "__main__":

    with open("./input.txt", 'r') as file:
        lines = [line for line in file.readlines()]

    sum = 0

    for line in lines:
        seen_words = []

        valid = True

        current_word = ""
        for char in line:
            if char == ' ' or char == '\n':
                if current_word in seen_words:
                    valid = False
                    break
                else:
                    seen_words.append(current_word)

                current_word = ""
            else:
                current_word += char

        if valid:
            sum += 1

    print(sum)
