def isSafe(line: str) -> bool:
    """Check if the given report is safe."""

    # Convert the levels to integers
    levels = [int(x) for x in line.split()]

    if len(levels) < 2:
        return True

    isIncreasing = levels[0] < levels[1]

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if isIncreasing:
            if diff not in [1, 2, 3]:
                return False
        else:
            if diff not in [-1, -2, -3]:
                return False

    return True

def isSafeAfterRemovingFailure(line: str) -> bool:
    """Check if removing one bad level can make the report safe."""

    # Convert the levels to integers
    levels = [int(x) for x in line.split()]

    if isSafe(line):
        return True

    for i in range(len(levels)):
        # Remove the element at index i
        new_levels = levels[:i] + levels[i + 1:]

        if isSafe(' '.join(map(str, new_levels))):
            return True

    return False

if __name__ == "__main__":

    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Part 1: Count how many reports are safe without any removal
    safeReportCount = sum(1 for report in lines if isSafe(report))
    print(safeReportCount)

    # Part 2: Count how many reports are safe after removing one bad level
    semiSafeReportCount = sum(1 for report in lines if isSafeAfterRemovingFailure(report))
    print(semiSafeReportCount)

