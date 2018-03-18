

def readInput(filename='test13.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    t = int(f.readline())
    testcases = []
    for i in range(t):
        n = int(f.readline())
        testcase = []
        for j in range(n):
            line = map(lambda x: int(x), f.readline().split(' '))
            testcase.append(line)
        testcases.append(testcase)
    return testcases


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    total = sum(map(len, a))
    result = []
    i = 0
    while total > 0:
        if len(a[i % len(a)]) > 0:
            result.append( a[i % len(a)].pop(0) )
            i += 1
            total -= 1
        else:
            i += 1

    return result


def writeOutput(results, filename='test13.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = map(lambda result: ' '.join(map(lambda x: str(x), result)), results)
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__=='__main__':
    main()