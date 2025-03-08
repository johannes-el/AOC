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
    int n = line.length();
    int check_range = n / 2;

    for (int i = 0; i < n; i++) {
      if (line[i] - '0' == line[(i + check_range) % n] - '0') {
	sum += line[i] - '0';
      }
    }
  }

  std::cout << sum << std::endl;

  file.close();

  return 0;
}
