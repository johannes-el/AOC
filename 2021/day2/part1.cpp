#include <iostream>
#include <string>
#include <fstream>

int main()
{
	std::ifstream file("./input.txt");

	int horizontal_pos = 0;
	int depth = 0;

	if (!file.is_open())
	{
		std::cerr << "Could not open file" << std::endl;
		return -1;
	}

	std::string line{};
	while (std::getline(file, line))
	{
		if (line[0] == 'f')
		{
			horizontal_pos += line[8] - '0';
		}
		else if (line[0] == 'd')
		{
			depth += line[5] - '0';
		}
		else if (line[0] == 'u')
		{
			depth -= line[3] - '0';
		}
	}

	std::cout << horizontal_pos * depth << std::endl;

	return 0;
}
