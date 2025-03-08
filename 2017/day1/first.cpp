#include <iostream>
#include <fstream>

int main() {

  std::string line{};
  std::ifstream file("./input.txt");

  if (!file.is_open()) {
    std::cerr << "Could not open file\n";
    return -1;
  }

  int sum = 0;

  while (std::getline(file, line)) {
    for (int i = 0; i < line.length() - 1; ++i) {
      if (line[i] - '0' == line[i + 1] - '0') {
	sum += line[i] - '0';
      }
    }
    if (line[line.length() - 1] == line[0]) sum += line[0] - '0';
  }

  std::cout << sum << std::endl;

  file.close();

  return 0;
}
