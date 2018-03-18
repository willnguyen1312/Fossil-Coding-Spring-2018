

def readInput(filename='test3.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = map(lambda line: line.strip(), f.readlines())
    return lines


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    s = sorted(a)
    if s[0] == '0':
        i = 0
        while s[i] == '0':
            i += 1
        s[0], s[i] = s[i], '0'
    return s


def writeOutput(results, filename='test3.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = results
    f = open(filename, 'w')
    f.write('\n'.join(map(lambda line: ''.join(line), lines)))
    f.close()


def main():
    testcases = readInput('3.in')
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results, '3.out_tin')


if __name__ == "__main__":
    main()
