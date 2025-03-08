#include <iostream>
#include <set>
#include <fstream>

const std::set<char> vowels_set = {'a', 'e', 'i', 'o', 'u'};
const std::set<std::string> forbidden = {"ab", "cd", "pq", "xy"};

bool three_vowels(const std::string &text) {
    int counter = 0;
    for (auto &x : text) {
        if (vowels_set.find(x) != vowels_set.end()) {
            counter++;
        }
    }
    return counter >= 3;
}

bool twice_in_row(const std::string &text) {
    for (size_t i = 0; i < text.length() - 1; ++i) {
        if (text[i] == text[i + 1]) {
            return true;
        }
    }
    return false;
}

bool not_contain(const std::string &text) {
    for (size_t i = 0; i < text.length() - 1; i++) {
        if (forbidden.find(text.substr(i, 2)) != forbidden.end()) {
            return false;
        }
    }
    return true;
}

int main() {
    std::ifstream file("./input.txt");

    if (!file.is_open()) {
        std::cerr << "Could not open file\n";
        return -1;
    }

    std::string line{};
    int nice_count = 0;

    while (std::getline(file, line)) {
        // Check the three conditions for "nice" strings
        if (three_vowels(line) && twice_in_row(line) && not_contain(line)) {
            nice_count++;
        }
    }

    std::cout << nice_count << std::endl;

    return 0;
}
