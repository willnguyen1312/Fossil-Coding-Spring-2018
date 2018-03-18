import datetime


def readInput(filename='test10.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = f.readlines()
    return map(lambda line: map(lambda x: int(x), line.split('/')), lines)


def solve(a):
    """
    solve the problem
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    dd = a[0]
    mm = a[1]
    yyyy = a[2]
    d1 = datetime.date(yyyy, mm, dd)
    d2 = datetime.date(yyyy, 1, 1)
    return (d1 - d2).days + 1


def writeOutput(results, filename='test10.out'):
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
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__ == "__main__":
    main()
