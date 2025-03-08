#include <iostream>
#include <vector>
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
    for (int x = 0; x < numbers.size(); x++) {
	for (int y = 0; y < numbers.size(); y++) {
	  if (x == y)
	    continue;
	  if (numbers[x] % numbers[y] == 0 && numbers[y] != 0) {
	    sum += numbers[x] / numbers[y];
          } else if (numbers[y] % numbers[x] == 0 && numbers[x] != 0) {
	    sum += numbers[y] / numbers[x];
	  }
	}
    }
  }

  std::cout << sum << std::endl;

  return 0;
}
