#include <iostream>

std::string look_and_say(std::string value) {
  if (value.empty()) return "";

  std::string new_value = "";
  int count = 1;

  for (size_t i = 1; i < value.length(); i++) {
    if (value[i] == value[i - 1]) {
      count++;
    } else {
      new_value += std::to_string(count) + value[i - 1];
      count = 1;
    }
  }
  return new_value + std::to_string(count) + value.back();
}

int main() {

  std::string value = "3113322113";

  int iteration_amount = 40; 

  for (int i = 0; i < iteration_amount; i++)
  {
    value = look_and_say(value);
  }

  std::cout << value.length() << std::endl;
  
  return 0;
}
