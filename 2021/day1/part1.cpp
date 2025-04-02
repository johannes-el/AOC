#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("./input.txt");
    std::string line{};

    int previous = 0;
    int increased = 0;

    bool firstLine = true;

    while (std::getline(file, line)) {
        int num = std::stoi(line);

        if (firstLine) {
            previous = num;
            firstLine = false;
            continue;
        }

        if (num > previous) {
            increased++;
        }
        previous = num;
    }

    std::cout << increased << std::endl;

    return 0;
}
