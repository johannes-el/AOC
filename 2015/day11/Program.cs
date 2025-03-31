namespace Day11;

class Program
{
    static bool ContainsThreeInRow(String puzzleInput)
    {
	char[] input = puzzleInput.ToCharArray();
	int counter = 1;
	for (int i = 1; i < puzzleInput.Length; i++)
	{
	    if (++input[i - 1] == puzzleInput[i])
	    {
		counter++;
	    }
	    else
	    {
		counter = 1;
	    }

	    if (counter == 3)
	    {
		return true;
	    }
	}
	return false;
    }

    static bool ContainsInvalidCharacters(String puzzleInput)
    {
	for (int i = 0; i < puzzleInput.Length; i++)
	{
	    if (puzzleInput[i] == 'i' || puzzleInput[i] == 'l' || puzzleInput[i] == 'o')
	    {
		return false;
	    }
	}
	return true;
    }

    static bool ContainsNonOverlappingPairs(String puzzleInput)
    {
	int counter = 0;
	int index = -1;

	for (int i = 1; i < puzzleInput.Length; i++)
	{
	    if (puzzleInput[i - 1] == puzzleInput[i] && i - 1 != index)
	    {
		index = i;
		counter++;
	    }
	}

	if (counter == 2)
	{
	    return true;
	}
	return false;
    }

    static String IncrementString(String puzzleInput)
    {
	char[] inputChars = puzzleInput.ToCharArray();

	for (int i = inputChars.Length - 1; i >= 0; i--)
	{
	    if (inputChars[i] != 'z')
	    {
		inputChars[i]++;
		break;
	    }
	    else {
		inputChars[i] = 'a';
	    }
	}
	return new String(inputChars);
    }

    static String findValidIncrement(String input)
    {
	while (!ContainsThreeInRow(input)
	    || !ContainsInvalidCharacters(input)
	    || !ContainsNonOverlappingPairs(input))
	{
	    input = IncrementString(input);
	}

	return input;
    }

    static void Main(string[] args)
    {
	String puzzleInput1 = "hepxcrrq";

	String firstResult = findValidIncrement(puzzleInput1);
	Console.WriteLine("Part1: " + firstResult);

	String puzzleInput2 = IncrementString(firstResult);
	String secondResult = findValidIncrement(puzzleInput2);

	Console.WriteLine("Part2: " + secondResult);
    }
}
