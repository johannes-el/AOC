#include <iostream>
#include <fstream>
#include <string>
#include <numeric>
#include <deque>

int main() {
    std::ifstream file("./input.txt");
    std::string line{};

    int increased = 0;
    std::deque<int> triples;

    while (std::getline(file, line)) {
        int num = std::stoi(line);

        triples.push_back(num);

        if (triples.size() > 3)
        {
            int first_triple = std::accumulate(triples.begin(), triples.begin() + 3, 0);
            triples.pop_front();
            int second_triple = std::accumulate(triples.begin(), triples.begin() + 3, 0);

            if (second_triple > first_triple) {
                increased++;
            }
        }
    }

    std::cout << increased << std::endl;

    return 0;
}
