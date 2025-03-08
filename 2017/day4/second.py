if __name__ == "__main__":

    with open("./input.txt", 'r') as file:
        lines = [line for line in file.readlines()]

    sum = 0

    for line in lines:
        anagrams = dict()

        current_word = ""
        for char in line:
            if char == ' ' or char == '\n':
                sorted_word = "".join(sorted(current_word))
                if sorted_word not in anagrams.keys():
                    anagrams[sorted_word] = [current_word]

                else:
                    anagrams[sorted_word].append(current_word)

                current_word = ""
            else:
                current_word += char

        for matching_words in anagrams.values():
            if len(matching_words) > 1:
                print(matching_words)
                sum += 1

    print(sum)
