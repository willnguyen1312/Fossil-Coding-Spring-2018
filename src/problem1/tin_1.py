

def readInput(filename='test1.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    lines = f.readlines()
    return lines


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    s = a.strip()
    s2 = s.replace('  ',' ')
    while len(s2) != len(s):
        s, s2 = s2, s2.replace('  ', ' ')
    return s2


def writeOutput(results, filename='test1.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = map(lambda result: str(result), results)
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput('1.in')
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results, '2.out_tin')


if __name__ == "__main__":
    main()
