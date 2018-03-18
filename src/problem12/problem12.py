

def readInput(filename='test12.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = map(lambda x: map(lambda y: str(int(y)), x.strip('\n').split()), f.readlines())
    return lines


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    return sorted(a)


def writeOutput(results, filename='test12.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = map(lambda result: ' '.join(result), results)
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__=='__main__':
    main()