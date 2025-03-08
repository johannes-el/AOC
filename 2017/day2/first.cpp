#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>

int main() {

  std::ifstream file("./input.txt");
  if (!file.is_open()) {
    std::cerr << "Couldn't open file\n";
    return -1;
  }

  std::string line{};

  auto split = [](const std::string &str) {
    std::istringstream iss(str);
    std::vector<int> tokens;

    std::string token;
    while (iss >> token) {
      tokens.emplace_back(std::stoi(token));
    }

    return tokens;
  };

  int sum = 0;

  while (std::getline(file, line)) {
    std::vector<int> numbers = split(line);
    auto max = std::max_element(numbers.begin(), numbers.end());
    auto min = std::min_element(numbers.begin(), numbers.end());

    sum += std::abs(*max - *min);
  }

  std::cout << sum << std::endl;

  return 0;
}
