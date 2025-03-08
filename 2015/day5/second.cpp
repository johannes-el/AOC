#include <iostream>
#include <fstream>

bool repeats(const std::string &text) {
  for (size_t i = 0; i < text.length() - 2; ++i) {
    std::string current_string = text.substr(i, 2);
    size_t pos = text.find(current_string, i + 2);

    if (pos != std::string::npos) return true;
  }
  return false;
}

bool repeats_with_spacing(const std::string &text) {
  for (int i = 0; i < text.length() - 2; ++i) {
    if (text[i] == text[i + 2]) return true;
  }
  return false;
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
      if (repeats(line) && repeats_with_spacing(line)) {
            nice_count++;
        }
    }

    std::cout << nice_count << std::endl;

    return 0;
}
