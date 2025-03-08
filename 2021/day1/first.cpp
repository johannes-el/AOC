#include <iostream>
#include <fstream>

int main() {

  std::ifstream file("./input.txt");
  std::string line{};

  int iter = 0;

  int previous = 0;

  int increased = 0;

  while (std::getline(file, line)) {
    int num = std::stoi(line);

    if (iter == 0) {
      previous = num;
      iter++;
      continue;
    }

    if (previous < num) {
      previous = num;
      increased++;
    }
  }

  std::cout << increased << std::endl;

  return 0;
}
