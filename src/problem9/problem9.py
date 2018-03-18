

def readInput(filename='test9.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = f.readlines()
    return map(lambda line: map(lambda x: int(x), line.split(' ')), lines)


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    h = set()
    b = []
    for each in a:
        if each not in h:
            h |= {each}
            b += [each]
    return b


def writeOutput(results, filename='test9.out'):
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