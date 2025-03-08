#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

bool already_visited(std::pair<int, int> pos,
			std::vector<std::pair<int, int>> &positions) {
    for (auto &position : positions) {
	if (position == pos) {
	return true;
	}
    }
    return false;
};

int main() {

  std::ifstream file("./input.txt");

  if (!file.is_open()) {
    std::cerr << "Could not open file\n";
    return -1;
  }

  std::string line{};

  std::vector<std::pair<int, int>> positions;

  positions.push_back({0, 0});
  std::pair<int, int> current_position = {0, 0};
  int sum = 0;

  while (std::getline(file, line)) {
    for (auto &i : line) {
      if (i == '^') {
	current_position.second -= 1;
      }
      else if (i == 'v') {
	current_position.second += 1;
      } else if (i == '>') {
	current_position.first += 1;
      } else if (i == '<') {
	current_position.first -= 1;
      }
      std::cout << current_position.first << ' ' << current_position.second << std::endl;
      if (!already_visited(current_position, positions)) {
	sum += 1;
      }
      positions.push_back(current_position);
    }
  }

  std::cout << sum << std::endl;

  file.close();

  return 0;
}
