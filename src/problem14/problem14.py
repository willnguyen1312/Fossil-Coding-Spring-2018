

def readInput(filename='test14.in'):
    """
    read input file
    :param filename: filename
    :return: an array of testcases, each testcase is an array of numbers
    """
    f = open(filename, 'r')
    f.readline()
    lines = map(lambda x: x.strip(), f.readlines())
    return lines


def solve(a):
    """
    solve the problem: given a number, keep sum the
    :param a: an array of input numbers
    :return: output array that has been removed duplicated numbers
    """
    def reduce(num):
        if len(num) == 1:
            return num
        return reduce(str(sum(map(lambda x: int(x), num))))

    return reduce(a)


def writeOutput(results, filename='test14.out'):
    """
    write output file
    :param filename: filename
    :return: write results to file
    """
    lines = results
    f = open(filename, 'w')
    f.write('\n'.join(lines))
    f.close()


def main():
    testcases = readInput()
    results = map(lambda testcase: solve(testcase), testcases)
    writeOutput(results)


if __name__=='__main__':
    main()