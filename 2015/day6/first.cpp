#include <iostream>
#include <fstream>
#include <regex>

enum class Instruction {
  TOGGLE,
  TURN_OFF,
  TURN_ON,
};

struct RectangleInstruction {
  int x1;
  int y1;
  int x2;
  int y2;
  Instruction instruction;
};

RectangleInstruction process_command(const std::string &line) {
  std::regex regex("^(toggle|turn (on|off)) (\\d+),(\\d+) through (\\d+),(\\d+)$");
  std::smatch match;

  RectangleInstruction rect;

  if (std::regex_match(line, match, regex)) {
    std::string action = match[1];

    if (action == "toggle") rect.instruction = Instruction::TOGGLE;
    if (action == "turn on") rect.instruction = Instruction::TURN_ON;
    if (action == "turn off") rect.instruction = Instruction::TURN_OFF;

    rect.x1 = std::stoi(match[3]);
    rect.y1 = std::stoi(match[4]);
    rect.x2 = std::stoi(match[5]);
    rect.y2 = std::stoi(match[6]);
  }
  return rect;
}

int main() {
  std::ifstream file("input.txt");

  if (!file.is_open()) {
    std::cerr << "Could not open file\n";
    return -1;
  }

  std::string line{};
  const int light_amount = 1000;
  bool light_grid[light_amount][light_amount] = {};

  while (std::getline(file, line)) {
    RectangleInstruction rect = process_command(line);

    switch (rect.instruction) {
    case Instruction::TOGGLE:
      for (int i = rect.y1; i <= rect.y2; i++) {
        for (int j = rect.x1; j <= rect.x2; j++) {
          light_grid[i][j] = !light_grid[i][j];
        }
      }
      break;
    case Instruction::TURN_OFF:
      for (int i = rect.y1; i <= rect.y2; i++) {
        for (int j = rect.x1; j <= rect.x2; j++) {
          light_grid[i][j] = false;
        }
      }
      break;
    case Instruction::TURN_ON:
      for (int i = rect.y1; i <= rect.y2; i++) {
        for (int j = rect.x1; j <= rect.x2; j++) {
          light_grid[i][j] = true;
        }
      }
      break;
    default:
      break;
    }
  }

  int lit_lights = 0;

  for (int i = 0; i < light_amount; i++) {
    for (int j = 0; j < light_amount; j++) {
      if (light_grid[i][j]) lit_lights++;
    }
  }

  std::cout << lit_lights << std::endl;

  file.close();
}
